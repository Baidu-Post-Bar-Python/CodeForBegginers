# oxygen.html
import requests
import io
from PIL import Image

if __name__ == "__main__":
    # 没别的线索，只有图片里的怪怪的条形码
    # 那就下载图片看条形码的内容
    img = Image.open(io.BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
    # 找到条形码所在行，直接取中间没问题，格子宽度7像素，切片一下
    row = [img.getpixel((x, img.height / 2)) for x in range(img.width)][::7]
    # 可以发现都是rgb相等的像素，可猜测就是这个值是个ascii码，才能变成文字
    message = ''.join(map(lambda item: chr(int(item[0])), row))
    print(message)
    # 可以看到一个列表，抽出来再来一次ascii码映射……
    print(''.join(map(chr, eval(message[message.index('['): message.index(']') + 1]))))
