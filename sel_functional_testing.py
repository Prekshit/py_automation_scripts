from selenium import webdriver

# Create a webdriver instance
driver = webdriver.Firefox()

# Navigate to the website
driver.get("http://www.example.com")

# Find the search bar element and enter a search term
search_bar = driver.find_element_by_id("search_bar")
search_bar.send_keys("example search term")
search_bar.submit()

# Check the page title to see if the search was successful
assert "Example Search Results" in driver.title

# Close the browser window
driver.quit()
