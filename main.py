import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_autoinstaller

# Install ChromeDriver
chromedriver_autoinstaller.install()

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Streamlit app
st.title("Selenium with Streamlit")
st.write("This is a Streamlit app using Selenium.")

# Example Selenium interaction
driver.get("https://www.google.com/")
title = driver.title
st.write(f"Title of the page: {title}")

driver.quit()
