# ----------------------------------------------------------------------
# Robot Parallel runner in docker containers
#
# Assumptions:
# - Executing on a linux vm with all pre-needed software installed
# - Docker container called "robotfwk" already pre-built
# Command line parameters:
# - executionfile : Path to a file containing what to execute
# - suitebase : Path to parent directory containing all suites
# - outputbase : Path to root directory of all outputs
# - maxsuites : Number of max suites to execute in parallel
# ----------------------------------------------------------------------

import argparse
import os.path
from robotkeywords.runner.parallelrunner import ParallelRunner


def main():
    parser = argparse.ArgumentParser(description='Required command line parameters')
    parser.add_argument("-s", "--executionfile", type=str, required=True, help="Path of json file of what to execute")
    parser.add_argument("-b", "--suitebase", type=str, required=True, help="Base path for all suites")
    parser.add_argument("-o", "--outputbase", type=str, required=True, help="Path to outputs root directory")
    parser.add_argument("-m", "--maxsuites", type=int, required=True, help="Max suites to execute at same time")
    args = parser.parse_args()
    print('Execution file = %s' % args.executionfile)
    print('Suites base directory = %s' % args.suitebase)
    print('Output root directory: %s' % args.outputbase)
    print('Max parallel suites: %s' % args.maxsuites)
    # check input parameters
    if args.maxsuites < 1:
        print('maxsuites needs to be >1')
        exit(1)
    if not os.path.exists(args.executionfile):
        print('executionfile file not found')
        exit(1)
    if not os.path.isdir(args.suitebase):
        print('suitebase directory not found')
        exit(1)
    if not os.path.isdir(args.outputbase):
        print('outputbase directory not found')
        exit(1)
    # execute
    try:
        runner = ParallelRunner(execution_file=args.executionfile, suite_base_path=args.suitebase,
                                output_base_path=args.outputbase, max_suites=args.maxsuites)
        runner.execute_suites()
    except Exception as e:
        print('Error - %s' % str(e))
        exit(1)


if __name__ == "__main__":
    main()
