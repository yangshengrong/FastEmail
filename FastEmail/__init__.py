# -*- coding:utf-8- -*-
"""
Author:Yang Sheng-rong
Date:2023年09月08日
Email:3118393236@qq.com
"""
from . import Email
from . import Message


"""
Usage::
    >>> from FastEmail.Email import QQEmail
    >>> from FastEmail.Message import MixMsg
    >>> qq = QQEmail("xxxxx@qq.com", 'xxxxxxx')
    >>> msg = MixMsg(title="Util Test", to_addr="xxxxxxx@qq.com")
    >>> msg.content(html_path="test.html", filepath="requirements.txt")
    >>> qq.send(msg.msg())
"""