from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, JavascriptException
import time

class RestaurantLayoutTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_service = ChromeService(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=chrome_service)
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        # Navigate directly to the restaurant layout page
        self.driver.get(f"{self.live_server_url}/restaurant-layout/")
        
        try:
            # Wait for Konva to load and initialize
            self.wait.until(
                EC.presence_of_element_located((By.ID, "stage-container"))
            )
            # Wait for table editor to be ready
            self.wait.until(
                EC.presence_of_element_located((By.ID, "table-editor"))
            )
            time.sleep(2)  # Additional time for JavaScript to fully initialize
        except TimeoutException:
            self.fail("Restaurant layout page failed to load in time")

    def get_table_shapes(self):
        """Safely retrieve table shapes using a simplified JavaScript approach."""
        try:
            return self.driver.execute_script("""
                if (typeof Konva === 'undefined' || !Konva.stages || Konva.stages.length === 0) {
                    return [];
                }
                
                const stage = Konva.stages[0];
                const layer = stage.getLayers()[0];
                
                // Use pure data extraction to avoid circular references
                return layer.getChildren()
                    .filter(node => node.attrs.width !== undefined || node.attrs.radius !== undefined)
                    .map(node => ({
                        width: node.attrs.width,
                        radius: node.attrs.radius,
                        x: node.attrs.x,
                        y: node.attrs.y
                    }));
            """)
        except JavascriptException as e:
            print(f"JavaScript error: {e}")
            return []

    def test_layout_page_loads_correctly(self):
        """Verify the Restaurant Layout page loads with all expected elements."""
        try:
            # Check key elements are present
            stage_container = self.wait.until(
                EC.presence_of_element_located((By.ID, "stage-container"))
            )
            self.assertTrue(stage_container, "Stage container should be present")
            
            table_editor = self.driver.find_element(By.ID, "table-editor")
            self.assertTrue(table_editor, "Table editor panel should be present")
            
            tooltip = self.driver.find_element(By.ID, "tooltip")
            self.assertTrue(tooltip, "Tooltip element should be present")
        except (TimeoutException, NoSuchElementException) as e:
            self.fail(f"Failed to find expected page elements: {str(e)}")

    def test_table_selection_and_editing(self):
        """Test selecting a table and editing its details."""
        try:
            # Wait for tables to be available
            table_shapes = self.get_table_shapes()
            
            # Verify tables exist
            self.assertTrue(len(table_shapes) > 0, "No tables found on the layout")
            
            # Click first table via JavaScript
            self.driver.execute_script("""
                const stage = Konva.stages[0];
                const layer = stage.getLayers()[0];
                const firstTable = layer.getChildren()
                    .find(node => node.attrs.width !== undefined || node.attrs.radius !== undefined);
                
                if (firstTable) {
                    firstTable.fire('click');
                }
            """)
            
            # Wait for editing controls to be ready
            status_dropdown = self.wait.until(
                EC.presence_of_element_located((By.ID, "table-status"))
            )
            
            # Change table status
            guests_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "table-guests"))
            )
            waiter_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "table-waiter"))
            )

            # Select 'occupied' status
            for option in status_dropdown.find_elements(By.TAG_NAME, "option"):
                if option.get_attribute("value") == "occupied":
                    option.click()
                    break
            
            # Update guests and waiter
            guests_input.clear()
            guests_input.send_keys("4")
            
            waiter_input.clear()
            waiter_input.send_keys("John")

            # Update table
            update_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Update Table']"))
            )
            update_button.click()
            
            time.sleep(1)
        except Exception as e:
            self.fail(f"Table selection and editing failed: {str(e)}")

    def test_table_timer_functionality(self):
        """Test the timer functionality for tables."""
        try:
            # Click first table via JavaScript
            self.driver.execute_script("""
                const stage = Konva.stages[0];
                const layer = stage.getLayers()[0];
                const firstTable = layer.getChildren()
                    .find(node => node.attrs.width !== undefined || node.attrs.radius !== undefined);
                
                if (firstTable) {
                    firstTable.fire('click');
                }
            """)
            
            # Wait for timer buttons to be clickable
            start_timer_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Start Timer')]"))
            )
            start_timer_button.click()
            
            # Wait a few seconds
            time.sleep(3)
            
            # Reset timer
            reset_timer_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reset Timer')]"))
            )
            reset_timer_button.click()
            
            time.sleep(1)
        except Exception as e:
            self.fail(f"Table timer functionality failed: {str(e)}")

    def test_tooltip_hover_functionality(self):
        """Test that tooltips appear and disappear correctly when hovering over tables."""
        try:
            # Get table shapes
            table_shapes = self.get_table_shapes()
        
            # Verify tables exist
            self.assertTrue(len(table_shapes) > 0, "No tables found on the layout")
        
            # Simulate hover over tables
            for _ in range(min(3, len(table_shapes))):
                # Trigger hover via JavaScript
                self.driver.execute_script("""
                    const stage = Konva.stages[0]; // Ensure this is the correct stage
                    const layer = stage.getLayers()[0];
                    const firstTable = layer.getChildren()
                        .find(node => node.attrs.width !== undefined || node.attrs.radius !== undefined);
                
                    console.log("Hovering over table:", firstTable);  // Log for debugging
                
                    if (firstTable) {
                        firstTable.fire('mouseenter');
                    }
                """)
            
                # Add a wait time to ensure tooltip has time to appear
                time.sleep(1)  # Wait for tooltip to appear
            
                # Wait for tooltip to appear and ensure it becomes visible
                tooltip = self.wait.until(
                    EC.visibility_of_element_located((By.ID, "tooltip"))
                )
            
                # Check tooltip visibility and content
                self.assertTrue(tooltip.is_displayed(), "Tooltip should be visible")
                tooltip_text = tooltip.text
                print(f"Tooltip content: {tooltip_text}")  # Log tooltip content
            
                # Check for expected content
                expected_fields = ["Seats:", "Guests:", "Status:"]
                for field in expected_fields:
                    self.assertIn(field, tooltip_text, f"Tooltip should contain {field}")
            
                # Remove hover
                self.driver.execute_script("""
                    const stage = Konva.stages[0];
                    const layer = stage.getLayers()[0];
                    const firstTable = layer.getChildren()
                        .find(node => node.attrs.width !== undefined || node.attrs.radius !== undefined);
                
                    console.log("Removing hover from table:", firstTable);  // Log for debugging
                
                    if (firstTable) {
                        firstTable.fire('mouseleave');
                    }
                """)
            
                time.sleep(1)  # Wait a moment after removing hover
        except Exception as e:
            self.fail(f"Tooltip hover functionality failed: {str(e)}")