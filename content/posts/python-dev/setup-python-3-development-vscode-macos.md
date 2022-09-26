--- 
title: "\U0001f4bb Python3 Development on VS Code for MacOS \U0001f40d \U0001f469\u200D\U0001f4bb \U0001f34f" 
date: 2021-04-11T11:00:00+02:00 
draft: false 
tags: ["tech", "python", "macos", "development"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/python-3-code-1200x630.jpg" # image path/url
    alt: "The Python3 language logo over some Python code" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

A quick how-to guide to installing Python3 tooling for Microsoft VS Code on MacOS.

<!--more-->

## Install Python3 on MacOS

Let's keep this nice and easy, use the official `python.org` installer, choose whomever is most stable for the smoothest experience: [download python3 for macos](https://www.python.org/downloads/macos/)

## Installing VS Code on MacOS

Let's get started by installing VS Code on MacOS. For the installation:

- Download Visual Studio Code for macOS [Download link](https://go.microsoft.com/fwlink/?LinkID=534106)
- Open the browser's download list and locate the downloaded archive.
- Extract the archive contents. Use double-click for some browsers or select the 'magnifying glass' icon with Safari.
- Drag 'Visual Studio Code.app' to the Applications folder, making it available in the MacOS Launchpad.
- Add VS Code to your Dock by right-clicking on the icon to bring up the context menu and choosing Options, Keep in Dock.

### Command Line Launcher

- Launch VS Code.
- Open the Cmd Palette (`Cmd+Shift+P`) and type `shell command` to find the **Shell Command: Install 'code' command in PATH** command.

![VS Code on MacOS: Shell Command from Command Palette](/post-img/vscode-macos-shell-command.jpg)

- Select the option, provide the admin password.
- Restart the terminal for the new `$PATH` value to take effect. 
- You'll be able to type `code .` in any folder to start editing files in that folder.

## Install Python extensions

- Open the extensions manager
- Install the Python extension for VS Code from the Visual Studio Marketplace. The Python extension is named Python and it's published by Microsoft. It is shown below:

![Example image](/post-img/install-python-vscode-extension-1200x630.jpg)

- Next, check that the `python3` interpreter is available on the command line by typing:

```bash
$ python3 --version
Python 3.9.10
```

- There will be a button on the post install configuration called: **Select Python Interpreter**. It is very important to select the Python3 interpreter from here.
- Test that you can run a Python script by creating a new file, and hitting run. Try this one:

```python
import subprocess
cmd = [
    "/sbin/ifconfig", 
    "-g"]
p = subprocess.Popen(
    cmd, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)
stdoutdata, stderrdata = p.communicate()

output = stdoutdata.decode()
if output:
    print(output)
else:
    print("ERROR!!!\n", stderrdata.decode())
```

The quick witted will have noted that there is not a `-g` option for `/ifconfig`, we should swap that to `-a` to get it to run nicely!

## Debugging

Debugging Python is as straight forward as: 

- Select the Debugger icon from the menu (icon: triangle with a bug!)
- Add a breakpoint (click the red dot next to the line numbers)
- Then selecting **Run and Debug** from the menu
- The usual step over, step into, options are available, and all the variables should be visible from the debugger menu

## `pip` and `venv` 

These two standard tools can be installed on MacOS easily. First, make sure your `pip` is up to date. This involves the usual whac-a-mole with Python3 on MacOS:

```bash
$ pip3 --version
pip 21.2.4 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)

$ python3 -m pip install --upgrade pip
Requirement already satisfied: pip in /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages (21.2.4)
Collecting pip
  Using cached pip-22.0.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
  WARNING: The scripts pip, pip3 and pip3.9 are installed in '/Library/Frameworks/Python.framework/Versions/3.9/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-22.0.2

$ echo 'PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin:$PATH' >> ~/.bashrc
$ bash

$ python3 --version
Python 3.9.10

$ pip3 --version
pip 22.0.2 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)

$ pip --version
pip 22.0.2 from /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip (python 3.9)
```

And now we have access to `venv` for Python3, we don't need to install anything since it is part of the standard library since Python v3.3

```bash
$ python3 -m venv env

$ source env/bin/activate
(env) ...

$ which python3
/Users/dave/code/pygui/env/bin/python3

$ which python
/Users/dave/code/pygui/env/bin/python

$ python --version
Python 3.9.10

$ deactivate
```

For more info on `pip` and `venv` check out the [official documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) 
