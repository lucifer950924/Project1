import os
from datetime import datetime as dt




def take_screenshot(driver):
    now = dt.now().strftime("%Y%m%d%H%M%S")
    curr_wd = os.getcwd()
    sc_dir = os.path.join(curr_wd,"Screenshots")
    sc_filepath = os.path.join(sc_dir,f"SC_{now}.png")
    driver.save_screenshot(sc_filepath)