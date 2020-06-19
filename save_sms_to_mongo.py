#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# import os
import sys
from pymongo import MongoClient

def save_sms(argv):
    try:
        client = MongoClient('mongodb://192.168.1.210/zz_web')
        db = client.zz_web
        zz_sms = db.zz_sms
        post_id = zz_sms.insert_one(argv).inserted_id
        print(post_id)
    except Exception as e:
        print(e)
    else:
        print("test")