import streamlit as st
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@st.experimental_singleton
def install_geckodriver():
    os.system('sbase install geckodriver')
    os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

_ = install_geckodriver()

opts = Options()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

browser.get('http://example.com')
st.write(browser.page_source)
