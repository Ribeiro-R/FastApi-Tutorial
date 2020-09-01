<h1>Installing virtualenv</h1>

<p>virtualenv is used to manage Python packages for different projects.
Using virtualenv allows you to avoid installing Python packages globally
which could break system tools or other projects. You can install virtualenv
using pip.</p>

<p>On Linux:</p>

```
$ python3 -m pip install --user virtualenv
```

<h1>Creating a virtual environment</h1>
<p>venv (for Python 3) allow you to manage separate package installations for different projects. They essentially allow you to create a “virtual” isolated Python installation and install packages into that virtual installation. When you switch projects, you can simply create a new virtual environment and not have to worry about breaking the packages installed in the other environments. It is always recommended to use a virtual environment while developing Python applications.</p>

<p>On Linux:</p>

```
$ python3 -m venv env
```

<h1>Activating a virtual environment</h1>

<p>Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.</p>

<p>On Linux:</p>

```
$ source env/bin/activate
```


<h1>Leaving the virtual environment</h1>

<p>If you want to switch projects or otherwise leave your virtual environment, simply run:</p>

```
$ deactivate
```

<h1>Installing packages using requirements files</h1>

<p>For example you could create a requirements.txt file containing:</p>

```
fastapi
uvicorn
```
<p>And tell pip to install all of the packages in this file using the -r flag:</p>

```
$ pip install -r requirements.txt
```

<h1>Freezing dependencies</h1>

<p>Pip can export a list of all installed packages and their versions using the freeze command:</p>

```
$ pip freeze
```
