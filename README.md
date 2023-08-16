Ekşi Sözlük Screenshot grabber

A utility that captures and stores screenshots for specified eksisozluk url for given intervals for given run numbers

You may install required packages (Selenium) by executing:

`$ pip3 install -r requirements.txt`

For Windows and other OSes download geckodriver for Firefox at:
https://github.com/mozilla/geckodriver/releases

Edit binary_path and driver_path in config.ini

### Default variables in config.ini:

```
driver_path = C:\Selenium\geckodriver.exe
binary_path = C:\Program Files\Mozilla Firefox\firefox.exe
```

### Usage:
`$ eksi.py -u <urltothread> -i <intervalnumber> -r <runnumber>`