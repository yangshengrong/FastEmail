# -*- coding:utf-8- -*-
"""
Author:Yang Sheng-rong
Date:2023年09月09日
Email:3118393236@qq.com
"""
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
import mimetypes

from typing import List
import os


class BaseMsg:
    """product msg"""
    _msgs = MIMEMultipart()

    def __init__(self, title: str, to_addr: List[str] or str):
        """
        :param title: Email Title
        :param to_addr: Send to addr
        """
        self._msgs["Subject"] = Header(title, 'utf-8')
        if type(to_addr) is list:
            to_addr = ";".join(to_addr)
        self._msgs["To"] = to_addr

    def content(self, content: str):
        """
        :param content: Email content
        :return: None
        """
        self._msgs.attach(MIMEText(content, "plain", "utf-8"))

    def msg(self) -> MIMEMultipart:
        """
        :return: msg :class: <MIMEMultipart> object
        """
        return self._msgs


class TextMsg(BaseMsg):
    """
    send plain email
    """
    pass


class HtmlMsg(BaseMsg):
    """
    send html email
    """
    def content(self, content: str = None, filepath: str = None):
        """
        :param content: html string
        :param filepath: or html filepath
        :return: None
        """
        if content or filepath:
            if filepath:
                html = open(filepath, 'r', encoding='utf-8').read()
                self._msgs.attach(MIMEText(html, 'html'))
                return
            self._msgs.attach(MIMEText(content, 'html'))
            return
        raise 'not give params content or path'


class FileMsg(BaseMsg):
    """
    send file email
    """
    def content(self, filepath: str):
        """
        :param filepath: file path
        :return: None
        """
        content_type = mimetypes.guess_type(filepath)[0]
        app = MIMEApplication(open(filepath, 'rb').read())
        app.set_type(content_type)
        filename = os.path.basename(filepath)
        app.add_header('content-disposition', 'attachment', filename=filename)
        self._msgs.attach(app)


class MixMsg(BaseMsg):
    """
    send mix html and file
    """
    def content(self, html_path: str, filepath: str = None):
        """
        :param html_path: html path
        :param filepath: file path
        :return: None
        """
        if not filepath:
            raise "recommend to use HtmlMsg Class"
        content_type = mimetypes.guess_type(filepath)[0]
        app = MIMEApplication(open(filepath, 'rb').read())
        app.set_type(content_type)
        filename = os.path.basename(filepath)
        app.add_header('content-disposition', 'attachment', filename=filename)
        self._msgs.attach(app)

        html = open(html_path, 'r', encoding='utf-8').read()
        self._msgs.attach(MIMEText(html, 'html'))
