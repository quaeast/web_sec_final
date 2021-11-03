import static_elements


def append_save_to_dict(dict_list, filename='dict.txt'):
    dict_list = map(lambda s: str(s) + '\n', dict_list)
    with open(filename, 'a') as f:
        f.writelines(dict_list)


def multiply_str(*args):
    if len(args) < 2:
        return args[0]
    if len(args) == 2:
        result_list = []
        for i in args[0]:
            for j in args[1]:
                result_list.append(i + j)
        return result_list
    else:
        return multiply_str(multiply_str(args[0], args[1]), *args[2:])


# index >= 1
def power_str(str_list, index):
    if index <= 1:
        return str_list
    return multiply_str(str_list, power_str(str_list, index - 1))


def get_len_byte(dict_list):
    res = 0
    for i in dict_list:
        res += len(i)
    return res


def get_len_h(num):
    num = num
    if num / 1024 ** 3 >= 1:
        return str(num / 1024.0 ** 3) + 'G'
    if num / 1024 ** 2 >= 1:
        return str(num / 1024.0 ** 2) + 'M'
    if num / 1024 >= 1:
        return str(num / 1024.0) + 'K'
    return num


def gen_basic_dict():
    res = []
    # 六位数字
    res += power_str(static_elements.nums_list, 6)
    # 八位日期
    res += multiply_str(['19', '20'], static_elements.nums_list, static_elements.nums_list,
                        static_elements.month_digital,
                        static_elements.date_digital)
    # 6位字母和数字
    res += power_str(static_elements.nums_list + static_elements.alphabet, 6)
    return res

def gen_csdn_dict():
    res = gen_basic_dict()
    # 匹配频繁出现的单词、键盘组合
    res += multiply_str(static_elements.csdn_hot_words, power_str(static_elements.printable_ascii_list, 3))
    return res


def gen_yahoo_dict():
    res = gen_basic_dict()
    res += multiply_str(static_elements.yahoo_hot_words, power_str(static_elements.printable_ascii_list, 3))
    return res



if __name__ == '__main__':
    # res_l = gen_csdn_dict()
    # le = get_len_h(get_len_byte(res_l))
    # print(le)
    a = get_len_h(34 ** 6)
    print(a)
