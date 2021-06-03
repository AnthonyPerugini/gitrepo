# GitRepo

> many people make the mistake of saving money by wasting time.
> 
> -J.R. Rim
> 
Wow, now that you're feeling super inspired, check out Gitrepo

What Is It?
----
Python to automate the process of git repo and github initialization.

Uses selenium to access github, and complete all the repetitive steps for you.


This command will:

* creates a new github repository with a name of your choice (defaults to cwd name).
* runs 'git init' (if no .git file is found).
* creates a blank README.md (if none is found).
* remote attaches git to the newly created github repo.
* pushes an initial commit to github.
* returns a link to the repo on your clipboard.


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
chmod +x install.sh
./install.sh
```

* You may need to replace some of the information inside gitrepo.py

	* Inside gitrepo.py
		* You can either hard code in your username and password for conveinence, or keep it as is for security.
		* Change the options.binary_location if your google-chrome installation path is different

Requirements
----
see requirements.txt
everything will be installed automatically with install.sh

You may want to change google-chrome and chromedriver to match the browser of your choice.

[Selenium](https://pypi.org/project/selenium/)

[Chrome or browser of choice](https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=en)

[chromedriver or driver of choice](https://chromedriver.chromium.org/downloads)

[clipboard](https://pypi.org/project/clipboard/)

