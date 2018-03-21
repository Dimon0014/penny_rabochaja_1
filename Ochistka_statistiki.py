import json
import win32api, win32con, time
import os
# with open('real_01_ochistka.txt', 'r') as f:  # извлекаем  из файла
#     data2 = json.load(f)
# print(data2)
k = 93                   ##
proverka = True
while proverka:
    k =k+1
    print('nomer cikla',k)
    name = str(k)+'cikl_m.txt'
    name2 = str(k)+'cikl_m_och.txt'
    path_name ='C:/Users/Dimon/PycharmProjects/penny_rabochaja_1/'+name
    print('ищем файл',path_name)
    if os.path.exists(path_name):
        print("Файл найден")
        viborka = []                                          ##
        file_obj = open(name, 'r')                      ## Создание списка из нагерерированого
        data_list = file_obj.readlines()                      ##
        i = 0
        for line in data_list:                                ##
            i += 1
            if i%2 ==0:
                viborka.append(int(line))
        file_obj.close()
        print(viborka)


        file_obj = open(name2, 'w')
        file_obj.writelines("%s\n" % i for i in viborka)
    else:
        print("Файл не найден")
        proverka = False

# for item in viborka:
#    file_obj.writeline(str(item)+'/n')
# file_obj.close()