#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: UTF-8 -*-

from send import send
import json
from jsonschema import validate

site = [1,2,4]
url = ("http://api.uat.chunbo.com:90/CookbookHome/getTopicList")
body = {'Page':'1','pagesize':'10'}
schema = {
  "$schema": "http://api.uat.chunbo.com:90/CookbookHome/getTopicList#",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "subTitle": {
      "type": "string"
    },
    "list": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string"
          },
          "desc": {
            "type": "string"
          },
          "cookbook_id": {
            "type": "string"
          },
          "display_name": {
            "type": "string"
          },
          "url": {
            "type": "string"
          },
          "pic_url": {
            "type": "string"
          },
          "chef_name": {
            "type": "string"
          },
          "chef_img": {
            "type": "string"
          },
          "chef_url": {
            "type": "string"
          },
          "iscollect": {
            "type": "string"
          }
        },
        "required": [
          "type",
          "desc",
          "cookbook_id",
          "display_name",
          "url",
          "pic_url",
          "chef_name",
          "chef_img",
          "chef_url",
          "iscollect"
        ]
      }
    },
    "flag": {
      "type": "integer"
    }
  },
  "required": [
    "title",
    "subTitle",
    "list",
    "flag"
  ]
}
for x in site:
   Headers={"siteid":"%s"%x,"resoursrverion":"2.7.0"}
   # print(json.dumps(body))
   # print(Headers)
   result = send(url,Headers,body)
   try:
       validate(result,schema)
   except validationError as v:
       print("validate 站点",x," failed",v)
   else:
       print("validete 站点",x,"  succed")
