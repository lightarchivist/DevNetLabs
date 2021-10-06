#!/usr/bin/env python
""" simple code to parse json """
import json
with open("data.json", "r", encoding = "UTH-8") as file:
    data = json.load(file)
    print(data)
