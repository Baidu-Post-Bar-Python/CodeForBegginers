# peak.html
import requests
import pickle

# pronounce it
# <!-- peak hell sounds familiar ? -->
# 读一读，能发现是模块pickle的发音

# 有个奇怪的peakhell元素，里面有个文件，下载下来用pickel解码

if __name__ == "__main__":
    response = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
    obj = pickle.loads(response.content)
    print(obj)
    # 可以看到是个二元组的二位列表
    # 单字符和数字，可猜想是个图形，数字表示重复次数遍历打印看看，就是结果，是channel的形状
    for array in obj:
        print(''.join(char * count for char, count in array))
    
