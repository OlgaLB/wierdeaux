#!/usr/bin/env python3

# for ability to send HTTP requests
import requests
# for pulling data out of HTML file
from bs4 import BeautifulSoup
# for working with page source
import selenium
from selenium.webdriver.firefox.options import Options
# for exiting in case of exception
import sys


if __name__ == "__main__":
    # exception handling if the web site is not reachable
    try:
        response = requests.get("http://www.weerindelft.nl/")
    except:
        print("Web page cannot be reached")
        sys.exit(1)

    # by inspecting the element with the current temperature, a path was found as: 
    # html>body>div>div>iframe#ifrm_3>html>body>div>div.ajaxDashboard>table>tbody>tr>td>table>tbody>tr>td.data1>span#ajaxtemp.ajax

    # the outer html of the element was found as:
    # <span class="ajax" id="ajaxtemp" style="font-size: 20px;" lastobs="6.8&amp;deg;C">6.8°C</span>

    options = Options()
    options.headless = True
    driver = selenium.webdriver.Firefox(executable_path = '/work/geckodriver', options = options)

    soup = BeautifulSoup(response.content, 'html.parser')

    driver.get(soup.find("iframe", attrs = {'id':'ifrm_3'})["src"])
    soup = BeautifulSoup(driver.page_source,'html.parser')
    temperature = soup.find("span", attrs = {'id':'ajaxtemp'}).text

    print("Current temperature in Delft in Celcius degrees is: " + temperature)
