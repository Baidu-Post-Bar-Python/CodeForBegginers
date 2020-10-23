# map.html
import functools

# 从图中看出字母有+2的对应关系，可以联想到凯撒密码

def caesar_decode_character(encoded: str, offset: int) -> str:
    if not encoded.isalpha(): return encoded
    ascii_no = ord(encoded)
    # 本题中都是小写，所以只对小写做处理
    start_no = ord('a')
    character_offset = ascii_no - start_no # encoded在字母表中的偏移量
    return chr(start_no + (character_offset + offset) % 26)

def caesar_decode(ciphertext: str, offset: int) -> str:
    return ''.join(map(functools.partial(caesar_decode_character, offset=offset), ciphertext))
    # 上面这行代码的作用基本等价于下面代码的逻辑
    chars = []
    for char in ciphertext:
        chars.append(caesar_decode_character(char, offset))
    return ''.join(chars)
    # 能简单地用map映射简化逻辑，何乐而不为呢
    # 毕竟这道题的名字就是map

if __name__ == "__main__":
    print(caesar_decode("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.", 2))
    print(caesar_decode('map', 2))
