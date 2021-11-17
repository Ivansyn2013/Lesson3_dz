# задание №2 из третьего урока
# * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.
def first_sign (my_element):
    '''
    Return first sign of element
    :param my_element:
    :return:
    '''
    work_f = []
    work_f = list(my_element)
    return work_f[0]



def theaurus_adv (my_name, my_surname):
    #подготовка данных
    my_name_dict = {}
    my_name_dict.clear
    my_name = str(my_name)
    my_surname = str(my_surname)
    fs_list = []
    name_surname_list = []
    name_list = []
    name_surname_list.append()
    #создание списка первых букв
    fs_list.append(first_sign(my_name))
    # создание списока имен
    name_list.append(my_name)
    #сортировка и фильтрация
    for i in range(len(fs_list)):

        # работа в словаре
        my_name_dict = {first_sign(my_name): my_surname}
    print(my_name_dict)
    return None

input_names = []
input_names.append(input('Введите имя и фамилию:').split(' '))



#print(input_names)

for i in range(0, len(input_names[0])-1, 2):
    print(theaurus_adv(input_names[0][i],input_names[0][i+1]))