# import schedule
import time
import yaml
import datetime
import random
# import getpass

from threading import Timer
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

credentials = yaml.load(open('change.yml'))
timeout = 3

def get_driver():
    chrome_options = Options()
    # # 關閉通知(是否顯示通知)
    prefs = {
        'profile.default_content_setting_values':
        {
            'notifications':2
        }
    }
    chrome_options.add_experimental_option('prefs', prefs)
    
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("window-size=1024,768")
    # chrome_options.add_argument('headless')                 # 瀏覽器不提供可視化頁面
    chrome_options.add_argument('no-sandbox')               # 以最高權限運行
    chrome_options.add_argument('--start-maximized')        # 縮放縮放（全屏窗口）設置元素比較準確
    chrome_options.add_argument('--disable-gpu')            # 谷歌文檔說明需要加上這個屬性來規避bug
    chrome_options.add_argument('--window-size=1920,1080')  # 設置瀏覽器按鈕（窗口大小）
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options = chrome_options, executable_path = 'chromedriver')

    url = credentials['yawen_url']
    toast_url = url
    driver.get(toast_url)
 

    return driver

def toast():    
    try:
<<<<<<< HEAD
        for i in range(1, 5):
=======
        for i in range(1, 11):
>>>>>>> refs/remotes/origin/main
            if i == 9 or i == 13:
                pass
            else:
                driver = get_driver()
<<<<<<< HEAD
                WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'entry-title')))
                login(i, driver) 
                time.sleep(3)
                vote(driver)
                print(i)
                time.sleep(3)
                login(i, driver) 
                time.sleep(10)
                driver.switch_to_alert().accept()        #點選彈出裡面的確定按鈕
=======
                time.sleep(3)
                # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'logo-area')))
                # vote(driver)
                print(i)
                time.sleep(3)
                login(i, driver) 
>>>>>>> refs/remotes/origin/main
                time.sleep(15)
                now = datetime.datetime.now()     
                date_time = now.strftime('%Y%m%d')
                fime_time = date_time+str(i)+'.png'
                print(fime_time)
                driver.get_screenshot_as_file('./yawen/' + fime_time +'')       #截圖的名稱拼接上日期
                driver.quit()
<<<<<<< HEAD
=======
                r = random.randrange(1,180)
                time.sleep(r)
>>>>>>> refs/remotes/origin/main
                # done_title = done_vote.text
                # if done_title == '已投票':
                #     print(done_title)
                    
                # else:
                #     done_vote.click()
                #     time.sleep(20)
                #     print(done_title)  
                #     now = datetime.datetime.now()     #截圖的名稱拼接上日期
                #     date_time = now.strftime('%Y%m%d')
                #     fime_time = date_time+str(i)+'.png'
                #     print(fime_time)
                #     driver.get_screenshot_as_file('./angel/' + fime_time +'')
                #     driver.quit()
                #     r = random.randrange(1,180)
                #     time.sleep(r)
    finally:
        time.sleep(3)
        driver.quit()

def vote(driver):   
    toast = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/article/header/h2/text()')
    toast_name = toast.text
    print(toast_name)
    try:
        if toast_name == '''
                            懷念的家鄉
                            ''':
            print(toast_name)
    except NoSuchElementException as NE:
        raise TypeError(toast_name) from NE
    
def login(i, driver):
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/article/div[2]/div/div/a[1]').click()  #click FB 
    time.sleep(3)

    username = credentials['login' + str(i) +'']['username']
    driver.find_element(By.ID, 'email').send_keys(username) #FB username

    password = credentials['login' + str(i) +'']['password']
    driver.find_element(By.ID, 'pass').send_keys(password) #FB pwd
    time.sleep(3)
<<<<<<< HEAD
    login = driver.find_element(By.ID, 'loginbutton').click()
=======
    login = driver.find_element(By.NAME, 'login').click()
>>>>>>> refs/remotes/origin/main
    print('%s登入成功'%username)
    time.sleep(3)

    return i



if __name__ == '__main__':
    toast()