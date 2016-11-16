#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: UTF-8 -*-

from send import send
import json
from jsonschema import validate

site = [1,2,4]
url = ("http://api.uat.chunbo.com:90/CookbookHome/getCookbookIndex")
body = {'Page':'1','pagesize':'10'}
schema = {
  "$schema": "http://api.uat.chunbo.com:90/CookbookHome/getCookbookIndex#",
  "type": "object",
  "properties": {
    "flag": {
      "type": "integer"
    },
    "list_focus": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "link": {
            "type": "string"
          },
          "pic_url": {
            "type": "string"
          },
          "link_type": {
            "type": "integer"
          },
          "pid": {
            "type": "integer"
          },
          "cookbook_id": {
            "type": "string"
          }
        },
        "required": [
          "title",
          "link",
          "pic_url",
          "link_type",
          "pid",
          "cookbook_id"
        ]
      }
    },
    "category": {
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
              "category_id": {
                "type": "string"
              },
              "pic_url": {
                "type": "string"
              }
            },
            "required": [
              "category_id",
              "pic_url"
            ]
          }
        }
      },
      "required": [
        "title",
        "subTitle",
        "list"
      ]
    },
    "chef": {
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
              "name": {
                "type": "string"
              },
              "pic_url": {
                "type": "string"
              },
              "summary": {
                "type": "string"
              },
              "url": {
                "type": "string"
              }
            },
            "required": [
              "name",
              "pic_url",
              "summary",
              "url"
            ]
          }
        }
      },
      "required": [
        "title",
        "subTitle",
        "list"
      ]
    }
  },
  "required": [
    "flag",
    "list_focus",
    "category",
    "chef"
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
       print("灵感首页 站点",x," 校验失败",v)
   else:
       print("灵感首页 站点",x,"  数据正常")
