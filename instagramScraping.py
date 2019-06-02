# -*- encoding UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

# hash tags title
tagName = input('#')

# ユーザーネームとパスワードを別ファイルから取得する
with open('keys.txt', 'r') as f:
    keys = f.readlines()
    username = keys[0]
    password = keys[1]

# 最初に立ち上げるURL。今回は映えを求めてyahooからスタートする
browserURL = 'http://www.yahoo.co.jp/'
# ハッシュタグの検索
tagSearchURL = "https://www.instagram.com/explore/tags/{}/?hl=ja" #tagsearch with hashtag

# Xpaths
loginPath = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a' #login botton
usernamePath = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/div[1]/input' #when login
passwordPath = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/div[1]/input' #when login
mediaSelector = 'div._9AhH0' # Post's selector
popPath = '/html/body/div[3]/div/div/div[3]/button[2]'# 'after' on Notification pop when logged in
nextPagerSelector = 'a.coreSpriteRightPaginationArrow' #nextpage
likeXpath = '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]'

driver = webdriver.Chrome()

# yahooの検索結果からIndstagramを探して、クリックする
driver.get(browserURL)
elem = driver.find_element_by_name('p')
elem.send_keys('Instagram')
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(2)

# ログインする
driver.find_element_by_link_text('Instagram').click()
driver.implicitly_wait(2)
driver.find_element_by_link_text('ログインする').click()
driver.find_element_by_xpath(loginPath).click()
driver.implicitly_wait(5)
usernameField = driver.find_element_by_xpath(usernamePath)
usernameField.send_keys(username)
passwordField = driver.find_element_by_xpath(passwordPath)
passwordField.send_keys(password)
time.sleep(1)
passwordField.send_keys(Keys.RETURN)

# ログイン後のポップに「あとで」をクリック
driver.implicitly_wait(5)
popIgnore = driver.find_element_by_xpath(popPath)
popIgnore.click()

#ハッシュタグをエンコーディングする
encodedTag = urllib.parse.quote(tagName)
encodedURL = tagSearchURL.format(encodedTag)
driver.get(encodedURL)
driver.implicitly_wait(5)
mediaList = driver.find_elements_by_css_selector(mediaSelector)

# ハッシュタグに対してひたすらいいねしてく
for media in mediaList:
    media.click()
    while True:
        try:
            time.sleep(2)
            driver.find_element_by_xpath(likeXpath).click()
            driver.implicitly_wait(10)
            driver.find_element_by_css_selector(nextPagerSelector).click()
        except:
            break
    break
