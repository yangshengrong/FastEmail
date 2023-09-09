# -*- coding:utf-8- -*-
"""
Author:Yang Sheng-rong
Date:2023年09月08日
Email:3118393236@qq.com
"""
import smtplib
from email.mime.multipart import MIMEMultipart


class BaseEmail:
    _client = None

    def __init__(self, account: str, pwd: str):
        self.account = account
        self.pwd = pwd

    def _exam(self):
        self._client = smtplib.SMTP_SSL(host='exam.com', port=465)

    def _login(self):
        self._exam()
        self._client.login(user=self.account, password=self.pwd)

    def send(self, msg: MIMEMultipart):
        self._login()
        msg["From"] = self.account
        self._client.sendmail(self.account, msg["To"], msg.as_string())


class QQEmail(BaseEmail):
    def _exam(self):
        self._client = smtplib.SMTP_SSL("smtp.qq.com", 465)


class Email163(BaseEmail):
    def _exam(self):
        self._client = smtplib.SMTP_SSL("smtp.163.com", 465)


class GoogleEmail(BaseEmail):
    def _exam(self):
        self._client = smtplib.SMTP_SSL("smtp.gmail.com", 465)
