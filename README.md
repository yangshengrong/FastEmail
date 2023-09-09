# FastEmail
Fast send email by Python

# Usage
```
from FastEmail.Email import QQEmail
from FastEmail.Message import MixMsg
qq = QQEmail("xxxxx@qq.com", 'xxxxxxx')
msg = MixMsg(title="Util Test", to_addr="xxxxxxx@qq.com")
msg.content(html_path="test.html", filepath="requirements.txt")
qq.send(msg.msg())
```
