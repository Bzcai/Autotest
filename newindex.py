#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# -*- coding: UTF-8 -*-

from send import send
import json
from jsonschema import validate

site=[1,2,4]
url = "http://api.uat.chunbo.com:90/home/newindex"
body = {"member_id":"811156"}

home_schema = {
  "$schema": "api.uat.chunbo.com:90/home/newindex",
  "type": "object",
  "properties": {
    "flag": {
      "type": "integer"
    },
    "data": {
      "type": "object",
      "properties": {
        "list_focus": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": {
                "type": "string"
              },
              "pic_url": {
                "type": "string"
              },
              "link": {
                "type": "string"
              },
              "link_type": {
                "type": "integer"
              },
              "pid": {
                "type": "string"
              }
            },
            "required": [
              "title",
              "pic_url",
              "link",
              "link_type",
              "pid"
            ]
          }
        },
        "list_lc": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string"
              },
              "cid": {
                "type": "string"
              },
              "parent_id": {
                "type": "string"
              },
              "basic": {
                "type": "object",
                "properties": {
                  "floor_name": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "floor_title": {
                    "type": "string"
                  },
                  "model_url": {
                    "type": "string"
                  },
                  "sub_name": {
                    "type": "string"
                  },
                  "m_title_color": {
                    "type": "string"
                  },
                  "m_title_pic": {
                    "type": "string"
                  },
                  "cid": {
                    "type": "string"
                  },
                  "parent_id": {
                    "type": "string"
                  }
                },
                "required": [
                  "floor_name",
                  "name",
                  "floor_title",
                  "model_url",
                  "sub_name",
                  "m_title_color",
                  "m_title_pic",
                  "cid",
                  "parent_id"
                ]
              },
              "banner1": {
                "type": "object",
                "properties": {
                  "pic": {
                    "type": "string"
                  },
                  "banner1_url": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  },
                  "priority": {
                    "type": "integer"
                  },
                  "pid": {
                    "type": "string"
                  },
                  "link_type": {
                    "type": "integer"
                  }
                },
                "required": [
                  "pic",
                  "banner1_url",
                  "description",
                  "priority",
                  "pid",
                  "link_type"
                ]
              },
              "list": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "product_id": {
                      "type": "integer"
                    },
                    "pid": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "shortname": {
                      "type": "string"
                    },
                    "subname": {
                      "type": "string"
                    },
                    "des": {
                      "type": "string"
                    },
                    "chunbo_price": {
                      "type": "string"
                    },
                    "promotion_price": {
                      "type": "string"
                    },
                    "discount_price": {
                      "type": "string"
                    },
                    "sku_code": {
                      "type": "string"
                    },
                    "specifications": {
                      "type": "string"
                    },
                    "promo_type": {
                      "type": "array",
                      "items": {
                        "type": "integer"
                      }
                    },
                    "stock": {
                      "type": "integer"
                    },
                    "url": {
                      "type": "string"
                    },
                    "gift_name": {
                      "type": "string"
                    },
                    "is_stock": {
                      "type": "integer"
                    },
                    "market_price": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "product_id",
                    "pid",
                    "name",
                    "title",
                    "shortname",
                    "subname",
                    "des",
                    "chunbo_price",
                    "promotion_price",
                    "discount_price",
                    "sku_code",
                    "specifications",
                    "promo_type",
                    "stock",
                    "url",
                    "gift_name",
                    "is_stock",
                    "market_price"
                  ]
                }
              }
            },
            "required": [
              "name",
              "cid",
              "parent_id",
              "basic",
              "banner1",
              "list"
            ]
          }
        },
        "urlProductImage": {
          "type": "object",
          "properties": {
            "hotsales": {
              "type": "string"
            },
            "hotsales_link": {
              "type": "string"
            },
            "newproduct": {
              "type": "string"
            },
            "newproduct_link": {
              "type": "string"
            },
            "dailyFood": {
              "type": "string"
            },
            "dailyFood_link": {
              "type": "string"
            },
            "today_eat": {
              "type": "string"
            },
            "today_eat_link": {
              "type": "string"
            },
            "is_cache_hotsales": {
              "type": "string"
            },
            "chunboStandard": {
              "type": "null"
            },
            "alliance": {
              "type": "null"
            },
            "chunboing": {
              "type": "null"
            }
          },
          "required": [
            "hotsales",
            "hotsales_link",
            "newproduct",
            "newproduct_link",
            "dailyFood",
            "dailyFood_link",
            "today_eat",
            "today_eat_link",
            "is_cache_hotsales",
            "chunboStandard",
            "alliance",
            "chunboing"
          ]
        },
        "daliy_cook": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "link": {
                "type": "string"
              },
              "pid": {
                "type": "string"
              }
            },
            "required": [
              "link",
              "pid"
            ]
          }
        },
        "best_recommend": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "product_id": {
                "type": "integer"
              },
              "pid": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "shortname": {
                "type": "string"
              },
              "subname": {
                "type": "string"
              },
              "des": {
                "type": "string"
              },
              "chunbo_price": {
                "type": "string"
              },
              "promotion_price": {
                "type": "string"
              },
              "discount_price": {
                "type": "string"
              },
              "sku_code": {
                "type": "string"
              },
              "specifications": {
                "type": "string"
              },
              "promo_type": {
                "type": "array",
                "items": {
                  "type": "integer"
                }
              },
              "stock": {
                "type": "integer"
              },
              "url": {
                "type": "string"
              },
              "gift_name": {
                "type": "string"
              },
              "is_stock": {
                "type": "integer"
              },
              "market_price": {
                "type": "string"
              }
            },
            "required": [
              "product_id",
              "pid",
              "name",
              "title",
              "shortname",
              "subname",
              "des",
              "chunbo_price",
              "promotion_price",
              "discount_price",
              "sku_code",
              "specifications",
              "promo_type",
              "stock",
              "url",
              "gift_name",
              "is_stock",
              "market_price"
            ]
          }
        },
        "roll_list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "product_list": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "product_id": {
                      "type": "integer"
                    },
                    "pid": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "shortname": {
                      "type": "string"
                    },
                    "subname": {
                      "type": "string"
                    },
                    "des": {
                      "type": "string"
                    },
                    "chunbo_price": {
                      "type": "string"
                    },
                    "promotion_price": {
                      "type": "string"
                    },
                    "discount_price": {
                      "type": "string"
                    },
                    "sku_code": {
                      "type": "string"
                    },
                    "specifications": {
                      "type": "string"
                    },
                    "promo_type": {
                      "type": "array",
                      "items": {
                        "type": "integer"
                      }
                    },
                    "stock": {
                      "type": "integer"
                    },
                    "url": {
                      "type": "string"
                    },
                    "gift_name": {
                      "type": "string"
                    },
                    "is_stock": {
                      "type": "integer"
                    },
                    "market_price": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "product_id",
                    "pid",
                    "name",
                    "title",
                    "shortname",
                    "subname",
                    "des",
                    "chunbo_price",
                    "promotion_price",
                    "discount_price",
                    "sku_code",
                    "specifications",
                    "promo_type",
                    "stock",
                    "url",
                    "gift_name",
                    "is_stock",
                    "market_price"
                  ]
                }
              },
              "title": {
                "type": "string"
              },
              "sub_title": {
                "type": "string"
              },
              "more_link": {
                "type": "string"
              }
            },
            "required": [
              "product_list",
              "title",
              "sub_title",
              "more_link"
            ]
          }
        },
        "banner_list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "image_url": {
                "type": "string"
              },
              "link": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "button_text": {
                "type": "string"
              },
              "next_page_title": {
                "type": "string"
              },
              "timestamp": {
                "type": "string"
              },
              "is_flot": {
                "type": "string"
              },
              "is_https": {
                "type": "string"
              }
            },
            "required": [
              "image_url",
              "link",
              "title",
              "button_text",
              "next_page_title",
              "timestamp",
              "is_flot",
              "is_https"
            ]
          }
        },
        "new_banner_list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "timestamp": {
                "type": "string"
              },
              "image_url": {
                "type": "string"
              },
              "link": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "button_text": {
                "type": "null"
              },
              "is_flot": {
                "type": "string"
              },
              "not_close": {
                "type": "integer"
              }
            },
            "required": [
              "timestamp",
              "image_url",
              "link",
              "title",
              "button_text",
              "is_flot",
              "not_close"
            ]
          }
        },
        "newest_goods_url": {
          "type": "string"
        },
        "top_sale_goods_url": {
          "type": "string"
        },
        "top_banner_list": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "link": {
                "type": "string"
              },
              "image": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "isShow": {
                "type": "integer"
              }
            },
            "required": [
              "link",
              "image",
              "title",
              "isShow"
            ]
          }
        }
      },
      "required": [
        "list_focus",
        "list_lc",
        "urlProductImage",
        "daliy_cook",
        "best_recommend",
        "roll_list",
        "banner_list",
        "new_banner_list",
        "newest_goods_url",
        "top_sale_goods_url",
        "top_banner_list"
      ]
    },
    "etag": {
      "type": "string"
    }
  },
  "required": [
    "flag",
    "data",
    "etag"
  ]
}


for x in site:
    Headers = {'siteid':'%s'%x,'resoursrverion':'2.7.1'}
    result = send(url,Headers,body)
    try:
        validate(result,home_schema)
    except:
        print('站点',x,'校验失败')
    else:
        print('站点',x,'校验成功')