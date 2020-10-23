# equality.html
import requests
from level_2 import get_comments

def is_bodyguard(inner:str, outer: str):
    return inner.islower() and outer.isupper()

if __name__ == "__main__":
    text = requests.get('http://www.pythonchallenge.com/pc/def/equality.html').text
    comment = get_comments(text)[0]
    # 题意大概是找到所有左右恰好有三个大写字母的小写字母
    # 可以验证，开头和结尾的4个都不符合，因此在中间[4:-4]的范围找，省去越界判断
    for i in range(4, len(comment) - 4):
        inner = comment[i]
        if (all(is_bodyguard(inner, left) for left in comment[i - 3: i]) and
            all(is_bodyguard(inner, right) for right in comment[i + 1: i + 4]) and
            not is_bodyguard(inner, comment[i - 4]) and
            not is_bodyguard(inner, comment[i + 4])
        ):
            print(inner, end='')
    print()


