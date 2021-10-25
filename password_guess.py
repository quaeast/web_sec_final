from match_command import load_csdn, generate_is_command_func_list


def dict(data_frame):
    # passwd == username
    username_is_passwd = data_frame['passwd'] == data_frame['username']
    # email == passwd
    email_is_passwd = data_frame['passwd'] == data_frame['email']
    # passwd is command
    # 这里其实需要把正则表达式改成更严格的形式
    # 因为分析内容的时候只考虑包含，而如果破解密码则需要严格相等
    is_command_func_list = generate_is_command_func_list()
    command_is_passwd = False
    for i in is_command_func_list:
        command_is_passwd |= i(data_frame)
    # 还可以增加其他条件...
    return username_is_passwd | email_is_passwd | command_is_passwd


if __name__ == '__main__':
    df = load_csdn()
    res = df.loc[dict]
    print(res.shape)
    print('success rate: {:.2%}'.format(res.shape[0]/df.shape[0]))
