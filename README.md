# GitRepo

Bash/python script to automate the process of git/github initialization.
Uses selenium to access github, and do all the repetitive steps of creating the repo for you.


This script will:

	* Create a new github repository with a name of your choice
	* runs 'git init' (if no .git is found)
	* create a blank README.md (if none is found)
	* remote attach git to the newly created github repo
	* pushes an initial commit to github
	* return a link to the repo on your clipboard


Usage
----
```
gitrepo [repositoryName]
```
repositoryName is optional.  Default will be the name of the current working directory.
if a name is provided, the new repo will be created inside your current working directory.


Setup
----
* you will need to replace some of the information inside gitrepo.py and gitrepo
	* you can either hard code in your username and password for conveinence, or keep it as is for security.
	* put the gitrepo bash script anywhere in your PATH.  You can rename this whatever you want.
	* inside the gitrepo bash script, change path to python interpreter, and gitrepo.py
	

Requirements
----
	* [Selenium](https://pypi.org/project/selenium/)
	* [Chrome (or browser of choice)](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en)
	* [chromedriver (or driver of choice)](https://chromedriver.chromium.org/downloads)
	* [clipboard](https://pypi.org/project/clipboard/)

