from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10) # seconds
driver.maximize_window()
driver.get("http://www.edx.org")
assert "edX" in driver.title
# Xpath location click for some reasons doesnt work
#login_link = driver.find_element_by_xpath("//*[@id='primary-menu-bar']/nav/ul/li[3]/a[1]")

login_link = driver.find_element_by_link_text('Sign In')
login_link.click()

login_email = driver.find_element_by_id('login-email')
login_password = driver.find_element_by_id('login-password')

login_email.send_keys("your_email")
login_password.send_keys("your_password")
login_email.send_keys(Keys.RETURN)

#wait = WebDriverWait(driver,20)

#frame = driver.find_element_by_tag_name('iframe')
#driver.switch_to.frame(frame)

def get_dropdown():
	try:
		course_tag = driver.find_element_by_id('actions-dropdown-link-0')
		return course_tag
	except:
		return None	


course_tag = get_dropdown()
while (course_tag != None):
	course_tag.click()

	action_tag = driver.find_element_by_link_text('Unenroll')
	action_tag.click()


	time.sleep(3) 

	unenroll_button_tag = driver.find_element_by_name('submit')
	unenroll_button_tag.click()

	time.sleep(3) 

	submit_unenroll_tag = driver.find_element_by_class_name('submit_reasons')
	submit_unenroll_tag.click()

	time.sleep(3)
	back_to_dashboard_tag = driver.find_element_by_link_text('Return To Dashboard')
	back_to_dashboard_tag.click()
	time.sleep(3)
	course_tag = get_dropdown()









#login_password.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
# driver.close()
