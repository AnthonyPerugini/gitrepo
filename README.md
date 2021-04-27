# GitRepo

Bash/python script to automate the process of git/github initialization.

This script will:

	* Create a new github repository with a name of your choice
	* run a git init (if no .git is found)
	* create a blank README.md (if none is found)
	* remote attach git to the newly created github repo
	* push an initial commit
	* return a link to the repo on your clipboard


Usage
----

```
gitrepo [repository_name]
```
* repository_name is optional.  Default will be the name of the current working directory.

How It Works
----
* you will need to replace some of the information inside gitrepo.py
	* you can either hard code in your username and password, or keep it as is
	* TODO: finish setup

Requirements:
----
	* [Selenium](https://pypi.org/project/selenium/)
	* [Chrome (or browser of choice)](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en)
	* [chromedriver (or driver of choice)](https://chromedriver.chromium.org/downloads)

