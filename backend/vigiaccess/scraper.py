"""

VigiAccess scraper using Selenium. Only tested with Chrome, so we recommend you leverage Google Chrome.

Please ensure to have a folder called selenium with the the chromedriver executable inside for this to work.

"""

import json
import os
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

CHROMEDRIVER_EXECUTABLE: str = 'chromedriver.exe'  # Change this depending on what your executable is called.
DRIVER_PATH: str = os.path.join(os.getcwd(), 'selenium', CHROMEDRIVER_EXECUTABLE)

URL: str = "http://www.vigiaccess.org/"
DRIVER: WebDriver = webdriver.Chrome(DRIVER_PATH)
WAIT_TIME: int = 10


def dump_to_json(data: Dict[str, List[str]], path: str):
    """
    Dump data provided in JSON format to the path provided.
    :param data: Data to dump.
    :param path: Where to dump data.
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def scrape_adr(drug: str):
    """
    Scrape adverse drug reactions information.
    """
    # Get the ADRs accordion element and then click it.
    adr_category_element = DRIVER.find_element_by_xpath("//span[@class='ng-scope' and contains(text(), 'ADR')]")
    adr_category_element.click()

    # Wait until the ADRs section expands.
    WebDriverWait(DRIVER, WAIT_TIME).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//div[@class='panel-collapse collapse in']"))
    )

    data = {}
    disorder_categories = DRIVER.find_elements_by_xpath("//li[@class='a2 ng-scope tree-collapsed']")
    for disorder_category in disorder_categories:
        arrow = disorder_category.find_element_by_tag_name('i')
        arrow.click()

        WebDriverWait(DRIVER, WAIT_TIME).until(
            # Wait until the spinner hides. This guarantees the accordion has loaded.
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//div[@class='spinner ng-hide']"))
        )

        category, *disorders = disorder_category.find_elements_by_tag_name("span")
        data[category.text] = [disorder.text for disorder in disorders]
        arrow.click()  # Close this accordion.

    dump_to_json(data, path=f'{drug}.json')


def scrape(drug: str):
    """
    Initiate scraping through VigiAccess.
    :param drug: Drug to scrape from VigiAccess.
    """
    # Launch the website.
    DRIVER.get(URL)

    # Wait until the tick box appears.
    tick_box = WebDriverWait(DRIVER, WAIT_TIME).until(
        expected_conditions.presence_of_element_located((By.ID, "acceptTermsCheckBox"))
    )

    # Click the tick box once it appears.
    tick_box.click()

    # Click the submit button and enter the query view.
    DRIVER.find_element_by_tag_name('button').click()

    # Wait until the query view loads.
    search_bar = WebDriverWait(DRIVER, WAIT_TIME).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//input[@type='search']"))
    )

    # Type in the drug provided to the search query.
    search_bar.send_keys(drug + Keys.RETURN)

    # Wait for the drug information to load.
    WebDriverWait(DRIVER, WAIT_TIME).until(  # Wait until the spinner hides. This guarantees the accordion has loaded.
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//div[@class='spinner ng-hide']"))
    )

    # Initiate scraping ADR information.
    scrape_adr(drug)


def main():
    """
    Main driver function.
    """
    scrape("paracetamol")


if __name__ == '__main__':
    main()
