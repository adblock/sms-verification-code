#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import sys
import requests
import json
import time

def sendmessage(argv):
    # 短信标记 只转发包含以下字段的短信
    signs = [
                "验证码",
                "【阿里巴巴】",
                "【京东】",
                "【京东咚咚】",
                "【京东商家后台】",
                "【京麦工作台】",
                "京东服务市场",
                "【微博】",
                "【支付宝】",
                "【淘宝网】",
                "【今日头条】",
                "【阿里巴巴钉钉】",
                "【阿里妈妈】"
            ]

    # 钉钉机器人地址
    URLs = {
                '6987': ['https://oapi.dingtalk.com/robot/send?access_token=bcc01fc3ec0ef36c9adae04dbc874baf981fc7a766c2860d3e0ea7e9c6a72f08'],
                '6910': ['https://oapi.dingtalk.com/robot/send?access_token=bcc01fc3ec0ef36c9adae04dbc874baf981fc7a766c2860d3e0ea7e9c6a72f08'],
                '6912': ['https://oapi.dingtalk.com/robot/send?access_token=bcc01fc3ec0ef36c9adae04dbc874baf981fc7a766c2860d3e0ea7e9c6a72f08'],
                '6913': ['https://oapi.dingtalk.com/robot/send?access_token=bcc01fc3ec0ef36c9adae04dbc874baf981fc7a766c2860d3e0ea7e9c6a72f08'],
                '5650': [
                    'https://oapi.dingtalk.com/robot/send?access_token=e26fd938d2ac477e0d9cf0f61bc108a86f271002f4600edcaabb6ba6e345b6b4',
                    'https://oapi.dingtalk.com/robot/send?access_token=764a749c0bd635de1f4d17afffaad30e037dd954f54ebee223df26bbfbb7f369'
                    ]
            }
    try:
        # 发送结果
        send_result = []
        # 手机尾号
        phone_num = sys.argv[1]
        # 尾号对应的地址
        urls = URLs[phone_num]
        # 短信页数
        numparts = int(os.environ['DECODED_PARTS'])
        # 短信内容
        message = ''
        # 短信页判断
        if numparts == 0:
            message = os.environ['SMS_1_TEXT']
        else:
            for i in range(0, numparts):
                varname = 'DECODED_%d_TEXT' % i
                if varname in os.environ:
                    message = message + os.environ[varname]
        # 判断短信标记
        for sign in signs:
            if sign in message:

                # 屏蔽京东用户名
                replace_start = message.find('用户')
                replace_end = message.find(',')
                if replace_start != -1 and replace_end != -1:
                    message = message[:replace_start + 2] + '*****' + message[replace_end:]

                string_text = {
                    "msgtype": "markdown",
                    "markdown": {
                        "title": '尾号' + phone_num + ':',
                        "text": "#### 尾号 " + phone_num + ": \n" +
                            '>' + message + ' \n' + 
                            '>>' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        }
                }
                string_text = json.dumps(string_text)
                for url in urls:
                    res = requests.post(
                        url,
                        data=string_text,
                        headers={"Content-Type": "application/json ;charset=utf-8 "}
                    )
                    send_result.append(res)
                break
        else:
            print('do not send')
    except Exception as e:
        print(e)
    else:
        print(send_result)

if __name__ == '__main__':
    sendmessage(sys.argv)
