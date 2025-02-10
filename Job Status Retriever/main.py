import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd


def job_status_retriever():
    
    # Get Data from CSV
    df = pd.read_csv('Adam-195/Work-Script-Automation/Job Status Retriever/jobs.csv')
    

    # Open Target Website
    driver = webdriver.Edge()
    driver.get("https://www.google.com/search?q=test1&rlz=1C1CHBF_en-GBGB931GB931&oq=test1&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIJCAMQABgKGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgkIBhAAGAoYgAQyCQgHEAAYChiABDIJCAgQABgKGIAEMgcICRAAGIAE0gEHOTI2ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")


    # Navigate on Website + wait on HTML element
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "W0wltc"))
    )
    reject_cookies = driver.find_element(By.ID, "W0wltc")
    reject_cookies.send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )
    search_element = driver.find_element(By.CLASS_NAME, "gLFyf")
    search_element.send_keys("test1" + Keys.ENTER)

    # Return Info
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "LC20lb MBeuO DKV0Md"))
    )
    result = driver.find_element(By.CLASS_NAME, "LC20lb MBeuO DKV0Md").text


    return result

    time.sleep(6)



    driver.quit()


job_status_retriever()