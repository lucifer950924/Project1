import subprocess
import os
from datetime import datetime as dt
import shutil
import yaml
import pyautogui
import snoop
import logging
from functools import wraps


now = dt.now().strftime("%Y%m%d%H%M%S")
curr_dir = os.path.join(os.getcwd(),"Results")
results_dir = os.path.join(curr_dir,f"Results_{now}")
print(results_dir)
os.makedirs(results_dir,exist_ok=True)
log_file = f"results_{now}.html"
results_filepath = os.path.join(results_dir,log_file)
snoop.install(out=open(results_filepath,"w"))

@snoop
def runner():
    with open("runner_config.yml","r") as f:
        data = yaml.safe_load(f)

    config_data = data['config_data']


    with open("results.txt", 'w') as f:
        try:
            subprocess.run([config_data['language'],config_data['suite']],stdout=f,stderr=subprocess.STDOUT)
            sc = pyautogui.screenshot()

            screenshot_directory = os.path.join(results_dir,"Screenshots")
            os.makedirs(screenshot_directory)
            sc_filepath = os.path.join(screenshot_directory,f"sc_{now}.png")
            sc.save(sc_filepath)
            f.write(f"{config_data['suite']} ran successfully")
        except:
            f.write(f"{config_data['suite']} ran unsuccessfully")


    shutil.move("results.txt",results_dir)



runner()