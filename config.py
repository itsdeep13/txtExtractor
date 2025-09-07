#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8211756735:AAF8CfBs2ufj950ltAiDKHDBs0vyamzl7K4")
    API_ID = int(os.environ.get("API_ID", "27473563"))
    API_HASH = os.environ.get("API_HASH", "bc2ea0765ac96bb474891b0243f44390")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6363345131")
