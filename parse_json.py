#!/usr/bin/env python
""" parse json """
import json
with open("data.json", "r") as file:
    jdata = file.read()
alldata = json.load(jdata)
