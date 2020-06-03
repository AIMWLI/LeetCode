"""
三次逆转
"""


class abcdef_feabcd:
    index = 4;
    str = 'abcdef'

    def reverse_words(str, index):
        # [0:index:1] 从0到n步长为1
        # [-1::-1] 第一个参数起:到末尾:步长-1为反向
        str1 = str[0:index:1][-1::-1]  # dcba
        str2 = str[index::1][-1::-1]  # fe
        return (str1 + str2)[-1::-1]

    result = reverse_words(str, index)
    print(result) #efabcd