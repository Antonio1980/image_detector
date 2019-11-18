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

The "GM_test"- is a first overview and base for home exam.

LOCATION
---------

- SSH: git@gitlab.com:rizvash/gm.git
- HTTPS: https://gitlab.com/rizvash/gm_cv.git

-------The home assigment folder: 'venv_examples_test'---------
---------------------------------------------------------------

CONFIGURATION
-------------

The ctructure of the framevork will be separeted on two domaine zone:
1) Global scope  
2) Virtual Env Scopes:
 - venv_luminoth: playground for open source Computer Vision toolkit https://luminoth.ai/
 - venv_pg_image_ai: playground for ImageAI is a python Computer Vision library https://imageai.readthedocs.io/en/latest/
 - venv_test: playground for a home assignment
 
For activate virtual env: run in terminal `actvate` 
file must be used with "source bin/activate" *from bash*

** each of the virtual environments contains its own list of dependencies specified 
in the "requirements.txt" file.

**How to change activate System Interpreter/venv:
File -> Settings ->  Project <project name> -> Project Interpreter
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html 

* To install all dependencies run command (for chosen env):
* $ pip3 install -r requirements.txt


ENABLE PyTest FOR PROJECT
-------------------------

- Open the Settings/Preferences | Tools | Python Integrated Tools settings dialog as described in Choosing Your Testing Framework.
- In the Default test runner field select pytest.
- Click OK to save the settings.

TECHNOLOGIES, COMPUTER VISISON TOOLS/LIBRARIES
----------------------------------------------
https://hub.packtpub.com/top-10-computer-vision-tools/

- PyTest - advanced test framework.
- Luminoth - open source toolkit for computer vision.
- TensorFlow - open source library for ML models. 
- Pandas - a library for data manipulation and analysis
- NumPy - a library for adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
- Matplotlib
- Opencv

- Google Cloud and Mobile Vision 
- Amazon Rekognition
- Microsoft Azure Computer Vision

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
* $ pytest -v tests/GM --alluredir=src/repository/allure_results

2 Run tests as a package:
* $ pytest -v tests/GM/path to package_tests --alluredir=data_source/repository/allure_results

3 Run specific test:
* $ pytest -v tests/'path to package_test/test' --alluredir=src/repository/allure_results

4 Generate temporary allure report:
* $ allure.bat serve src/repository/allure_results
  
5 Generate report:
* $ allure.bat generate src/repository/allure_results -o src/repository/allure_report --clean
  
6 Open allure report:
* $ allure.bat open src/repository/allure_report

7 Show pytest fixtures and execution plan:
* $ pytest --collect-only


* Test Groups:

1. smoke - 
2. ui - 
3. accuracy - 
4. sensor data validation 
5. e2e - end to end tests
6. tests related to DBs
7. services
8. perfomance 
9. integration
10. negative 
11. public_api
12. regression 
13.
14.

TROUBLESHOOTING
---------------

Docker / Solving Network conflict:
-----------------------------------
* If your docker build fails such as:
"ERROR: cannot create network",
(br-c868a505e7d9): "conflicts with network",
(br-992ca1654879): "networks have overlapping IPv4"

* Look on docker network processes:
$ docker network ls

* Find from returned list conflicted ID:
NETWORK ID          NAME                        DRIVER              SCOPE
10060c77e51a        bridge                      bridge              local
992ca1654879        crm_bo-master_crm-network   bridge              local
82c2f8dcfa10        host                        host                local
64d5c2636300        none                        null                local

* Remove by ID:
$ docker network rm

Kafka:
------
1 Installation guide:

https://kafka.apache.org/quickstart

https://medium.com/@shaaslam/installing-apache-kafka-on-windows-495f6f2fd3c8


Git Configuration:
------------------
* $ git init

* $ git status

* $ git config --global --list

* $ git config --global user.name ""

* $ git config --global user.email ""

* $ cat ~/.gitconfig

* $ git config --global help.autocorrect 1

* $ git config core.autorlf true/false


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

* Rizvash Iliya <rizvash.i@gmail.com>
