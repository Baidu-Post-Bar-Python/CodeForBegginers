# ocr.html
import requests
from typing import List
# 这道题需要页面内注释的数据，因此需要做个简单的爬虫……
# 当然直接从网页复制数据也可以

# 获取html中的注释
def get_comments(text: str) -> List[str]:
    comments: List[str] = []
    start = text.find('<!--', 0)
    while start != -1:
        end = text.find('-->', start)
        if end == -1:
            break
        comments.append(text[start + 4:end])
        start = text.find('<!--', end + 3)
    return comments


def get_messed_text():
    text = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html').text
    # 最后一段注释中间的就是数据
    messed_text = get_comments(text)[-1]
    return messed_text


if __name__ == "__main__":
    messed = get_messed_text()
    letters = ''.join(filter(str.isalpha, messed))
    print(letters)
