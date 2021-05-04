# GitRepo


What Is It?
----
Python to automate the process of git repo and github initialization.

Uses selenium to access github, do all the repetitive steps of creating the repo for you, and initialized the local repo if necessary.


This command will:

* Create a new github repository with a name of your choice.
* runs 'git init' (if no .git is found).
* create a blank README.md (if none is found).
* remote attach git to the newly created github repo.
* pushes an initial commit to github.
* return a link to the repo on your clipboard.


Usage
----
```
gitrepo [repositoryName]
```

repositoryName is optional.  Default will be the name of the current working directory.
if a name is provided, a new repo with that name will be created inside your current working directory.


Setup
----
to install, run the following:
```
git clone https://github.com/AnthonyPerugini/gitrepo
chmod -x install.sh
./install.sh
```

* You will need to replace some of the information inside gitrepo.py

	* Inside gitrepo.py
		* You can either hard code in your username and password for conveinence, or keep it as is for security.

Requirements
----
see requirements.txt

[Selenium](https://pypi.org/project/selenium/)

[Chrome or browser of choice](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en)

[chromedriver or driver of choice](https://chromedriver.chromium.org/downloads)

[clipboard](https://pypi.org/project/clipboard/)

> many people make the mistake of saving money by wasting time.
> 
> -J.R. Rim
> 
