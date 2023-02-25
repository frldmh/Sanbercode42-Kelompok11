import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogout(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_logout(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(8) > a").text
        self.assertIn('Dashboard', response_data)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-header > div.oxd-topbar-header-userarea > ul > li > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-header > div.oxd-topbar-header-userarea > ul > li > ul > li:nth-child(4) > a").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > h5").text
        self.assertIn('Login', response_data)
        time.sleep(3)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
