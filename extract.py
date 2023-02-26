import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_list(resulta):
        list_link_job=[]  ,list_title_jobs=[],  list_company_location=[],  list_company_name=[]
        soup = BeautifulSoup(resulta, "lxml")
        list_li = soup.findAll("div", {"class": "slider_item css-kyg8or eu4oa1w0"})
        for i in range(len(list_li)):
                link_job = "https://ma.indeed.com" + \
                           list_li[i].find("div", {"class": "css-1m4cuuf e37uo190"}).find("a")["href"]
                print(link_job)
                list_link_job.append(link_job)
                title = list_li[i].find("div", {"class": "css-1m4cuuf e37uo190"}).find("a").text
                list_title_jobs.append(title)
                comany_location = list_li[i].find("div", {"class": "companyLocation"}).text
                list_company_location.append(comany_location)
                try:
                        company_name = list_li[i].find("span", {"class": "companyName"}).text
                except:
                        company_name = None
                list_company_name.append(company_name)
        # return list_link_job,list_title_jobs,list_company_location,list_company_name

def get_page_source(driver: webdriver.Chrome) -> str:
        driver.get("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
        lil=driver.page_source
        list_link_job = [], list_title_jobs = [], list_company_location = [], list_company_name = []

        soup = BeautifulSoup(lil, "lxml")
        list_li = soup.findAll("div", {"class": "slider_item css-kyg8or eu4oa1w0"})
        for i in range(len(list_li)):
                link_job = "https://ma.indeed.com" + \
                           list_li[i].find("div", {"class": "css-1m4cuuf e37uo190"}).find("a")["href"]
                print(link_job)
                list_link_job.append(link_job)
                title = list_li[i].find("div", {"class": "css-1m4cuuf e37uo190"}).find("a").text
                list_title_jobs.append(title)
                comany_location = list_li[i].find("div", {"class": "companyLocation"}).text
                list_company_location.append(comany_location)
                try:
                        company_name = list_li[i].find("span", {"class": "companyName"}).text
                except:
                        company_name = None
                list_company_name.append(company_name)

async def createDriver() -> webdriver.Chrome:

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.headless = True
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--disable-features=NetworkService")
        # chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        # myDriver = webdriver.Chrome(service=ChromeService(executable_path="D:\\chromedriver\\chromedriver.exe"),
        #                             options=chrome_options)
        myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        get_page_source(myDriver)
        myDriver.close()


