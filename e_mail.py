from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = 'https://www.naver.com/'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)


## 네이버 로그인 우회
id = "hintda"
pw = "qorltjd48^"

driver.find_element_by_css_selector('.link_login').click()



# execute_script 함수 사용 (자바스크립트로 아이디, 패스워드를 넘겨주는 형태)
driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.find_element_by_css_selector('.pw_area').click()

driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
driver.find_element_by_css_selector('.btn_global').click()


time.sleep(2)
driver.get('https://mail.naver.com/#%7B%22fClass%22%3A%22write%22%2C%22oParameter%22%3A%7B%22orderType%22%3A%22new%22%2C%22sMailList%22%3A%22%22%7D%7D')

time.sleep(1)
action.send_keys('dlckstn89@gmail.com').pause(1).key_down(Keys.TAB).key_down(Keys.TAB).send_keys('제목입니다.').pause(1).key_down(Keys.TAB).send_keys('내용입니다').perform()
#action값이 남아있어 초기화를 시켜줘야된다
action.reset_actions()

#driver.find_element_by_css_selector('.buSend').click()







