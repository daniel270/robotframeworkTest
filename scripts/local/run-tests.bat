echo "Creating results directory"
cd %~dp0/../..
rd results /s /q
mkdir results
cd %~dp0
SET ROBOTOUT=%~dp0/../../results
echo "Running test cases"
robot --pythonpath ../../src --outputdir %ROBOTOUT% --xunit ./junit.xml --listener robotkeywords.AnnotationsListener %~dp0/../../internetsite/tests
taskkill /F /IM chromedriver.exe 2>nul