#!/bin/bash
echo "Creating results directory"
SCRIPT_PATH=$(dirname `which $0`)
export ROBOTOUT="${SCRIPT_PATH}/../../results"
export ROBOT_SYSLOG_FILE="${ROBOTOUT}/syslog.txt"
rm -r $ROBOTOUT
mkdir $ROBOTOUT
robot --pythonpath ../../src --outputdir $ROBOTOUT --xunit ./junit.xml --listener robotkeywords.AnnotationsListener ../../internetsite/tests