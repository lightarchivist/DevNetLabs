#!/usr/bin/env python
""" parse json """
import json
with open("data.json", "r") as file:
    print(json.load(file.read()))
