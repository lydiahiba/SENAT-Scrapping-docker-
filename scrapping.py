from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import numpy as np
import time
import datetime
import numpy as np
import pandas as pd
import locale
import re 
from elasticsearch import Elasticsearch

class ScrappingSena():
    def __init__(self,link,config):
        self.link=link
        self.browser = config.get_driver()
        
    def get_press_release_links_by_page(self):
    
        #browser = webdriver.Chrome(options=chrome_options)
        self.browser.get(self.link)
        link = self.browser.find_elements_by_css_selector('li .link')

        current_date= datetime.date.today().strftime('%d-%m-%Y')

        self.links=[]

        for i in link :
            self.links.append(i.get_attribute('href'))

        self.browser.close()
        self.browser.quit()
        df=pd.DataFrame(self.links,columns=['url'])
        df['date']=current_date
        df.to_csv("PressRelease.csv")
        self.df = df
        return df
    
    
    def get_acronymes(self):
        self.acronymes=[]
        i = 0
        #browser = webdriver.Chrome(options=chrome_options)
        for link in self.links:
            i+=1
            print(i)
            self.browser.get(link)
            text=browser.find_element_by_xpath('//*[@id="CP"]').text
            time.sleep(1)
            regex=re.findall(r'[A-Z]{2,}',text)
            if regex!=None:
                self.acronymes.extend(regex)
        self.browser.close()
        self.browser.quit()        
        return self.acronymes

            
    def to_es(self,url,index_name,username,password,nom):
        INDEX_NAME= index_name   
        URL= url  
        ELASTIC_ID= username 
        ELASTIC_PSSWD= password 
        self.df['nom']= nom 
        
        es_client = Elasticsearch([URL], http_auth=(ELASTIC_ID,ELASTIC_PSSWD ))
        df_iter = self.df.iterrows()
        result = []
        for index, document in df_iter:
            res = es_client.index(index=INDEX_NAME, id=index, body=document.to_dict())
            result.append(res['result'])
            
        return result