# GitRepo


What Is It?
----
Python to automate the process of git repo and github initialization.

Uses selenium to access github, do all the repetitive steps of creating the repo for you, and initialized the local repo if necessary.


This command will:

* Create a new github repository with the name of your choice.
* runs 'git init' if no .git is found.
* creates a blank README if none is found.
* remote attach local git to the newly created github repo
* pushes an initial commit to github
* return a link to the repo on your clipboard


Usage
----
Add 'gitrepo' to your ~/usr/bin/~ folder and use like any script command.

```
gitrepo [repositoryName]
```

repositoryName is optional.  Default will be the name of the current working directory.
if a name is provided, a new repo with that name will be created inside your current working directory.


Setup
----
* Put the gitrepo bash script anywhere in your PATH ~/usr/bin/~ default.  You can rename this whatever you want.
* You will need to replace some of the information inside gitrepo.py and gitrepo

	* Inside gitrepo.py
		* You can either hard code in your username and password for conveinence, or keep it as is for security.
	* Inside gitrepo
		* Change path to python interpreter, and gitrepo.py

Requirements
----
see requirements.txt

[Selenium](https://pypi.org/project/selenium/)

[Chrome or browser of choice](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en)

[chromedriver or driver of choice](https://chromedriver.chromium.org/downloads)

[clipboard](https://pypi.org/project/clipboard/)

And with that, ill leave you with some words of wisdom.
> many people make the mistake of saving money by wasting time.
> 
> -J.R. Rim
> 
