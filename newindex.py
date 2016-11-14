#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: UTF-8 -*-

from send import send
import json
from jsonschema import validate

URL = "http://api.uat.chunbo.com:90/home/newindex"
Header= {"siteid":"1"}
Form = {"member_id":"811156"}

print (send(URL,Header,Form))
