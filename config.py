from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.ui import Select

def get_driver():
    # initialize options
    options = webdriver.ChromeOptions()
    # pass in headless argument to options
    options.add_argument('--headless')
    # initialize driver
    driver = webdriver.Remote(
                command_executor='http://172.20.0.2:4444/wd/hub',
                desired_capabilities=DesiredCapabilities.CHROME)
    return driver


def to_es(self,url,index_name,username,password,nom,df):
        INDEX_NAME= index_name   
        URL= url  
        ELASTIC_ID= username 
        ELASTIC_PSSWD= password 
        df['nom']= nom 
        
        es_client = Elasticsearch([URL], http_auth=(ELASTIC_ID,ELASTIC_PSSWD ))
        df_iter = df.iterrows()
        result = []
        for index, document in df_iter:
            res = es_client.index(index=INDEX_NAME, id=index, body=document.to_dict())
            result.append(res['result'])
            
        return result