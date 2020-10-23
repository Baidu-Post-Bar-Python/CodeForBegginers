# integrity.html
import requests
from level_2 import get_comments
import bz2

if __name__ == "__main__":
    # 看页面元素，又有注释，虫子点进去让你登陆
    # 注释里un和pw容易猜到是用户名和密码，而且不是明文
    comment = get_comments(requests.get('http://www.pythonchallenge.com/pc/def/integrity.html').text)[0]
    _, un, _, pw, _ = comment.split("'")
    print(un, pw)
    # 根据格式特点判断是bzip2的解压……
    username = bz2.decompress(eval(f'b"{un}"'))
    password = bz2.decompress(eval(f'b"{pw}"'))
    print(f'un = {username}')
    print(f'pw = {password}')
    