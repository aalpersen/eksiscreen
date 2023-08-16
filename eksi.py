import io
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import argparse
import configparser


def raw_string(string):
    return fr"{string}"


def main():


    # process config.ini
    config_object = configparser.ConfigParser
    with open("config.ini", "r") as file_object:
        config_file = file_object.read()

    config_object = configparser.RawConfigParser(allow_no_value=True)
    config_object.read_file(io.StringIO(config_file))
    driver_p = config_object.get("selenium", "driver_path")
    binary_p = config_object.get("selenium", "binary_path")
    print("config.ini, driver_path: ", driver_p)
    print("config.ini, binary_path: ", binary_p)
    # end of processing config.ini

    # parse arguments
    parser = argparse.ArgumentParser(description="Processes Ekşisözlük and saves screenshots of given url")
    parser.add_argument("-u", "--url", nargs=1, required=True, help="Taranacak URL adresi")
    parser.add_argument("-i", "--interval", nargs=1, required=True, help="Hangi aralıklarla taranacak, dk olarak")
    parser.add_argument("-r", "--runnumber", nargs=1, required=True, help="Kaç kere taranacak")
    args = parser.parse_args()
    defaulturl = args.url[0]
    intervalminutes = args.interval[0]
    runnumber = args.runnumber[0]
    # end of parsing arguments
    print("Url:", defaulturl)
    print("Run Number:", runnumber)
    print("Interval:", intervalminutes)

    # driver_path = r'C:\Selenium\geckodriver.exe'
    # binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

    driver_path = str(fr"{driver_p}")
    binary_path = str(fr"{binary_p}")

    options = webdriver.FirefoxOptions()
    options.binary_location = binary_path
    driver = webdriver.Firefox(executable_path=driver_path, options=options)
    # options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    # driver = webdriver.Firefox(executable_path=r"C:\selenium\geckodriver.exe", options=options)

    # options.binary_location = os.path.join(binary_p)
    # ffprofile = FirefoxProfile(r'C:\FirefoxProfil\selenium')
    # options = Options()
    # firefox_profile = FirefoxProfile(profile_directory=ffprofile)
    # firefox_profile.set_preference()
    # options.profile(ffprofile)
    # firefox_profile.path(ffprofile)
    # options.set_preference('profile', ffprofile)
    # options.binary_location(binary_path)
    # service = Service(driver_path)

    firstpage = defaulturl
    print("Getting page: ", firstpage)
    startpage = 1
    allpages = []
    allpages.append(firstpage)
    runno = 0
    driver.get(firstpage)
    mainpage = driver.find_element(By.CLASS_NAME, "pager")
    gen = mainpage.find_elements(By.CLASS_NAME, "last")
    lastpage = int(gen[-1].text)
    print("last page: ", lastpage)
    while runno < int(runnumber):
        print("Running for iteration: ", str(runno))
        allpages = []
        allpages.append(firstpage)
        simdi = datetime.now()
        mevcutklasor = os.getcwd()
        kayitklasor = mevcutklasor + "\\" + str(simdi.hour) + "-" + str(simdi.minute) + "-" + str(int(runno)) + "\\"
        os.mkdir(str(simdi.hour) + "-" + str(simdi.minute) + "-" + str(int(runno)))
        while startpage < lastpage:
            page = defaulturl + "?p=" + str(startpage + 1)
            startpage = startpage + 1
            print("page: ", page)
            print("startpage: ", startpage)
            allpages.append(page)
        screenshotnumber = 0
        for page in allpages:
            print("Getting page: ", page)
            driver.get(page)
            time.sleep(10)
            element = driver.find_element(By.ID, "topic")
            screenshotname = "screenshot" + str(screenshotnumber) + ".png"
            element.screenshot(kayitklasor + screenshotname)
            print("Saving screenshot: ", kayitklasor + screenshotname)
            screenshotnumber = screenshotnumber + 1
        runno = runno + 1
        print("Sleeping for: ", str(int(intervalminutes) * 60))
        time.sleep(int(intervalminutes) * 60)

    driver.quit()


if __name__ == "__main__":
    main()
