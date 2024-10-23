from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
from termcolor import colored
from bs4 import BeautifulSoup
import requests
import time
import pyautogui
import os
import random
import time
import sys
from colorama import init, Fore, Style
banner = "YOUTUBE PLAYLIST V.10"
byx = "CREATED BY: AGUNG ID™\n"
x = byx.center(50)
z = banner.center(50)
os.system('cls' if os.name == 'nt' else 'clear')
print(colored(z, 'red', ))
print(colored(x, 'green'))
license_url = 'https://raw.githubusercontent.com/agunggunawanid/license/main/username.txt'
headers = {'Authorization': 'KEYAUTH-8C5QpG-JupTUw-EAd1Qt-eGGwTf-InE0uj-873sCL'}
init(autoreset=True)
def running_text_color(text, color=Fore.GREEN, speed=0.1):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print()
response = requests.get(license_url, headers=headers).text
license_keys = response.splitlines()
def check_license(key):
    return key in license_keys
user_key = input(colored('\n👤 Enter Username: ', 'green'))
if check_license(user_key):
    text = "✅ Username Valid, Please wait...."
    running_text_color(text, color=Fore.BLUE, speed=0.1)
else:  # inserted
    WR = '[X]'.center(60)
    US = 'Incorrect Username'.center(60)
    GT = 'Get Username Please Contact Me:'.center(60)
    SR = '=========================================================='
    EM = '[1] Email.....: agunggunawann.id@gmail.com             [1]'
    WA = '[2] Whatsapp..: https://wa.me/+6285759406150           [2]'
    TE = '[3] Telegram..: https://t.me/agunggunawann.id          [3]'
    FB = '[4] Facebook..: https://facebook.com/agunggunawann.id  [4]'
    IG = '[5] Instagram.: https://instagram.com/agunggunawann.id [5]'
    ST = '=========================================================='
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(WR, 'red'))
    print(colored(US, 'red'))
    print(colored(GT, 'green'))
    print(colored(SR, 'white'))
    print(colored(EM, 'white'))
    print(colored(WA, 'white'))
    print(colored(TE, 'white'))
    print(colored(FB, 'white'))
    print(colored(IG, 'white'))
    print(colored(ST, 'white'))
    time.sleep(20)
    os._exit(0)
os.system('cls' if os.name == 'nt' else 'clear')
print(colored(z, 'red', ))
print(colored(x, 'green'))
email = input(colored('\n[1] Email...........: ', 'cyan'))
pwd = input(colored('[2] Password........: ', 'cyan'))
jumchnl = input(colored('[3] Jumlah Channel..: ', 'cyan'))
muldr = input(colored('[4] Dari Channel Ke.: ', 'cyan'))
files = input(colored('[5] File Excel xlsx.: ', 'cyan'))
jumplyst = input(colored('[6] Jumlah Playlist.: ', 'cyan'))
mtlang = 'aktif'
mtlang = 'nonaktif'
options = webdriver.ChromeOptions()
options.add_argument('--lang=en-US')
options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
prefs = {'profile.default_content_setting_values.notifications': 2}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)
wb = load_workbook(filename=files)
sheetRange = wb['Sheet1']
driver.get('https://youtube.com/channel_switcher')
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"identifierId\"]')))
emailes = driver.find_element(By.XPATH, '//*[@id=\"identifierId\"]')
emailes.send_keys(email)
next1 = driver.find_element(By.XPATH, '//*[@id=\"identifierNext\"]/div/button')
next1.click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"password\"]/div[1]/div/div[1]/input')))
passw = driver.find_element(By.XPATH, '//*[@id=\"password\"]/div[1]/div/div[1]/input')
passw.send_keys(pwd)
next2 = driver.find_element(By.XPATH, '//*[@id=\"passwordNext\"]/div/button')
next2.click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"contents\"]/ytd-account-item-renderer[2]')))
cnl = driver.find_element(By.XPATH, '//div[@id=\"contents\"]/ytd-account-item-renderer[2]')
cnl.click()
time.sleep(2)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"body\"]')))
gethtml = driver.find_element(By.XPATH, '//div[@id=\"body\"]').get_attribute('innerHTML')
basehtml = BeautifulSoup(gethtml, 'html.parser')
getcontents = basehtml.find('div', {'id': 'contents'}).find_all('ytd-account-item-renderer')
totch = len(getcontents)
totchnl = totch - 1
allchnlname = {}
for nmch in range(0, int(totchnl)):
    jch = nmch + 1
    getchname = getcontents[jch].find('yt-formatted-string', {'id': 'channel-title'}).text
    allchnlname['ch{0}'.format(jch)] = getchname
for zoom in range(0, 2):
    pyautogui.hotkey('ctrl', '-')
    time.sleep(1)
driver.get('https://studio.youtube.com/')
for zoom2 in range(0, 5):
    pyautogui.hotkey('ctrl', '-')
    time.sleep(1)
for i in range(int(muldr), int(jumchnl)):
    vid = i + 1
    chanelname = allchnlname['ch' + str(i)]
    driver.get('https://studio.youtube.com/')
    print(colored('\nChannel Name : ' + chanelname, 'yellow'), colored(i, 'red'))
    try:
        driver.find_element(By.XPATH, '//ytcp-button[@id="dismiss-button"]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
        time.sleep(1)
    except:
        pass
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//button[@id=\"avatar-btn\"]')))
    swchnl = driver.find_element(By.XPATH, '//button[@id=\"avatar-btn\"]')
    swchnl.click()
    time.sleep(1)
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"items\"]/ytd-compact-link-renderer[3]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]')))
    swchnls = driver.find_element(By.XPATH, '//div[@id=\"items\"]/ytd-compact-link-renderer[3]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]')
    swchnls.click()
    time.sleep(2)
    try:
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//yt-formatted-string[@id=\"channel-title\"][text()=\"' + chanelname + '\"]')))
        tochnl = driver.find_element(By.XPATH, '//yt-formatted-string[@id=\"channel-title\"][text()=\"' + chanelname + '\"]')
        tochnl.location_once_scrolled_into_view
        tochnl.click()
        time.sleep(2)
    except:
        print('Channel Habis')
        break
    if mtlang == 'aktif':
        driver.get('https://www.youtube.com/')
        time.sleep(2)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//button[@id=\"avatar-btn\"]')))
        clikavt = driver.find_element(By.XPATH, '//button[@id=\"avatar-btn\"]')
        clikavt.click()
        time.sleep(2)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"container\"]/div[1]/yt-multi-page-menu-section-renderer[3]/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item')))
        clibhs = driver.find_element(By.XPATH, '//div[@id=\"container\"]/div[1]/yt-multi-page-menu-section-renderer[3]/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item')
        clibhs.click()
        time.sleep(2)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//yt-formatted-string[contains(text(),\"English (US)\")]')))
        toengus = driver.find_element(By.XPATH, '//yt-formatted-string[contains(text(),\"English (US)\")]')
        toengus.location_once_scrolled_into_view
        toengus.click()
        time.sleep(2)
    else:  # inserted
        pass
    driver.get('https://studio.youtube.com/')
    try:
        conty = driver.find_element(By.XPATH, '//ytcp-button[@id="dismiss-button"]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        conty.click()
        time.sleep(1)
    except:
        pass
    try:
        clsntfy = driver.find_element(By.XPATH, '//ytcp-button[@id="close-button"]/ytcp-button-shape/button')
        clsntfy.click()
        time.sleep(1)
    except:
        pass
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menu-paper-icon-item-7"]')))
    Customization = driver.find_element(By.XPATH, '//*[@id="menu-paper-icon-item-7"]')
    Customization.click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]')))
    tabsContent = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]')
    tabsContent.click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="home-tab-enabled-toggle"]/div[1]')))
    enabled = driver.find_element(By.XPATH, '//*[@id="home-tab-enabled-toggle"]/div[1]')
    enabled.click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shelf-actions-menu"]')))
    act1 = driver.find_element(By.XPATH, '//*[@id="shelf-actions-menu"]')
    act1.click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="text-item-0"]')))
    dellt = driver.find_element(By.XPATH, '//*[@id="text-item-0"]')
    dellt.click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shelf-actions-menu"]')))
    act1 = driver.find_element(By.XPATH, '//*[@id="shelf-actions-menu"]')
    act1.click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="text-item-0"]')))
    dellt = driver.find_element(By.XPATH, '//*[@id="text-item-0"]')
    dellt.click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shelf-actions-menu"]')))
    act1 = driver.find_element(By.XPATH, '//*[@id="shelf-actions-menu"]')
    act1.click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="text-item-0"]')))
    dellt = driver.find_element(By.XPATH, '//*[@id="text-item-0"]')
    dellt.click()
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shelf-actions-menu"]')))
    act1 = driver.find_element(By.XPATH, '//*[@id="shelf-actions-menu"]')
    act1.click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="text-item-0"]')))
    dellt = driver.find_element(By.XPATH, '//*[@id="text-item-0"]')
    dellt.click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="publish-button"]/ytcp-button-shape/button')))
    publis = driver.find_element(By.XPATH, '//*[@id="publish-button"]/ytcp-button-shape/button')
    publis.click()
    time.sleep(7)
    tit = i * int(jumplyst)
    dsk = tit + int(jumplyst)
    for det in range(tit, dsk):
        data = det + 1 - int(jumplyst)
        tittle = sheetRange['A' + str(data)].value
        liga = sheetRange['B' + str(data)].value
        vid2 = sheetRange['C' + str(data)].value
        desc1 = sheetRange['D' + str(data)].value
        thum = sheetRange['E' + str(data)].value
        linkk = sheetRange['F' + str(data)].value
        vers = sheetRange['G' + str(data)].value
        masct = sheetRange['H' + str(data)].value
        hom = sheetRange['I' + str(data)].value
        away = sheetRange['J' + str(data)].value
        hastag = sheetRange['K' + str(data)].value
        description = f'Live Stream: {vers}\nThe official broadcast of the match in excellent quality will soon be available here. You just need:\n1 Click the link In the Chat Link Below\n2 Watch live legally without ads\n\n{masct}\n{desc1}\n\n{hom} vs {away}\n{hom} Vs. {away}\n{hom} @ {away}\n{hom} - {away}\n{hom} and {away}\n\nTAG :\n{hastag}'
        print(colored('PLAYLIST KE : ', 'green'), colored(data, 'red'))
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="menu-paper-icon-item-1"]')))
        konten = driver.find_element(By.XPATH, '//*[@id="menu-paper-icon-item-1"]')
        konten.click()          
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//tp-yt-paper-tab[@id=\"playlist-list-tab\"]')))
        playlys = driver.find_element(By.XPATH, '//tp-yt-paper-tab[@id=\"playlist-list-tab\"]')
        playlys.click()
        try:
           driver.find_element(By.XPATH, '//ytcp-button[@id="dismiss-button"]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
           time.sleep(1)
        except:
            pass
        time.sleep(1)
        try:
            WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Create']")))
            create_button = driver.find_element(By.XPATH, "//button[@aria-label='Create']")
            create_button.click()
            playlist_option = WebDriverWait(driver, 1).until(
	        EC.presence_of_element_located((By.XPATH, "//yt-formatted-string[text()='New playlist']")))
            playlist_option.click()
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//ytcp-social-suggestions-textbox[@id=\"title-textarea\"]/ytcp-form-input-container/div[1]/div/div/ytcp-social-suggestion-input/div')))
            judlb = driver.find_element(By.XPATH, '//ytcp-social-suggestions-textbox[@id=\"title-textarea\"]/ytcp-form-input-container/div[1]/div/div/ytcp-social-suggestion-input/div')
            judlb.send_keys(tittle)
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add description\"]')))
            deskrpsy = driver.find_element(By.XPATH, '//div[@aria-label=\"Add description\"]')
            deskrpsy.send_keys(description)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menu-button"]/ytcp-dropdown-trigger/div/div[2]')))
            Visibility = driver.find_element(By.XPATH, '//*[@id="menu-button"]/ytcp-dropdown-trigger/div/div[2]')
            Visibility.click()
            unlisted_option = driver.find_element(By.XPATH, '//*[text()="Unlisted"]')
            unlisted_option.click()
            time.sleep(1)
            driver.find_element(By.XPATH,'//ytcp-playlist-metadata-sorting/div/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="text-item-5"]/ytcp-ve/tp-yt-paper-item-body/div/div/div/yt-formatted-string').click()
            time.sleep(1)
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//ytcp-button[@id=\"create-button\"]')))
            creates = driver.find_element(By.XPATH, '//ytcp-button[@id=\"create-button\"]')
            creates.click()
            time.sleep(3)
            # inserted
            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//ul[@id=\"main-menu\"]/li[2]/ytcp-ve/a/tp-yt-paper-icon-item/div/tp-yt-iron-icon')))
                kontens = driver.find_element(By.XPATH, '//ul[@id=\"main-menu\"]/li[2]/ytcp-ve/a/tp-yt-paper-icon-item/div/tp-yt-iron-icon')
                kontens.click()
            except:
                print(colored('PLAYLIST LIMITED', 'red'))
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//ytcp-button[@label=\"Cancel\"]/div')))
                clslmt = driver.find_element(By.XPATH, '//ytcp-button[@label=\"Cancel\"]/div')
                clslmt.click()
                time.sleep(2)
                break
            else:   # inserted
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//tp-yt-paper-tab[@id=\"playlist-list-tab\"]')))
            playlyss = driver.find_element(By.XPATH, '//tp-yt-paper-tab[@id=\"playlist-list-tab\"]')
            playlyss.click()
                # inserted
            try:
                driver.find_element(By.XPATH, '//ytcp-button[@id="dismiss-button"]/ytcp-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
                time.sleep(1)
                time.sleep(1)
            except:
                pass
                # inserted
            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"playlist-table-content\"]/ytcp-playlist-row[1]/div/div[1]/div/a')))
                linkplys = driver.find_element(By.XPATH, '//div[@id=\"playlist-table-content\"]/ytcp-playlist-row[1]/div/div[1]/div/a').get_attribute('href')
                time.sleep(1)
                if 'studio.' in linkplys:
                    removeedit = linkplys.replace('/edit', '')
                    linkplyst = removeedit.replace('studio.youtube.com/playlist/', 'youtube.com/playlist?list=')
                else:  # inserted
                    linkplyst = linkplys
                driver.execute_script('window.open(\'\');')
                driver.switch_to.window(driver.window_handles[1])
                driver.get(linkplyst)
                time.sleep(1)
            except:
                driver.refresh()
                time.sleep(1)
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@id=\"playlist-table-content\"]/ytcp-playlist-row[1]/div/div[1]/div/a')))
                linkplys = driver.find_element(By.XPATH, '//div[@id=\"playlist-table-content\"]/ytcp-playlist-row[1]/div/div[1]/div/a').get_attribute('href')
                time.sleep(1)
                driver.execute_script('window.open(\'\');')
                driver.switch_to.window(driver.window_handles[1])
                driver.get(linkplys)
                time.sleep(1)
                # inserted
            try:
                WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label=\"Add videos\"]')))
                advidnew = driver.find_element(By.XPATH, '//button[@aria-label=\"Add videos\"]')
                advidnew.click()
            except:
                WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//yt-button-shape[@id=\"button-shape\"]/button')))
                seti = driver.find_element(By.XPATH, '//yt-button-shape[@id=\"button-shape\"]/button')
                seti.click()
                WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//tp-yt-paper-listbox[@id=\"items\"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')))
                advid = driver.find_element(By.XPATH, '//tp-yt-paper-listbox[@id=\"items\"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')
                advid.click()
            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby=\":1\"]/div[2]/div/iframe')))
                driver.switch_to.frame(driver.find_element(By.XPATH, '//div[@aria-labelledby=\":1\"]/div[2]/div/iframe'))
            except:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby=\":0\"]/div[2]/div/iframe')))
                driver.switch_to.frame(driver.find_element(By.XPATH, '//div[@aria-labelledby=\":0\"]/div[2]/div/iframe'))
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//input[2]')))
            adevn = driver.find_element(By.XPATH, '//input[2]')
            adevn.send_keys(thum)
            adevn.send_keys(Keys.ENTER)
            time.sleep(2)
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div')))
            adevnvid = driver.find_element(By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div')
            adevnvid.click()
            time.sleep(1)
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[5]/div/div[3]/button')))
            svadevnvid = driver.find_element(By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[5]/div/div[3]/button')
            svadevnvid.click()
            time.sleep(2)
            driver.switch_to.default_content()
            # inserted
            try:
                WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label=\"Add videos\"]')))
                advidnew1 = driver.find_element(By.XPATH, '//button[@aria-label=\"Add videos\"]')
                advidnew1.click()
            except:
                WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//yt-button-shape[@id=\"button-shape\"]/button')))
                seti1 = driver.find_element(By.XPATH, '//yt-button-shape[@id=\"button-shape\"]/button')
                seti1.click()
                WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//tp-yt-paper-listbox[@id=\"items\"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')))
                advid1 = driver.find_element(By.XPATH, '//tp-yt-paper-listbox[@id=\"items\"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item/yt-formatted-string')
                advid1.click()
                # inserted
            try:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby=\":1\"]/div[2]/div/iframe')))
                driver.switch_to.frame(driver.find_element(By.XPATH, '//div[@aria-labelledby=\":1\"]/div[2]/div/iframe'))
            except:
                WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-labelledby=\":0\"]/div[2]/div/iframe')))
                driver.switch_to.frame(driver.find_element(By.XPATH, '//div[@aria-labelledby=\":0\"]/div[2]/div/iframe'))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[2]')))
            adevn1 = driver.find_element(By.XPATH, '//input[2]')
            adevn1.send_keys(vid2)
            adevn1.send_keys(Keys.ENTER)
            time.sleep(2)
            rand = random.randint(15, 20)
                # inserted
            try:
                for advidtoply in range(0, rand):
                    selvid = advidtoply + 1
                    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[' + str(selvid) + ']/div')))
                    advidtopls = driver.find_element(By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[3]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[' + str(selvid) + ']/div')
                    advidtopls.location_once_scrolled_into_view
                    advidtopls.click()
            except:
                pass
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[5]/div/div[3]/button')))
            svadevnvid1 = driver.find_element(By.XPATH, '//div[@aria-label=\"Add video to playlist\"]/div[5]/div/div[3]/button')
            svadevnvid1.click()
            time.sleep(5)
            driver.switch_to.default_content()
            print(colored(str(advidtoply) + ' Video Added to Playlis', 'white'))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except: 
         print(colored('There is an error', 'red'))
         time.sleep(1)
         driver.close()
         driver.switch_to.window(driver.window_handles[0])
         continue
        print(colored('Playlist Created Successfully', 'blue'))
        continue