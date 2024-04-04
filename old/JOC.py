import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import json


def JOC ():
    # Define the start and end years
    #start_decade = 1980
    #end_decade = 2000

    # Randomly select a decade
    #random_decade = random.randint(start_decade // 10, end_decade // 10) * 10

    # Randomly select a year within the chosen decade
    #random_year = random.randint(random_decade, random_decade + 9)
    
    year = 1980
    joc = {1980 : [],
           1981 : [],
           1982 : [],
           1983 : []}

    while year < 1982:

    #Vol = random_year - 1935
        Vol = year - 1935

        Issue_Dic = {1980: 26,
                    1981: 26,
                    1982: 27,
                    1983: 26,
                    1984: 26,
                    1985: 26,
                    1986: 26,
                    1987: 26,
                    1988: 26,
                    1989: 26,
                    1990: 26,
                    1991: 26,
                    1992: 26,
                    1993: 27,
                    1994: 26,
                    1995: 26,
                    1996: 26,
                    1997: 26,
                    1998: 26,
                    1999: 26,
                    2000: 26,
                    2001: 26,
                    2002: 26,
                    2003: 26,
                    2004: 26,
                    2005: 26,
                    2006: 26,
                    2007: 26,
                    2008: 24,
                    2009: 24}
    
        #Issue = Issue_Dic[random_year]
        Issue = Issue_Dic[year]

        while Issue > 0:

            #print (f'Year = {random_year}, Volume = {Vol}, Issue = {Issue}')

            url = f'https://pubs.acs.org/toc/joceah/{Vol}/{Issue}'
            #print(f"{url}")
            firefox_driver_path = "/var/www/html/RandomJournalGenerator/geckodriver"
            options = webdriver.FirefoxOptions();
            options.headless = True
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
            driver = webdriver.Firefox(executable_path=firefox_driver_path, options=options)
            driver.get(url)
       
            elem = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "design-studio-animate")))

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a')
            
            doi = []
            for link in links:
                current_link = link.get('href')
                if f'{current_link}'.startswith('/doi/abs'):
                    updated_doi = current_link.replace("/doi/abs", "https://doi.org")
                    doi.append(updated_doi)
            joc[year].extend(doi)
            print(f'{joc}')
            driver.close()
            
              
            #print(f'https://pubs.acs.org{selected_paper}')
            Issue = Issue - 1
        year = year + 1
    Json = (json.dumps(joc))
    print(f'{Json}')
    with open('joc_doi.json', 'w') as fp:
        json.dump(Json, fp)