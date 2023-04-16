# python

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


### Use filter to find object in a list based on attribute value  
`obj = list(filter(lambda x: x['id']==id, listOfObjects))[0]`
