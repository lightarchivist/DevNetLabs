#!/usr/bin/env python
# parse json script
import json
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
