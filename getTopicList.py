#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: UTF-8 -*-



schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
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
