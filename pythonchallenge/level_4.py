# linkedlist.html
import requests

# 可以看到点进去让你到linkedlist.php
# 然后点击图片能进入第一个节点
# 可以看到query parameter里参数nothing为12345
# 正文内容是下一个节点的nothing参数44827
# 因此做法就是循环请求，下一个的nothing是这个的响应里的……
# 最终会到不能发现任何数字的响应，即为结果

if __name__ == "__main__":
    nothing = '12345'
    while True:
        print(f'nothing = {nothing}')
        text = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}').text
        nothing = ''.join(filter(str.isdigit, text))
        if not nothing.isdigit():
            break
    print(text)