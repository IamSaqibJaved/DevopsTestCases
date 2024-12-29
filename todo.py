from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up headless Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=options)

# Test Case 1: User Registration (Sign Up)
def test_user_signup():
    driver.get("http://localhost/todo/newuser.php")  # Replace with your signup page URL
    driver.find_element(By.NAME, "username").send_keys("testuser")  # Test username
    driver.find_element(By.NAME, "password1").send_keys("Test1234")  # Test password
    driver.find_element(By.NAME, "password2").send_keys("Test1234")  # Confirm password
    driver.find_element(By.NAME, "captcha").send_keys("ABCDE")  # Replace with captcha if needed
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()  # Submit the form
    time.sleep(2)
    assert "Welcome" in driver.page_source  # Check for a success message
    print("Sign up test passed!")

# Test Case 2: User Login
def test_user_login():
    driver.get("http://localhost/todo/login.php")  # Replace with your login page URL
    driver.find_element(By.NAME, "username").send_keys("testuser")  # Test username
    driver.find_element(By.NAME, "password").send_keys("Test1234")  # Test password
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()  # Submit the form
    time.sleep(2)
    assert "My Todos" in driver.page_source  # Check for the 'My Todos' link or another element visible after login
    print("Login test passed!")

# Test Case 3: Add Task
def test_add_task():
    driver.get("http://localhost/todo.php")  # Replace with your todo page URL
    driver.find_element(By.NAME, "description").send_keys("Test Task")  # Task description
    driver.find_element(By.NAME, "addtask").click()  # Submit the form
    time.sleep(2)
    assert "Test Task" in driver.page_source  # Check if the task is added
    print("Add task test passed!")

# Test Case 4: Update Task
def test_update_task():
    driver.get("http://localhost/todo.php")  # Replace with your todo page URL
    driver.find_element(By.NAME, "check_list[]").click()  # Assuming the task has a checkbox to mark it as done
    driver.find_element(By.NAME, "Save").click()  # Save the task
    time.sleep(2)
    assert "Test Task" in driver.page_source  # Verify if the task is updated
    print("Update task test passed!")

# Test Case 5: Delete Task
def test_delete_task():
    driver.get("http://localhost/todo.php")  # Replace with your todo page URL
    driver.find_element(By.NAME, "check_list[]").click()  # Select task to delete
    driver.find_element(By.NAME, "Delete").click()  # Click delete
    time.sleep(2)
    assert "Test Task" not in driver.page_source  # Verify if the task is deleted
    print("Delete task test passed!")

# Test Case 6: Change Password
def test_change_password():
    driver.get("http://localhost/changepassword.php")  # Replace with your change password page URL
    driver.find_element(By.NAME, "oldpass").send_keys("Test1234")  # Old password
    driver.find_element(By.NAME, "newpass").send_keys("NewPass1234")  # New password
    driver.find_element(By.NAME, "change").click()  # Submit the form
    time.sleep(2)
    assert "Password Updated" in driver.page_source  # Verify success message
    print("Change password test passed!")

# Test Case 7: Delete Account
def test_delete_account():
    driver.get("http://localhost/deleteaccount.php")  # Replace with your delete account page URL
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()  # Click to delete account
    time.sleep(2)
    assert "Account Deleted" in driver.page_source  # Verify success message
    print("Delete account test passed!")

# Test Case 8: Check Logged-in User
def test_logged_in_user():
    driver.get("http://localhost/todo.php")  # Replace with your todo page URL
    assert "Welcome" in driver.page_source  # Ensure the user is logged in (check for welcome message)
    print("Logged in user test passed!")

# Test Case 9: View Tasks
def test_view_tasks():
    driver.get("http://localhost/todo.php")  # Replace with your todo page URL
    task_list = driver.find_elements(By.NAME, "check_list[]")  # Find all tasks
    assert len(task_list) > 0  # Ensure that tasks exist
    print("View tasks test passed!")

# Test Case 10: Logout
def test_logout():
    driver.get("http://localhost/logout.php")  # Replace with your logout page URL
    time.sleep(2)
    assert "Login" in driver.page_source  # Check if user is redirected to login page
    print("Logout test passed!")

# Run all tests
def run_tests():
    test_user_signup()
    test_user_login()
    test_add_task()
    test_update_task()
    test_delete_task()
    test_change_password()
    test_delete_account()
    test_logged_in_user()
    test_view_tasks()
    test_logout()
    driver.quit()  # Close the browser once tests are completed

# Run the tests
if __name__ == "__main__":
    run_tests()
