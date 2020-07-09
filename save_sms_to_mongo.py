#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# import os
import sys
from pymongo import MongoClient

def save_sms(argv):
    try:
        client_test = MongoClient('mongodb://192.168.1.210/zz_web')
        db_test = client_test.zz_web
        zz_sms_test = db_test.zz_sms
        post_id_test = zz_sms_test.insert_one(argv).inserted_id
        print(post_id_test)
        client_pro = MongoClient('mongodb://192.168.1.210/zz_web')
        db_pro = client_pro.zz_web
        zz_sms_pro = db_pro.zz_sms
        post_id_pro = zz_sms_pro.insert_one(argv).inserted_id
        print(post_id_pro)
    except Exception as e:
        print(e)
    else:
        print("test")