# Virtualenv

## Installing virtualenv

virtualenv is used to manage Python packages for different projects.
Using virtualenv allows you to avoid installing Python packages globally
which could break system tools or other projects. You can install virtualenv
using pip.

On Linux:

~~~bash
python3 -m pip install --user virtualenv
~~~

## Creating a virtual environment

venv (for Python 3) allow you to manage separate package installations for different projects. They essentially allow you to create a “virtual” isolated Python installation and install packages into that virtual installation. When you switch projects, you can simply create a new virtual environment and not have to worry about breaking the packages installed in the other environments. It is always recommended to use a virtual environment while developing Python applications.

On Linux:

~~~bash
python3 -m venv env
~~~

## Activating a virtual environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

On Linux:

~~~bash
source env/bin/activate
~~~

## Leaving the virtual environment

If you want to switch projects or otherwise leave your virtual environment, simply run:

~~~bash
deactivate
~~~

## Installing packages using requirements files

For example you could create a requirements.txt file containing:

~~~bash
fastapi
uvicorn
~~~

And tell pip to install all of the packages in this file using the -r flag:

~~~bash
pip install -r requirements.txt
~~~

## Freezing dependencies

Pip can export a list of all installed packages and their versions using the freeze command:

~~~bash
pip freeze
~~~
