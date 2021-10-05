#!/usr/bin/env python
""" parse json """
import json
with open("data_2.json", "r") as file:
    print(json.load(file.read()))
