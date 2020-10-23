# channel.html
import requests
import io
import zipfile
import re

if __name__ == "__main__":
    # 可以看到页面注释有个zip，那就试试zip，可以下载到一个文件
    # readme里面一看，又是个链表……
    # 开始是90052
    response = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
    byteio = io.BytesIO(response.content)
    channel_zip = zipfile.ZipFile(byteio)
    nothing = '90052'
    while True:
        file_name = f'{nothing}.txt'
        content = channel_zip.read(file_name).decode("utf-8")
        print(channel_zip.getinfo(file_name).comment.decode("utf-8"), end='')
        # 上次暴力筛数字，这次用下正则吧……
        match = re.search("Next nothing is (\d+)", content)
        if match == None:
            break
        nothing = match.group(1)

    # 里面的字母拼起来是oxygen