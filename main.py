import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from colorama import Fore, init
import requests
import time
import random
import string
import os
import tls_client
from pystyle import Center
import pyfiglet

banner = f'''
[+] Creator - Termwave | Lunarmart  
[+] Credits - Chorus 
'''

def account_ratelimit():
    """Fetches rate limit using account creation data."""
    try:
        m = format(''.join(random.choice(string.digits) for _ in range(6)))
        email = format(''.join(random.choice(string.ascii_lowercase) for _ in range(9)))+m
        mail = "{}@gmail.com".format(''.join(random.choice(string.ascii_lowercase) for _ in range(11)))
        nam = "ultimate"
        client = tls_client.Session(client_identifier='chrome_110')
        client.headers = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.5",
                "Content-Type": "application/json",
                "DNT": "1",
                "Host": "discord.com",
                "Origin": "https://discord.com",
                "Referer": 'https://discord.com/register',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
                "X-Debug-Options": "bugReporterEnabled",
                "X-Discord-Locale": "en-US",
                "X-Discord-Timezone": "Asia/Calcutta",
                "X-Super-Properties": 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIEZyYW1lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImdyLUFSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS80LjAgKGNvbXBhdGlibGU7IE1TSUUgOC4wOyBXaW5kb3dzIE5UIDYuMTsgVHJpZGVudC80LjA7IEdUQjcuNDsgY2hyb21lZnJhbWUvMjQuMC4xMzEyLjU3OyBTTENDMjsgLk5FVCBDTFIgMi4wLjUwNzI3OyAuTkVUIENMUiAzLjUuMzA3Mjk7IC5ORVQgQ0xSIDMuMC4zMDcyOTsgLk5FVDQuMEM7IEluZm9QYXRoLjM7IE1TLVJUQyBMTSA4OyBCUkkvMikiLCJicm93c2VyX3ZlcnNpb24iOiIyNC4wLjEzMTIiLCJvc192ZXJzaW9uIjoiNyIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cueW91dHViZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy55b3V0dWJlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJhc2suY29tIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0ODQ3OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
            }
        data = {
                'email': mail,
                'password': 'ultimate12$$',
                'date_of_birth': "2000-09-20",
                'username': email,
                'consent': True,
                'captcha_service': 'hcaptcha',
                'global_name': nam,
                'captcha_key': None,
                'invite': None,
                'promotional_email_opt_in': False,
                'gift_code_sku_id': None
            }
        req = client.post(f'https://discord.com/api/v9/auth/register', json=data)
        if 'The resource is being rate limited' in req.text:
                limit = req.json()['retry_after']
                return limit
        else:
                return 1
    except Exception as e:
        print(f'{Fore.RED}[{Fore.RESET}{Fore.MAGENTA}*{Fore.RESET}{Fore.RED}]{Fore.RESET}{Fore.RED} Error fetching rate limit: {str(e)}')
        return 1

init(autoreset=True)
os.system("cls")
os.system("title Ultimate EV Tool")
def random_sleep(base=2, variation=3):
    time.sleep(base + random.uniform(0, variation))

def generate_yopmail_email():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    email = f"{username}@1xp.fr"
    return username, email

def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def main():
    ultimate = pyfiglet.figlet_format("ULTIMATE", font="bloody")
    print(Fore.CYAN + Center.XCenter(ultimate))
    print(Fore.CYAN + Center.XCenter(banner))
    while True:
        username, email = generate_yopmail_email()
        driver = None
        try:
            options = uc.ChromeOptions()
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--disable-blink-features=AutomationControlled")  
            options.add_argument("--disable-infobars")  
            options.add_argument("--disable-extensions")
            driver = uc.Chrome(options=options)
            driver.maximize_window()
            driver.get("https://discord.com/register")
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
            password = "Ultimate69Op"
            driver.find_element(By.NAME, "email").send_keys(email)
            driver.find_element(By.NAME, "global_name").send_keys("LunarxTerm")
            username = generate_random_string()
            driver.find_element(By.NAME, "username").send_keys(username)
            driver.find_element(By.NAME, "password").send_keys(password)
            element_3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'react-select-2-input')))
            element_3.send_keys(random.randint(1, 28))
            element_3.send_keys(Keys.RETURN)
            element_2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'react-select-3-input')))
            element_2.send_keys(random.choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']))
            element_2.send_keys(Keys.RETURN)
            element_4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'react-select-4-input')))
            element_4.send_keys(random.randint(1995, 2005))
            continue_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
            limit = account_ratelimit()
            if limit > 1:
                print(f'{Fore.RED}[{Fore.RESET}{Fore.MAGENTA}*{Fore.RESET}{Fore.RED}]{Fore.RESET}{Fore.WHITE} Ratelimited for {limit} seconds. Retrying after ratelimit disappears.')
                time.sleep(limit)
            continue_button.click()
            print(f"{Fore.GREEN}[{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Please solve the captcha manually...")
            while True:
                WebDriverWait(driver, 300).until(EC.url_contains("discord.com/channels/@me"))
                print(f"{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}>{Fore.RESET}{Fore.BLUE}]{Fore.RESET}{Fore.WHITE} CAPTCHA solved and redirected to @me. Verifying email...")
                usernamebaba = email.split('@')[0]
                driver.get(f"https://yopmail.com/en/?login={usernamebaba}")
                print(f"{Fore.GREEN}[{Fore.RESET}{Fore.MAGENTA}!{Fore.RESET}{Fore.GREEN}]{Fore.RESET}{Fore.WHITE} Once you've verified email, Close the Browser to continue...")
                while True:
                    try:
                        driver.title  
                    except Exception:
                        break
                login_and_fetch_token(email, password)  
                break                
        finally:
            if driver:
                try:
                    driver.quit()
                except Exception as e:
                    pass
                finally:
                    driver = None 
                    
def login_and_fetch_token(email, password):
    data = {"email": email, "password": password, "undelete": "false"}
    headers = {
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    }
    r = requests.post("https://discord.com/api/v9/auth/login", json=data, headers=headers)
    if r.status_code == 200:
        token = r.json().get("token")
        if token:
            print(f"{Fore.BLUE}[{Fore.RESET}{Fore.MAGENTA}>{Fore.RESET}{Fore.BLUE}]{Fore.RESET}{Fore.WHITE} Got token -> {email}:{password}:{token}")
            with open("tokens.txt", "a") as f:
                f.write(f"{token}\n")
            with open("evs.txt", "a") as f:
                f.write(f"{email}:{password}:{token}\n")
            return True
    elif "captcha-required" in r.text:
        print(f"{Fore.RED}[{Fore.RESET}{Fore.MAGENTA}*{Fore.RESET}{Fore.RED}]{Fore.RESET}{Fore.WHITE} Error fetching token for {email}")
        return False
    return False

if __name__ == "__main__":
    main()