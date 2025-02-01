from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time

INITIAL_WEBPAGE = "https://www.linkedin.com/login"

class Linkedin:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(INITIAL_WEBPAGE)


    def login(self,login_email,login_password):
        username = self.wait.until(ec.presence_of_element_located((By.ID, "username")))
        username.send_keys(login_email)
        password = self.wait.until(ec.presence_of_element_located((By.ID, "password")))
        password.send_keys(login_password)
        signin = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"button[type='submit']")))
        signin.click()
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,"input[type='text']")))
        time.sleep(1)
        #will add feature to pass security check
        print("Login is successful")

    def search_for_jobs(self,job_description,location):
        search_input = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                                "input[type='text']")))
        search_input.send_keys(job_description)
        search_input.send_keys(Keys.ENTER)
        time.sleep(0.5)
        jobs_button = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                'li[class="search-reusables__primary-filter"] button')))
        jobs_button.click()
        time.sleep(0.5)
        location_input = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                        'input[id*="jobs-search-box-location"]')))
        location_input.send_keys(Keys.LEFT_CONTROL + "A")
        location_input.send_keys(Keys.BACKSPACE)
        location_input.send_keys(location)
        time.sleep(0.2)
        search_button = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                        'button[class*="jobs-search-box__submit-button"]')))
        search_button.click()
        time.sleep(1)
        easy_apply_button = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                            'button[id="searchFilter_applyWithLinkedin"]')))
        easy_apply_button.click()
        time.sleep(0.5)
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                    'div[class="scaffold-layout__list "')))
        time.sleep(1)
        print("Search is successful")

    def jobs_in_current_page(self):
        job_list = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                'div[class*="JFejZbOQJSnTiDbFsNTjartqbrZdYyaQqPM"')))
        total_height = self.driver.execute_script("return arguments[0].scrollHeight", job_list)

        scroll_height = 200
        current_position = 0

        while current_position < total_height:
            current_position += scroll_height
            self.driver.execute_script(
                f"arguments[0].scrollTop = {current_position}", job_list
            )

            time.sleep(0.25)

            total_height = self.driver.execute_script("return arguments[0].scrollHeight", job_list)

        time.sleep(0.5)
        jobs_in_current_page = self.wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                        'div[class*="job-card-container--clickable"')))
        return jobs_in_current_page

    def job_applier(self):
        jobs_in_current_page = self.jobs_in_current_page()
        for index in range(len(jobs_in_current_page)):
            jobs_in_current_page[index].click()
            time.sleep(0.5)
            # will be developed with help of AI model to complete surveys.
            ## only saving the easy apply jobs in the first page for now
            save_button = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                    'button[class*="save"]')))
            save_button.click()
            time.sleep(1)

        print("Job apply(save) is successful")





