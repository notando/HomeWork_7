from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.firefox.options import Options

driver_g = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\chromedriver.exe")
# driver_g.get('http://www.walla.co.il')
# web_title = driver_g.title
# driver_g.refresh()
# if web_title == driver_g.title:
#     print('Same')

#============================================
# #driver_g.get('https://translate.google.com/')
# #driver_g.find_element_by_id('source').send_keys('פרצתי אותך')
# driver_g.get('https://www.youtube.com/')
# driver_g.find_element_by_id('search').send_keys('NFS')
# driver_g.find_element_by_id('search-icon-legacy').click()
# def ok_ru():
#     driver_g.get("https://ok.ru")
#     driver_g.find_element_by_id('field_email').send_keys('alalal')
#     driver_g.find_element_by_id('field_password').send_keys('alalal')
#     driver_g.find_element_by_xpath('//*[@id="anonymPageContent"]/div[2]/div[1]/div[3]/form/div[5]/div[1]/input').click()
# ok_ru()
#====================[[ Chalenge]]=======================


# ab=driver_g.get_cookies()
# driver_g.delete_all_cookies()
# print(ab)
# a = driver_g.get_cookies()
# print(a)

#==============================
driver_g.get('https://github.com/login?return_to=%2Fjoin')
driver_g.find_element_by_id('login_field').send_keys('notando')
driver_g.find_element_by_id('password').send_keys('PhqE2keB9NQPjpY')
driver_g.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]').click()
sleep(2)
driver_g.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div/form/label/input[1]').send_keys("Internet of things" + Keys.ENTER)
#=====================================

browser = webdriver.Ie(executable_path="C:\\Program Files (x86)\\chromedriver.exe", ie_options=ie_options)
Ie_options = Options()
Ie_options.add_argument("--disable-extensions")
#webdriver.Firefox(firefox_options=firefox_options)