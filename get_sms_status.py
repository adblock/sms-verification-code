#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import requests
import json

def get_status():
    url = 'https://oapi.dingtalk.com/robot/send?access_token=5adb0ed002a46761df517eacee2a99ba285c613891adf110255bce2ea326a047'

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
