from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class WebAppTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_service = ChromeService(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=chrome_service)
        cls.driver.implicitly_wait(10)  # Set implicit wait for elements

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Close the browser after all tests
        super().tearDownClass()

    def test_navbar_navagation(self):
        """Test that all key pages render sequentially by clicking through the navbar."""
    
        # Step 1: Start at the Home page
        self.driver.get(f"{self.live_server_url}/")
        time.sleep(1)  # Ensure the page loads fully
    
        # Step 2: Define the sequence of navigation
        navigation_sequence = [
            {"link_text": "About", "url": "/about/", "content": "About"},
            {"link_text": "Menu", "url": "/menu/", "content": "Menu"},
            {"link_text": "Restaurant", "url": "/restaurant/", "content": "Restaurant"},
            {"link_text": "Table", "url": "/table/", "content": "Table"},
            {"link_text": "Layout", "url": "/restaurant-layout/", "content": "Layout"},
        ]
    
        # Step 3: Start navigation sequence
        for page in navigation_sequence:
            with self.subTest(page=page):
                # Click the navbar link
                nav_link = self.driver.find_element(By.LINK_TEXT, page["link_text"])
                nav_link.click()
                time.sleep(2)  # Wait for the page to load
            
                # Verify the URL matches the expected page
                self.assertIn(
                    f"{self.live_server_url}{page['url']}",
                    self.driver.current_url,
                    f"URL should redirect to {page['url']} after clicking {page['link_text']}.",
                )
            
                # Verify the page contains the expected content
                self.assertIn(
                    page["content"],
                    self.driver.page_source,
                    f"Page should contain '{page['content']}' after clicking {page['link_text']}.",
                )


    def test_user_signup_logout_and_login(self):
        """Test that a user can sign up, log out, and log in again with the same credentials."""
    
        # Step 1: Navigate to the Sign-Up page
        self.driver.get(f"{self.live_server_url}/signup/")
    
        # Fill in the sign-up form
        self.driver.find_element(By.NAME, "username").send_keys("newuser")
        self.driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        self.driver.find_element(By.NAME, "password1").send_keys("newpassword123")
        self.driver.find_element(By.NAME, "password2").send_keys("newpassword123")

        # Submit the form
        self.driver.find_element(By.NAME, "password2").send_keys(Keys.RETURN)
    
        # Wait for the success message after account creation
        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".messages p"))
        )
    
        # Check the success message
        self.assertIn(
            "Account created for user newuser", 
            success_message.text, 
            "Success message should indicate that the account was created for the user"
        )
    
        # Step 2: Log out from the navbar
        # Assuming there's a 'Log Out' button on the navbar with a link to '/logout/'
        self.driver.find_element(By.LINK_TEXT, "Log Out").click()

        # Wait for the user to be redirected to the home page
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(f"{self.live_server_url}/")
        )
    
        # Step 3: Log in with the newly created credentials
        self.driver.find_element(By.LINK_TEXT, "Log In").click()  # Click the Log In link
    
        # Fill in the login form
        self.driver.find_element(By.NAME, "username").send_keys("newuser")
        self.driver.find_element(By.NAME, "password").send_keys("newpassword123")
    
        # Submit the form
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

        # Wait for the login to complete and check redirection to the About page
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(f"{self.live_server_url}/about/") 
        )
    
        # Check that the user is redirected to the About page
        self.assertIn(f"{self.live_server_url}/about/", self.driver.current_url, "User should be redirected to the 'About' page after logging in.")
