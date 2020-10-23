# bull.html

from collections import Counter
from typing import List, Tuple
# 点击图片可以看到sequence，规律是1开始，1个1->11，2个1->21，1个2 1个1->1211，1个1 1个2 2个1 ->111221……
# 那就用生成器产生序列！
def sequence():
    s = '1'
    while True:
        yield s
        s = next_of(s)
        
def next_of(s: str):
    current_char = s[0]
    counts: List[Tuple[int, int]] = []
    count = 0
    for i in range(len(s)):
        if s[i] == current_char:
            count += 1
        else:
            counts.append((current_char, count))
            current_char = s[i]
            count = 1
    counts.append((current_char, count))
    return ''.join(f'{count}{value}' for value, count in counts)

if __name__ == "__main__":
    seq = sequence()
    for i in range(31):
        current = next(seq)
        print(f'a[{i}] = {current}')
    print(current.__len__())