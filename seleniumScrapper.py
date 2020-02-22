from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)


driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('python')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
driver.find_element_by_css_selector('.LC20lb.DKV0Md').click()   #클래스명사이에 공백이 있으면 지우고 .으로 대체해야함

