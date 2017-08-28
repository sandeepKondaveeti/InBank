import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AutomationInBank(unittest.TestCase):

    def runTest(self):
        # create a new Firefox session
        driver = webdriver.Chrome("C:\Users\skondaveeti\Downloads\chromedriver.exe")
        driver.implicitly_wait(30)
        driver.maximize_window()

        # navigate to the application home page
        driver.get("http://demo.testfire.net/default.aspx")

        # testCase1:  Entering value in to the text box and after submitting, verifying whether it actually searched
        # or not.

        # get the search textbox
        search_field = driver.find_element_by_id("txtSearch")
        search_field.clear()
        # enter search keyword and submit
        search_field.send_keys("test")
        search_field.submit()

        # get the list of elements which are displayed after the search

        # currently on result page using find_elements_by_class_name  method
        lists = driver.find_elements_by_class_name("_Rm")

        # get the number of elements found
        print ("Found " + str(len(lists)) + "searches:")
        search_message = driver.find_element_by_id("_ctl0__ctl0_Content_Main_lblSearch").text
        search_expected_message = "test"
        print search_message
        self.assertEqual(search_message,search_expected_message, "Unable to search for the given text")
        time.sleep(1)

        #testCase 2: Trying to login with empty credentials and verifying the error message is displayed or not.
        #login page
        login_page = driver.find_element_by_id("_ctl0__ctl0_Content_AccountLink")
        login_page.click()
        driver.find_element_by_name("btnSubmit").click()
        time.sleep(1)
        alert_text = driver.switch_to_alert()
        print alert_text.text
        self.assertEqual(alert_text.text,"You must enter a valid username", "Abe to take empty credentials")
        alert_text.accept()
        time.sleep(2)

        #testCase 3: Trying to login with invalid credentials and verifying the error message is displayed or not.
        username = driver.find_element_by_id("uid")
        password = driver.find_element_by_id("passw")

        username.send_keys("YourUsername")
        password.send_keys("Pa55worD")

        driver.find_element_by_name("btnSubmit").click()
        expected_message = "Login Failed: We're sorry, but this username was not found in our system. Please try again."
        message_id = "_ctl0__ctl0_Content_Main_message"
        actual_message = driver.find_element_by_id(message_id).text
        print actual_message
        self.assertEqual(actual_message,expected_message,msg= "Able to Login with invalid credentials.")

        # close the browser window
        driver.quit()

if __name__ == '__main__':
    obj = AutomationInBank()
    obj.runTest()