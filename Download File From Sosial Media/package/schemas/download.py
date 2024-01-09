from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class MediaDownloader():
    def __init__(self, url):
        self.url = url
        self.driver = self.driver_init()
        
    def driver_init(self):
        chrome_path = ChromeDriverManager().install()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        
        service = Service(executable_path=chrome_path)
        driver = webdriver.Chrome(service=service, options=options) #, options=options
        
        return driver
        
    def scraping_data(self):
        self.driver.get('https://savefrom.net/')
        
        sleep(1)
        self.driver.find_element(By.NAME, 'sf_url').send_keys(self.url)
        self.driver.find_element(By.NAME, "sf_submit").click()

        try:
            ele = WebDriverWait(self.driver, 15).until( #using explicit wait for 10 seconds
                EC.presence_of_element_located((By.XPATH, "//*[@id='sf_result']/div/div[1]/div[2]/div[2]")) #checking for the element with 'h2'as its CSS
            )
            
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
        except:
            soup = None
            print("Timeout Exception: Page did not load within 10 seconds.")
        finally:
            self.driver.close()
            return soup
        
    
    def json(self):
        soup = self.scraping_data()
        
        if soup is not None:
            
            metas = soup.find_all("div", {"class": "info-box"})
            
            full_dict = []  # Create an empty list

            for meta in metas:
                url= meta.find('a').get("href") if meta is not None else ''
                title = meta.find("div", {"class": "row title"}).get_text() if meta is not None else ''
                type = meta.find('a').get_text() if meta is not None else ''
                if type != 'Download':
                    type = type.split(" ")[2]
                elif type == 'Download':
                    type = 'MP4'
                
                my_dict = {
                    "title": title,
                    "type": type,
                    "url": url
                }  # Create a dictionary

                full_dict.append(my_dict)  # Append the dictionary to the list
                
            
            return full_dict
        