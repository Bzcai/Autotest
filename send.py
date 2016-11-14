#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: UTF-8 -*-

import requests

def send(URL,Header,Form):
    result = requests.post(URL,headers=Header,data=Form)
    return result.json()
