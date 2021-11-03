import pandas as pd

command_list = ['cd', 'ls', 'cp', 'mv', 'touch', 'rm', 'mkdir']


def load_csdn():
    file_path = 'www.csdn.net.sql'
    data_set = pd.read_csv(file_path,
                           sep=' # ',
                           names=['username', 'passwd', 'email'])
    print(data_set.head(3))
    print('csdn data loaded...')
    return data_set


def load_yahoo():
    file_path = 'plaintxt_yahoo.txt'
    data_set = pd.read_csv(file_path,
                           sep=':',
                           names=['user_id', 'username', 'passwd'])
    # print(data_set.isnull().any())
    print(data_set.head(3))
    print('yahoo data loaded...')
    return data_set.dropna()


def generate_is_command_func_list():
    res = []
    for i in command_list:
        def make_function(command):
            def temp(data_set):
                return data_set['passwd'].str.match(command + '.*')

            return temp

        res.append(make_function(i))
    return res


if __name__ == '__main__':
    ds = load_csdn()
    # ds = load_yahoo()
    func_list = generate_is_command_func_list()
    result_list = []
    for command_tuple in zip(command_list, func_list):
        temp = ds.loc[command_tuple[1]]
        print(command_tuple[0], temp.shape)
        result_list.append(temp)
