# AirBnB clone concepts
## The console
### TO DOs
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
### Description
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

## Web static
- learn HTML/CSS
- create the HTML of your application
- create template of each object

## MySQL storage
- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.

## Web framework - templating
- create your first web server in Python
- make your static HTML file dynamic by using objects stored in a file or database

## RESTful API
- expose all your objects stored via a JSON web interface
- manipulate your objects via a RESTful API

## Web dynamic
- learn JQuery
- load objects from the client side by using your own RESTful API

# AirBnB clone Files and Directories
- [models](https://github.com/lynnagidza/AirBnB_clone/tree/main/models) directory contains all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- [tests](https://github.com/lynnagidza/AirBnB_clone/tree/main/tests) directory contains all unit tests.
- [console.py]() file is the entry point of our command interpreter.
- [base_model.py](https://github.com/lynnagidza/AirBnB_clone/blob/main/models/base_model.py) file is the base class of all our models. It contains common elements: attributes: id, created_at and updated_at & methods: save() and to_json()
- engine]() directory contains all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.
