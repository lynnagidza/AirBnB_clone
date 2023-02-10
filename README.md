# AirBnB clone - The console
## Project Description
This project is the first part of building a full web application: the AirBnB clone.
## Command Interpreter
The console is a Unix shell-like command line user interface provided by the python [CmdModule](https://wiki.python.org/moin/CmdModule)
It prints a prompt and waits for the user for input.
Command | Example
------- | -------
Display commands help | ```(hbnb) help <command>```
Create object (prints its id)| ```(hbnb) create <class>```
Destroy object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Show "all" objects or instances class | ```(hbnb) all``` or ```(hbnb) all <class>```
Run console | ```./console.py```
Quit console | ```(hbnb) quit```


Help command example

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```
### Learning Objectives
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function