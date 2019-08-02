#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import requests
import json

def get_status():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=f8c7073ed5bef85b7ae86fff35fe6915266f26bb0d0f3de614d58f928a14df47'

    str = ""

    str = str + os.popen('gammu --identify').read()
    str = str + os.popen('gammu -s 1 --identify').read()
    str = str + os.popen('gammu -s 2 --identify').read()
    str = str + os.popen('gammu -s 3 --identify').read()

    str = str + "\n"

    str = str + os.popen('gammu-detect').read()

    print(str)
    string_text = {
        "msgtype": "text",
        "text": {
            "content": str
        }
    }
    string_text = json.dumps(string_text)
    res = requests.post(
        url,
        data = string_text,
        headers = {"Content-Type": "application/json ;charset=utf-8 "}
    )
    print(res)

if __name__ == '__main__':
    get_status()
