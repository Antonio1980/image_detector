CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Location
 * Configuration
 * Enable PyTest for the project
 * Technologies, CV tools/ libraries
 * Recommended plugins
 * Requirements
 * Tests
 * Configuration
 * Troubleshooting
 * Maintainers

INTRODUCTION
------------

The ""

LOCATION
---------

- HTTPS: https://github.com/Antonio1980/image_detector.git

---------------------------------------------------------------

CONFIGURATION
-------------

ENABLE PyTest FOR PROJECT
-------------------------

- Open the Settings/Preferences | Tools | Python Integrated Tools settings dialog as described in Choosing Your Testing Framework.
- In the Default test runner field select pytest.
- Click OK to save the settings.

TECHNOLOGIES, TOOLS/LIBRARIES
----------------------------------------------
- PyTest - advanced test framework.
- Luminoth - open source toolkit for computer vision.
- TensorFlow - open source library for ML models. 
- Pandas - a library for data manipulation and analysis
- NumPy - a library for adding support for large, multi-dimensional arrays and matrices, 
along with a large collection of high-level mathematical functions to operate on these arrays
- Matplotlib
- Opencv
- redis - access to Redis DB.
- PyMySQL - access to SQL DB.
- allure-pytest - reporting.
- beautifulsoup4 - work with HTML.


RECOMMENDED PLUGINS
-------------------
- bashsupport - ability to execute shell/bash scripts.
- multirun - ability to run several configurations.
- .gitignore - prevents redundant uploads.
- GitLab - projects integration with remote repo and VCS.
- CSV - plugin to support csv files.
- Docker - for docker integration.
- CMD support.


REQUIREMENTS
------------

1. PyCharm IDEA installed.
2. Python 3.5 - 3.7 or later installed.
3. Python virtualenvironment installed out of the project and activated.
4. Python interpreter configured.
5. Project requirements installed.
6. Project plugins installed.


TESTS
-----

1 Run all tests:
* $ pytest -v tests/ --alluredir=src/repository/allure_results

2 Run tests as a package:
* $ pytest -v tests/path to package_tests --alluredir=data_source/repository/allure_results

3 Run specific test:
* $ pytest -v tests/'path to package_test/path to test' --alluredir=src/repository/allure_results

4 Run specific group 
* $ pytest -v tests/ -m smoke --alluredir=src/repository/allure_results

4 Generate temporary allure report:
* $ allure serve src/repository/allure_results
  
5 Generate report:
* $ allure generate src/repository/allure_results -o src/repository/allure_report --clean
  
6 Open allure report:
* $ allure open src/repository/allure_report

7 Show pytest fixtures and execution plan:
* $ pytest --collect-only


* Test Groups:

1. smoke - Smoke tests group


Python Installation:  
--------------------
https://www.python.org/downloads/windows/


* install pip:
$ python get-pip.py

* install virtual environment:
$ pip install virtualenv

* create virtual environment:
$ virtualenv venv --python=python3.7

* activate environment for Windows:
$ venv\Scripts\activate

* activate environment for Unix:
$ source venv/bin/activate

* list all packages installed in the environment:
$ pip freeze

* upgrade pip:  
$ python -m pip install --upgrade pip



MAINTAINERS
-----------

* Anton Shipulin <antishipul@gmail.com>
