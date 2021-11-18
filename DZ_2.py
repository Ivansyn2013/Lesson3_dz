# задание №2 из третьего урока
# * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.
def first_sign(my_element):
    '''
    Return first sign of element
    :param my_element:
    :return:
    '''
    work_f = []
    work_f = list(my_element)
    return work_f[0]


def theaurus_adv(my_name_str):
    # подготовка данных
    my_name_dict = {}
    my_name_dict.clear
    fs_list = []
    surname_list = []
    name_list = []
    all_list = []

    filter_names = []
    all_list = my_name_str.split(' ')
    i = 0
    # получаем имена и фамилии
    while i < len(all_list):
        if i % 2 == 0:
            name_list.append(all_list[i]);
        else:
            surname_list.append(all_list[i]);
        i += 1
    # создание списка первых букв имен
    fs_list = list(map(first_sign, name_list))
    name_str = ' '.join(all_list)

    print(fs_list)
    # сортировка и фильтрация
    for i in range(len(name_list)):
        temp_name_list = []
        for ii in range(len(name_list)):
            if fs_list[i] == first_sign(name_list[ii]):
                temp_name_list.append(name_list[ii])
        filter_names.append(temp_name_list[:])

    my_name_dict = dict(zip(fs_list, filter_names))

    print(filter_names)
    print(my_name_dict)

    print(my_name_dict)
    return None


input_names = str(input('Введите имя и фамилию:'))

# print(input_names)

theaurus_adv(input_names)
