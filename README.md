# python

## Webscraping with python + export in csv format

[Sample](https://github.com/dgucc/python/blob/main/webscrap.py)

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

[Webpage as demo](https://github.com/dgucc/python/blob/main/index.html)  

## Tips

Use filter to find object in a list based on attribute value  
`obj = list(filter(lambda x: x['id']==id, listOfObjects))[0]`
