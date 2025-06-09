# python
![Avatar](https://github.com/dgucc/sandbox/blob/main/tips/images/avatar.gif)  
## Webscraping with python + export in csv format

[Sample](https://github.com/dgucc/python/blob/main/webscrap/webscrap.py)

## Pre-requesites
```bash
$ python3 -m pip install --upgrade pip
$ pip install requests  
$ pip install beautifulsoup4  
```
## Execute it
`$ python3 webscrap.py` 
&rarr; themes.csv  

## Webpage : load csv into html table + add filter with jquery

[Webpage as demo](https://github.com/dgucc/python/blob/main/webscrap/index.html)  

## Tips

### Working with Virtual Environments  

1. Create a virtual environment  
`$ python3 -m venv sandbox-env`  

2. Activate it  
`$ source sandbox-env/bin/activate`  


Python Environments  

Using Python environments allows you to work with multiple Python versions  
without altering the system default version. I’ve tested this approach with both pip3 and pipenv.

Using virtualenv  

01. Install pip3 (if not already installed):  
```bash
sudo apt update
sudo apt install python3-pip
```

02. Install virtualenv:  
```bash
pip3 install virtualenv
```

03. Install your desired Python version (e.g., Python 3.8):  
```bash
sudo apt install python3.8
```

04. Create an environment with the desired Python version:  
> python3.8 -m virtualenv -p python3.8 <YOUR_ENVIRONMENT_NAME>  

For example, if your environment name is env, the command will be:  
> python3.8 -m virtualenv -p python3.8 env  


05. Activate the environment:  

```bash
cd env
source bin/activate
```

06. Test the Python version:  

After activating the environment, run:

`python --version` 

You should see the output as Python 3.8.


### Use filter to find object in a list based on attribute value  
`obj = list(filter(lambda x: x['id']==id, listOfObjects))[0]`
