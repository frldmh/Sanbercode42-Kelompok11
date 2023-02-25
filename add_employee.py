import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestAddEmployee(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_add_employee(self):
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
        driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3) > a").click()
        time.sleep(1)
        response_data = driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--visited > a").text
        self.assertEqual('Add Employee', response_data)
        time.sleep(2)

        # step Input employee
        driver.find_element(By.NAME,"firstName").send_keys("Dinda") # isi firstname
        time.sleep(1)
        driver.find_element(By.NAME,"lastName").send_keys("Kirana") # isi lastname
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space").click()
        time.sleep(2)
 
    def test_a_Failed_add_employee(self):
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
        driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3) > a").click()
        time.sleep(1)
        response_data = driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--visited > a").text
        self.assertEqual('Add Employee', response_data)
        time.sleep(2)

        # step Input employee
        driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space").click()
        time.sleep(2)

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(1) > div.oxd-grid-1.orangehrm-full-width-grid > div > div > div.--name-grouped-field > div:nth-child(1) > span").text
        self.assertEqual(response_data, "Required")
        response_data = driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(1) > div.oxd-grid-1.orangehrm-full-width-grid > div > div > div.--name-grouped-field > div:nth-child(3) > span").text
        self.assertEqual(response_data, "Required")
        time.sleep(3)

    def test_a_cancel_add_employee(self):
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
        driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a > span").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3) > a").click()
        time.sleep(1)
        response_data = driver.find_element(By.CSS_SELECTOR,"#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--visited > a").text
        self.assertEqual('Add Employee', response_data)
        time.sleep(2)

        # step Input employee
        driver.find_element(By.NAME,"firstName").send_keys("Dinda") # isi firstname
        time.sleep(1)
        driver.find_element(By.NAME,"lastName").send_keys("Kirana") # isi lastname
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--ghost").click()
        time.sleep(2)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()