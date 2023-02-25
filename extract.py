from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



async def createDriver() -> webdriver.Chrome:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.headless = True

        chrome_options.add_experimental_option("prefs", prefs)
        myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        # chrome_options = webdriver.ChromeOptions()
        # # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # # chrome_options.headless = True
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument("--test-type")
        # chrome_options.add_argument('--log-level=3')
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--disable-web-security")
        # chrome_options.add_argument("--allow-running-insecure-content")
        # chrome_options.add_argument("--mute-audio")
        # chrome_options.add_argument("--disable-features=NetworkService")
        # # chrome_options.add_argument("--window-size=1920x1080")
        # chrome_options.add_argument("--disable-features=VizDisplayCompositor")
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
        # chrome_options.add_argument('user-agent={0}'.format(user_agent))
        # # myDriver = webdriver.Chrome(service=ChromeService(executable_path="D:\\chromedriver\\chromedriver.exe"),
        # #                             options=chrome_options)
        # chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        # myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return myDriver


async def get_page_source(driver: webdriver.Chrome) -> str:
        driver.get("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
        return driver.page_source

