from behave.__main__ import main as bh_main
import sys
import os
import yaml

with open("runner_config.yml","r") as file:
    data = yaml.safe_load(file)
    tags = data['config_data']['tags']
    feature_path = data['config_data']['feature_path']
    


sys.path.insert(0, os.path.abspath(f"{feature_path}"))
bh_main(f'{feature_path} -t {tags}')