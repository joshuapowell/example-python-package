# Example Package Installer
This application is an example of a Python package capable of being installed via `pip`.

## Getting Started

It is recommended to run this application within a `virtualenv` virtual 
environment.

### Run the Application

To run the package from within your virtual environment, you can either
start it in `editable` mode or you can simple install it.

#### Editable
To run the package under Editable, open your Command Line Interface and
execute the following command from the project root directory:

```
pip install --editable .
```

#### Install Package
To install the package within another application, open your Command Line
Interface and execute the following command:

```
pip install endor
```

##### Warning
This should display a message like the following:

```
Collecting endor
  Could not find a version that satisfies the requirement endor (from versions: )
  No matching distribution found for endor
```

The reason this happens is because this example package has not been
submitted to the Python Package Index for public consumption.

Alternately you will need to install your example Python package from 
a valid URL. For example, if you wish to install the package that you
have hosted on Github.com, you would execute the following command:

```
pip install git+git://github.com/joshuapowell/example-python-package/
```

## Documentation for Creating Packages
- [Official Python Packaging User Guide](https://packaging.python.org/)
- [Flask Package Tutorial](http://flask.pocoo.org/docs/0.12/tutorial/packaging/)
