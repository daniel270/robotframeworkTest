import os
from datetime import datetime
from robot import rebot
import shutil
import json


class ParallelRunner:
    IMAGE_NAME = 'robotfwk'
    ENTRY_SCRIPT = './execute-suite.sh'
    ROBOT_XML = 'SUITE_output.xml'
    JUNIT_XML = 'SUITE_junit.xml'
    ANNOTATIONS_JSON = "SUITE_annotations.json"
    HTML_REPORT = "allsuites_report.html"
    HTML_LOG = "allsuites_log.html"

    def __init__(self, execution_file, suite_base_path, output_base_path, max_suites):
        self.execution_file_path = execution_file
        self.suite_base_path = suite_base_path
        self.output_base_path = output_base_path
        self.max_suites = max_suites
        self.execution_file_json = None
        self.output_path = None
        self.suite_batches = None
        self.execution_name = None
        self.environment_file = None

    def execute_suites(self):
        print('Executing parallel suites from file: %s' % self.execution_file_path)
        try:
            self.__load_execution_file()
            self.__setup_output_directory()
            self.__divide_into_batches()
            batch_count = 1
            for batch in self.suite_batches:
                try:
                    print('Execute batch %s set of containers' % str(batch_count))
                    self.__execute_batch_of_containers(batch)
                    print('Batch %s completed' % str(batch_count))
                    batch_count += 1
                except Exception:
                    pass
            self.__merge_container_reports()
            self.__copy_files_to_jenkins_workspace()
            print('Execution completed')
        except Exception as e:
            print('Error executing parallel suites : %s' % str(e))
            raise

    def __merge_container_reports(self):
        """Merges the robot framework output files from each container"""
        print('Copying container output xml files to top level')
        files_to_merge = []
        try:
            for suite in self.execution_file_json['suites']:
                if 'suitefile' in suite:
                    name = suite['suitefile'].replace('.robot', '')
                else:
                    name = suite['suitedirectory']
                print('Copying xml file for suite: %s' % name)
                output_xml_path = os.path.join(self.output_path, name, ParallelRunner.ROBOT_XML.replace('SUITE', name))
                destination_path = os.path.join(self.output_path, ParallelRunner.ROBOT_XML.replace('SUITE', name))
                shutil.copyfile(src=output_xml_path, dst=destination_path)
                files_to_merge.append(destination_path)
        except Exception:
            pass
        print('Merging container output xml into html report')
        try:
            log_path = os.path.join(self.output_path, 'allsuites_log.html')
            report_path = os.path.join(self.output_path, 'allsuites_report.html')
            rebot(*files_to_merge, name='AllSuites', log=log_path, report=report_path)
        except Exception as e:
            print('Error merging container xml output: %s' % str(e))
            raise

    def __divide_into_batches(self):
        """Divides the list of suites into batches as per max suites"""
        print('Creating batches for parallel execution')
        num_suites = len(self.execution_file_json['suites'])
        full_batches = num_suites // self.max_suites
        print('- Full batches=%s' % full_batches)
        if num_suites % self.max_suites > 0:
            has_partial = True
        else:
            has_partial = False
        print('- Partial batch at end: %s' % has_partial)
        if has_partial:
            total_batches = full_batches + 1
        else:
            total_batches = full_batches
        print('- %s suites will be divided into %s container batches using max suites %s' % (
            num_suites, total_batches, self.max_suites))
        self.suite_batches = []
        # split full batches
        for batch_counter in range(0, full_batches):
            start_index = batch_counter * self.max_suites
            batch = []
            for counter in range(start_index, start_index + self.max_suites):
                batch.append(self.execution_file_json['suites'][counter])
            self.suite_batches.append(batch)
        print('- full batches created', self.suite_batches)
        # add partial batch
        if has_partial:
            start_index = full_batches * self.max_suites
            batch = []
            for counter in range(start_index, num_suites):
                batch.append(self.execution_file_json['suites'][counter])
            self.suite_batches.append(batch)
            print('- partial batch created', self.suite_batches)

    def __load_execution_file(self):
        """Loads the execution file and checks all suites exist, also basic validation of the json file"""
        with open(self.execution_file_path, 'r') as json_file:
            self.execution_file_json = json.load(json_file)
        # check each suite directory or file exists
        for suite in self.execution_file_json['suites']:
            if 'suitefile' in suite:
                suite_file_path = os.path.join(self.suite_base_path, suite['suitefile'])
                if not os.path.isfile(suite_file_path):
                    print('Suite file not found: %s' % suite_file_path)
                    raise Exception('Suite file not found, aborting: %s' % suite_file_path)
            elif 'suitedirectory' in suite:
                suite_dir_path = os.path.join(self.suite_base_path, suite['suitedirectory'])
                if not os.path.isdir(suite_dir_path):
                    print('Suite directory not found, aborting: %s' % suite_dir_path)
                    raise Exception('Suite directory not found, aborting: %s' % suite_dir_path)
            else:
                print('No suitefile or suitedirectory specified for suite')
                raise Exception('No suitefile or suitedirectory specified for suite, aborting')
        # check suite name specified
        if 'name' in self.execution_file_json:
            print('Execution list name: %s' % self.execution_file_json['name'])
            self.execution_name = self.execution_file_json['name'].replace(' ', '_')
        else:
            print('No execution name was specified in json file')
            raise Exception('No execution name specified in json file, aborting')
        # get environment file name
        if 'environmentfile' in self.execution_file_json:
            print('Execution environment file: %s' % self.execution_file_json['environmentfile'])
            self.environment_file = self.execution_file_json['environmentfile']
        else:
            self.environment_file = 'NotSet'
        print('Suite execution file was loaded')

    def __setup_output_directory(self):
        """Sets up the output directory in the output base path"""
        print('Setting up output directory')
        time_stamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        self.output_path = os.path.join(self.output_base_path, '%s_%s' % (self.execution_name, time_stamp))
        print('- Creating output directory: %s' % self.output_path)
        os.makedirs(self.output_path)
        print('- Output directory created')
