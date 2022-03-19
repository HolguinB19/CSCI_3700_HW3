Homework 3
Bryan Holguin Herrera

THE FOLLOWING IS FOR WINDOWS 10. ASSUMING YOU ARE USING THE CMD PROMPT. NOT LINUX OR UNIX

## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
pip install python3-venv
```

Create a virtual environment:
```
py -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/Scripts/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
py app.py
```

Or you can use the command:
```
flask run
```
and it will automatically run, by locating app.py and executing it for you. 