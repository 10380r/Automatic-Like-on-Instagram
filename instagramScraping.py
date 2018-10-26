# -*- encoding UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

tagName = input('#')
username = 'i_wanna_likes_for_you'
password = 'r19971104'
browserURL = 'http://www.yahoo.co.jp/'

# Xpaths
loginPath = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
usernamePath = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/div[1]/input'
passwordPath = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/div[1]/input'#パスワード
mediaSelector = 'div._9AhH0'
notNowPath = '//*[@id="react-root"]/div/div[2]/a[2]'
popPath = '/html/body/div[2]/div/div/div/div[3]/button[2]' #ログイン後のpopの後でボタン
nextPagerSelector = 'a.coreSpriteRightPaginationArrow' #次へボタン
likeXpath = '/html/body/div[2]/div/div[2]/div/article/div[2]/section[1]/span[1]/button'#いいね


driver = webdriver.Chrome()

# ヤフーを開いて検索窓に入力　クリック
driver.get(browserURL)
elem = driver.find_element_by_name('p')
elem.send_keys('Instagram')
elem.send_keys(Keys.RETURN)

driver.implicitly_wait(2)

driver.find_element_by_link_text('Instagram').click()

driver.implicitly_wait(2)

driver.find_element_by_link_text('ログインする').click()

#driver.get(login)
driver.find_element_by_xpath(loginPath).click()
driver.implicitly_wait(5)
usernameField = driver.find_element_by_xpath(usernamePath)
usernameField.send_keys(username)
passwordField = driver.find_element_by_xpath(passwordPath)
passwordField.send_keys(password)
time.sleep(1)
passwordField.send_keys(Keys.RETURN)

# ログインした瞬間にお知らせ機能のポップが出るのを対処
time.sleep(5)
popIgnore = driver.find_element_by_xpath(popPath)
popIgnore.click()

tagSearchURL = "https://www.instagram.com/explore/tags/{}/?hl=ja"
encodedTag = urllib.parse.quote(tagName)
encodedURL = tagSearchURL.format(encodedTag)
driver.get(encodedURL)
driver.implicitly_wait(5)
mediaList = driver.find_elements_by_css_selector(mediaSelector)

for media in mediaList:
    media.click()

    while True:
        try:
            time.sleep(3)
            driver.find_element_by_xpath(likeXpath).click()
            driver.implicitly_wait(10)
            driver.find_element_by_css_selector(nextPagerSelector).click()
        except:
            break
    break #for文自体も終了させる
