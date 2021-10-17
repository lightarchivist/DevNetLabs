""" parse YAML file simple example """
import yaml

with open ("data.yaml", "r", encoding = "UTF-8") as fdata:
    ydata = yaml.safe_load(fdata)
    print(fdata)
