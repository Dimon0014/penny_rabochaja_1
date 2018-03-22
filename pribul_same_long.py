import json
import random
from datetime import datetime, timedelta
from time import clock
# ------------- в начале обработка единичных символов
import math


def last_last_seen_steps_of_simv_01(dict, key):  # альтернатива  "last_next_seen_all_steps_1"
    result = dict[key][0]

    # print('функия next_seen_steps =',result)
    return result


def dob_next_seen_1(dict, key, steps):  # функция добавления/инициализация шагов с последнего появления

    if (key) in dict:  # проверка на наличие значений
        last_seen = last_last_seen_steps_of_simv_01(dict, key)
        # print('steps-last_time seen_in_key =', last_seen)
        # print('печатает dict[key][1][0]', dict[key][1][0])
        dict[key][1].append(last_seen)
        dict[key][2] = len(dict[key][1])  # сколько раз уже выпадала


    else:  # инициализация
        dict.update({(key): [0, [steps], 1, key, steps]})  # инициализация
        # print('key in function =', key)


def add_step_to_all_1(dict):
    for item in dict:
        dict[item][0] = dict[item][0] + 1
        dict[item][4] = dict[item][4] + 1


def more_of_1(dict):
    spisok = []
    a = 0
    s = 0
    spisok2 = []
    for item in dict:
        if dict[item][2] == 1:

            if dict[item][4] > 100:

                spisok.append(dict[item])
                if len(spisok) > 0:
                    a = dict[item][3]
                    s = dict[item][4]

                    # print('spisok', spisok)
                    spisok2.append(a)
                    spisok2.append(s)
                    # print('spisok2', spisok2)
                break

                # print("номер", dict[item][3], "выпал", dict[item][2], "раз(а)--шаг", dict[item][4])
    return spisok2


def podchet_simv(slist):  # подсчет сколько раз встречаются символы в строке(списке)
    d = dict()
    for c in slist:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# отсюда функции патернов-------------------------------
#
# сначала из двух цифр



# key1 -- значение выпавшего числа\\
# key1step(key,dictEd) - функция находит значение интервала для выпавшего числа в словаре dictEd  \\
# key1step - значение интервала у выпавшего сейчас числа\\
# key2step - значение интервала с предыдущего шага\\
# key1step, key2step -- паттерн который нужно сравнить \\
# dictEd -- словарь одиночных символов, откуда нужно взять значение step(dict[key][0])\\

# listAll_inter -- список всех интервалов друг за другом -- сплошняком
# dict2Glob -- словарь интервалов двоек глобал\\
# dict2Lok -- словарь интервалов двоек локал\\

#

#
# def intervals_of_02(key1_step,key2step):
def key01step(key, dictEd):
    result = dictEd[(key)][0]
    dictEd[key][0] = 0  # после того как достанет обнуляет
    # print('из функции достающей интервалы result',result )
    # print('из функции достающей интервалы dictEd[(key)][0]', dictEd[(key)][0])
    return result


# key01step = key01step(key,dictEd) # вычисляем когда последний раз был виден выпавший номер
def intervals_of_2(key2step, key1step, dict2Glob,
                   steps_sesia):  # функция добавления интервалов как для глобал так и для локал
    if (key2step, key1step) in dict2Glob:  # проверка dict2Glob на наличие ключа, если нет то инициализация

        last_seen = dict2Glob[(key2step, key1step)][0]  # переменную последний раз видели загоняем в буфер
        dict2Glob[(key2step, key1step)][0] = 0  # переменную последний раз видели обнуляем
        dict2Glob[(key2step, key1step)][1].append(last_seen)  # добавляем значение к списку последний раз видели
        count = len(dict2Glob[(key2step, key1step)][1])  # переменную переменную раз видели загоняем в буфер
        dict2Glob[(key2step, key1step)][2] = count
        #  dict2Glob[(key2step,key1step)][3] = steps_sesia # количество шагов в сесии- нужно для предсказанияkey1step # первый символ ключа
        #  dict2Glob[(key2step,key1step)][4] = key2step # первый символ ключа
        #  dict2Glob[(key2step,key1step)][5] = key1step # второй символ ключа
    else:
        dict2Glob.update({(key2step, key1step): [0, [1], 1, key2step, key1step, steps_sesia]})  # инициализация


def intervals_of_3(key3step, key2step, key1step, dict3Glob,
                   steps_sesia):  # функция добавления интервалов как для глобал так и для локал
    if (key3step, key2step, key1step) in dict3Glob:  # проверка dict2Glob на пустоту, если пусто то инициализация
        last_seen = dict3Glob[(key3step, key2step, key1step)][0]  # переменную последний раз видели загоняем в буфер
        dict3Glob[(key3step, key2step, key1step)][0] = 0  # переменную последний раз видели обнуляем
        dict3Glob[(key3step, key2step, key1step)][1].append(
            last_seen)  # добавляем значение к списку последний раз видели
        count = len(
            dict3Glob[(key3step, key2step, key1step)][1])  # переменную переменную раз видели загоняем в буфер
        dict3Glob[(key3step, key2step, key1step)][2] = count
        # dict3Glob[(key3step, key2step,key1step)][3] = steps_sesia   #количество шагов в сесии- нужно для предсказания
        #  dict3Glob[(key3step, key2step,key1step)][4] = key3step  # первый символ ключа
        #  dict3Glob[(key3step, key2step,key1step)][5] = key2step   # второй символ ключа
        #  dict3Glob[(key3step, key2step,key1step)][6] = key1step # третий символ ключа
        print(' обновление словаря')
    else:
        dict3Glob.update({(key3step, key2step, key1step): [0, [1], 1, key3step, key2step, key1step,
                                                           steps_sesia]})  # инициализация
        print(' создание словаря')


def intervals_of_all(key1step, listAll_inter):  # список всех подряд интервалов
    listAll_inter.append(key1step)


# функция добавляющая шаги к словарям
def add_step_to_all_intervals_of_2(dict_interv2, key2step, key1step):  # а вот функция которая добовляет всем шаги
    # key=(key2step, key1step)
    for item in dict_interv2:
        # if item != key:

        dict_interv2[item][0] = dict_interv2[item][0] + 1
        dict_interv2[item][3] = dict_interv2[item][3] + 1
        print('dict_interv2[item][0]', dict_interv2[item][0])
        print('dict_interv2[item][3]', dict_interv2[item][3])
        # for item in dict_interv2:
        #     if item == key:
        #        dict[item][3] = dict[item][0] + 1


        # def intervals_of_2(key1_step,key2step, dictEd, dict2,dict2lok,listAll_inter):
        #     #  перебор всех значений словаря по ключу в другой функции, эта функция сравнивает и добавляет
        #
        #       if len(dict2[(key1)][0]) != 0:  # проверка на наличие значений, проверяется длинна словаря- умное решение
        #         # times_seen = len(dict[key][1])
        #         listAll_inter.append(0) # добавление 0-левого интервала в общий список
        #                             # в принципе интервал равный нулю может быть только в начале, как и интервал [1,0], [2,1] в
        #                            # общем первые значения интервалов в мусор
        #         listAll_inter.append(dict[key1][0]) # добавление первого значимого интервала в общий список
        #         key2step=key1
        #         dict2[(key1)][0]=1
        #         print('первая запись в списке интервалов', key1)
        #       else:
        #         listAll_inter.append(dict[key1][0])
        #         dict[(key)][0]
        #         for item in dict:
        #             if item == key1:
        #                 dict2[item][0] = dict[item][0] + 1

        # собственно тело программы начинается здесь----------------------------------------------------------------


# steps = 225  типа имитатор счетчика ходов
# значение словаря еденичных символо на текущий момент

# проверочный словарь d = {(36):[ 1,[1, 2], 33, 22,2],(35):[ 11,[101, 102], 31, 22,2],(34):[ 13,[103, 106], 71, 22,2]}
# типа число полученное от распознователя символов key = (35)

# востановление всех ходов
def postrocno(spisok, name):
    i = 0
    for item in spisok:
        i = i + 1
        print(steps, name, 'стока', i, item)


def stepsbig(interval, porog, steps_big):
    steps_big
    if interval < porog:
        steps_big = steps_big + 1
    return steps_big


def podchet_interv_odd(slovar):
    obshie = 0
    rezult = 0
    for item in slovar:
        if (slovar[item][3] % 2) != 0:
            if (slovar[item][0]) < 1000:
                rezult = obshie + slovar[item][2]

    return rezult


def podchet_interv_iven(slovar):
    obshie = 0
    rezult = 0
    for item in slovar:
        if (slovar[item][3] % 2) == 0:
            if (slovar[item][0]) < 1000:
                rezult = obshie + slovar[item][2]
    return rezult


def nahogd_big_interv(slovar):
    rezult = 0
    big = 0
    for item in slovar:

        if (slovar[item][0]) > big:
            rezult = slovar[item][3]
            slovar[item][0] = big
    return rezult


def pre1_predskazatel_1(key, list_of200, steps_of_predscazan):
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36]
    list = list_of200

    for item in keys:
        if item == key:
            list.append(key)
            if len(list) > steps_of_predscazan:
                list.pop(0)
    return list


def pre2_predskazatel_1(list_of200):
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36]
    list = list_of200
    list_par = []
    for item in keys:
        list_par.append([item, 0])
        for it in list:
            if it == item:
                list_par[item][1] = list_par[item][1] + 1
    return list_par
    # for it in keys:
    #     for item in list:
    #         if item not in d:
    #             list_par.append([item])
    #         else:
    #             d[c] += 1


def pre3_predskazatel_1(list_sort):
    list_sort.sort(key=lambda item: item[1])
    list_sort.reverse()
    # nolik = list_sort[0][0]
    # odin = list_sort[1][0]
    # dva = list_sort[2][0]
    # #tri = list_sort[3][0]
    # result =list_sort[0][0] # random.choice([nolik,odin,dva] )
    if list_sort[0][1] > 1:
        result = list_sort[0][0]  # random.choice([nolik,odin,dva] )
    else:
        result = 99
    return result


def pre3_predskazatel_1_all(list_sort):
    list_sort.sort(key=lambda item: item[1])
    list_sort.reverse()
    # nolik = list_sort[0][0]
    # odin = list_sort[1][0]
    # dva = list_sort[2][0]
    # #tri = list_sort[3][0]
    result = list_sort  # random.choice([nolik,odin,dva] )

    return result


def proverka_predskaza_1(key, list_of_win_proverki, winer_1):
    if key == list_of_win_proverki[2]:
        list_of_win_proverki[
            1] = 1  # включение происходит в двух случаях при выигрыше и при превышении количества 54 шагов
        result = list_of_win_proverki  # первое значение - количество шагоd
        # второе значени флаг сброса продолжения проверки
        # третье значение предсказаное число
    else:
        list_of_win_proverki[1] = 0
        list_of_win_proverki[0] = list_of_win_proverki[
                                      0] + 1  # так как else наступает и в случае (winer_1 == 99) - когда
        #  шагов нет, они прибавляются то ниже при (winer_1 == 99)
        #   эти шаги вычитаются
        result = list_of_win_proverki
    if winer_1 == 99:
        list_of_win_proverki[0] = list_of_win_proverki[0] - 1
        result = list_of_win_proverki
    return result


def pre1_predskazatel_2(key, list_of200, steps_of_predscazan):
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
            28, 29, 30, 31, 32, 33, 34, 35, 36]
    list = list_of200

    for item in keys:
        if item == key:
            list.append(key)
            if len(list) > steps_of_predscazan:
                list.pop(0)
    return list


def pre2_predskazatel_2(list_of200):
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
            28, 29, 30, 31, 32, 33, 34, 35, 36]
    list = list_of200
    list_par = []
    for item in keys:
        list_par.append([item, 0])
        for it in list:
            if it == item:
                list_par[item][1] = list_par[item][1] + 1
    return list_par
    # for it in keys:
    #     for item in list:
    #         if item not in d:
    #             list_par.append([item])
    #         else:
    #             d[c] += 1


def pre3_predskazatel_2(list_sort):
    list_sort.sort(key=lambda item: item[1])
    list_sort.reverse()
    # nolik = list_sort[0][0]
    # odin = list_sort[1][0]
    # dva = list_sort[2][0]
    # #tri = list_sort[3][0]
    result = list_sort[0][0]  # random.choice([nolik,odin,dva] )

    return result


def proverka_predskaza_2(key, list_of_win_proverki):
    if key == list_of_win_proverki[2]:
        list_of_win_proverki[1] = 1
        result = list_of_win_proverki  # первое значение - количество шагоd
        # второе значени флаг сброса продолжения проверки
        # третье значение предсказаное число

    else:
        list_of_win_proverki[1] = 0
        list_of_win_proverki[0] = list_of_win_proverki[0] + 1
        result = list_of_win_proverki
    return result


def podchet_simv(slist):  # подсчет сколько раз встречаются символы в строке(списке)
    d = dict()
    for c in slist:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def podchet_balansa(spisok):
    pribyl = 0
    for item in spisok:
        if item == 1:
            pribyl = pribyl + 0.35  # - (item*0.01)
        if item == 2:
            pribyl = pribyl + 0.34  # - (item*0.01)
        if item == 3:
            pribyl = pribyl + 0.33  # - (item*0.01)

        if item == 4:
            pribyl = pribyl + 0.32  # - (item*0.01)

        if item == 5:
            pribyl = pribyl + 0.31  # - (item*0.01)

        if item == 6:
            pribyl = pribyl + 0.30  # - (item*0.01)
        ########################################################## +0.06
        if item == 7:
            pribyl = pribyl + 0.64  # - (item*0.01)

        if item == 8:
            pribyl = pribyl + 0.62  # - (item*0.01)
        if item == 9:
            pribyl = pribyl + 0.60  # - (item*0.01)
        if item == 10:
            pribyl = pribyl + 0.58  # - (item*0.01)
        if item == 11:
            pribyl = pribyl + 0.56  # - (item*0.01)
        if item == 11:
            pribyl = pribyl + 0.54  # - (item*0.01)
        if item == 12:
            pribyl = pribyl + 0.52  # - (item*0.01)
        if item == 13:
            pribyl = pribyl + 0.50  # - (item*0.01)
        if item == 14:
            pribyl = pribyl + 0.48  # - (item*0.01)
        if item == 15:
            pribyl = pribyl + 0.46  # - (item*0.01)
        if item == 16:
            pribyl = pribyl + 0.44  # - (item*0.01)
        if item == 17:
            pribyl = pribyl + 0.42  # - (item*0.01)
        if item == 18:
            pribyl = pribyl + 0.40  # - (item*0.01)
        if item == 19:
            pribyl = pribyl + 0.38  # - (item*0.01)
        if item == 20:
            pribyl = pribyl + 0.36  # - (item*0.01)
        if item == 21:
            pribyl = pribyl + 0.34  # - (item*0.01)
        if item == 22:
            pribyl = pribyl + 0.32  # - (item*0.01)
        if item == 23:
            pribyl = pribyl + 0.30  # - (item*0.01)
        ###########################################################      +0.36 =0.42
        if item == 24:
            pribyl = pribyl + 0.66  # - (item*0.01)

        if item == 25:
            pribyl = pribyl + 0.63  # - (item*0.01)
        if item == 26:
            pribyl = pribyl + 0.60  # - (item*0.01)
        if item == 27:
            pribyl = pribyl + 0.57  # - (item*0.01)
        if item == 28:
            pribyl = pribyl + 0.54  # - (item*0.01)
        if item == 29:
            pribyl = pribyl + 0.51  # - (item*0.01)
        if item == 30:
            pribyl = pribyl + 0.48  # - (item*0.01)
        if item == 31:
            pribyl = pribyl + 0.45  # - (item*0.01)
        if item == 32:
            pribyl = pribyl + 0.42  # - (item*0.01)
        if item == 33:
            pribyl = pribyl + 0.39  # - (item*0.01)
        if item == 34:
            pribyl = pribyl + 0.36  # - (item*0.01)
        if item == 35:
            pribyl = pribyl + 0.33  # - (item*0.01)
        if item == 36:
            pribyl = pribyl + 0.30  # - (item*0.01)
        # if (item > 0) and (item < 37):
        #     pribyl = pribyl + 0.35 #- (item*0.01)





        # if (item < 55) and (item >36):
        #    pribyl = pribyl + ((72-36) - (item-36)*2)
        # if (item > 35)  and (item < 54):
        #     pribyl = pribyl + 0.35*2 - (item * 0.01)*2
        #
        # if (item  > 53) and (item  < 66):
        #     pribyl = pribyl + 0.35 * 3 - (item * 0.01) * 3
        #
        # if (item > 65) and (item < 75):
        #     pribyl = pribyl + 0.35 * 4 - (item * 0.01) * 4
        # if (item > 74) and (item < 82):
        #     pribyl = pribyl + 0.35 * 5 - (item * 0.01) * 5
        #
        # if (item > 81) and (item < 88):
        #     pribyl = pribyl + 0.35 * 6 - (item * 0.01) * 6
        # if (item > 87) and (item < 93):
        #     pribyl = pribyl + 0.35 * 7 - (item * 0.01) * 7
        # if (item > 92) and (item < 97):
        #     pribyl = pribyl + 0.35 * 8 - (item * 0.01) * 8
        # if (item > 96) and (item < 101):
        #     pribyl = pribyl + 0.35 * 9 - (item * 0.01) * 9
        # if (item > 100) and (item < 105):
        #     pribyl = pribyl + 0.35 * 10 - (item * 0.01) * 10
        #
        # if (item > 104) and (item < 108):
        #     pribyl = pribyl + 0.35 * 11 - (item * 0.01) * 11
        # if (item > 107) and (item < 111):
        #     pribyl = pribyl + 0.35 * 12 - (item * 0.01) * 12
        #
        # if (item > 110) and (item < 114):
        #     pribyl = pribyl + 0.35 * 13 - (item * 0.01) * 13
        # if (item > 113) and (item < 116):
        #     pribyl = pribyl + 0.35 * 14 - (item * 0.01) * 14
        # if (item > 115) and (item < 119):
        #     pribyl = pribyl + 0.35 * 15 - (item * 0.01) * 15
        if item == 37:
            pribyl = pribyl - 0.81
    return pribyl


rasnica2 = 0
ik = 0
vig = 0
prg = 0
chag = 0
nol = 0
real_pribyl = 0
pribyl2 = 0
neuch = ''
neuch2 = 0
i = 0
next_nol = 0
uchet_intervala = 0

nolik = 0
dub_nolik = 0
same_list = []
lev_list = []
prav_list = []
pravo = 0
levo = 0
same = 0
pribul=0
global_pribul_same = 0
for i in range(105, 106):  # while (ik < 1): # количество файлов
    # ik = ik + 1
    # file_obj = open('200cikl_ochh.txt', 'w')
    # file_obj.close()
    # file_obj = open('200cikl_ochh.txt', 'a')
    # for i in range(200+1):               # количество ходов в файле
    #     chislo = random.randint(0, 36)  # генерируем число
    #     file_obj.write(str(chislo) + '\n')
    #
    # file_obj.close()


    naime_file = str(i) + 'cikl_m_och.txt'
    viborka = []
    file_obj = open(naime_file)
    data_list = file_obj.readlines()
    for line in data_list:
        viborka.append(int(line))
    # объявление всех переменных-----------------------------------------------------------------------------------
    dic_ed = {}  # болванка под словарь едениц
    # -----------------------------------------------------------------------------------
    key = 0
    steps_sesia = 1
    key1 = key
    steps = 0
    old_key = -1
    # print("выборка",len(viborka))
    chet = 0
    nechet = 0
    index_same = 0
    index_lev = 0
    index_prv = 0
    propusk_sam = 0
    propusk_sam2 =0
    propusk_lev = 0
    propusk_prv = 0
    konec = False
    pribul_same=10
    pribul_same2 = 0
    while (steps < len(viborka)):
        key = viborka[steps]

        key1 = key
        steps = steps + 1
        if old_key > -1:
            if ((old_key == 1) or (old_key == 4) or (old_key == 7) or (old_key == 10) or (old_key == 13) or (
                old_key == 16) or (old_key == 19) or (old_key == 22) or (old_key == 25) or (old_key == 28) or (
                old_key == 31) or (old_key == 34)) \
                    and ((key1 == 1) or (key1 == 4) or (key1 == 7) or (key1 == 10) or (key1 == 13) or (key1 == 16) or (
                        key1 == 19) or (key1 == 22) or (key1 == 25) or (key1 == 28) or (key1 == 31) or (key1 == 34)):
                same = same + 1
                # propusk_sam = 0
                propusk_sam = propusk_sam + 2
                propusk_lev = propusk_lev - 1
                propusk_prv = propusk_prv - 1
                pribul_same = pribul_same + 0.23
                # index_same = same/steps
                # index_lev = levo/steps
                # index_prv = pravo/steps
            if ((old_key == 1) or (old_key == 4) or (old_key == 7) or (old_key == 10) or (old_key == 13) or (
                old_key == 16) or (old_key == 19) or (old_key == 22) or (old_key == 25) or (old_key == 28) or (
                old_key == 31) or (old_key == 34)) \
                    and ((key1 == 2) or (key1 == 5) or (key1 == 8) or (key1 == 11) or (key1 == 14) or (key1 == 17) or (
                        key1 == 20) or (key1 == 23) or (key1 == 26) or (key1 == 29) or (key1 == 32) or (key1 == 35)):
                pravo = pravo + 1
                # propusk_prv = 0
                propusk_prv = propusk_prv + 2
                propusk_sam = propusk_sam - 1
                propusk_lev = propusk_lev - 1
                pribul_same = pribul_same - 0.13
                # index_same = same / steps
                # index_lev = levo / steps
                # index_prv = pravo / steps
            if ((old_key == 1) or (old_key == 4) or (old_key == 7) or (old_key == 10) or (old_key == 13) or (
                old_key == 16) or (old_key == 19) or (old_key == 22) or (old_key == 25) or (old_key == 28) or (
                old_key == 31) or (old_key == 34)) \
                    and ((key1 == 3) or (key1 == 6) or (key1 == 9) or (key1 == 12) or (key1 == 15) or (key1 == 18) or (
                        key1 == 21) or (key1 == 24) or (key1 == 27) or (key1 == 30) or (key1 == 33) or (key1 == 36)):
                levo = levo + 1
                # propusk_lev = 0
                propusk_lev = propusk_lev + 2
                propusk_sam = propusk_sam - 1
                propusk_prv = propusk_prv - 1
                pribul_same = pribul_same - 0.13
                # index_same = same / steps
                # index_lev = levo / steps
                # index_prv = pravo / steps
            if ((old_key == 2) or (old_key == 5) or (old_key == 8) or (old_key == 11) or (old_key == 14) or (
                old_key == 17) or (old_key == 20) or (old_key == 23) or (old_key == 26) or (old_key == 29) or (
                old_key == 32) or (old_key == 35)) \
                    and ((key1 == 2) or (key1 == 5) or (key1 == 8) or (key1 == 11) or (key1 == 14) or (key1 == 17) or (
                        key1 == 20) or (key1 == 23) or (key1 == 26) or (key1 == 29) or (key1 == 32) or (key1 == 35)):
                same = same + 1
                # propusk_sam = 0
                propusk_sam = propusk_sam + 2
                propusk_lev = propusk_lev - 1
                propusk_prv = propusk_prv - 1
                pribul_same = pribul_same + 0.23
                # index_same = same / steps
                # index_lev = levo / steps
                # index_prv = pravo / steps
            if ((old_key == 2) or (old_key == 5) or (old_key == 8) or (old_key == 11) or (old_key == 14) or (
                old_key == 17) or (old_key == 20) or (old_key == 23) or (old_key == 26) or (old_key == 29) or (
                old_key == 32) or (old_key == 35)) \
                    and ((key1 == 3) or (key1 == 6) or (key1 == 9) or (key1 == 12) or (key1 == 15) or (key1 == 18) or (
                        key1 == 21) or (key1 == 24) or (key1 == 27) or (key1 == 30) or (key1 == 33) or (key1 == 36)):
                pravo = pravo + 1
                # propusk_prv = 0
                propusk_prv = propusk_prv + 2
                propusk_sam = propusk_sam - 1
                propusk_lev = propusk_lev - 1
                pribul_same = pribul_same - 0.13
                # index_same = same / steps
                # index_lev = levo / steps
                # index_prv = pravo / steps
            if ((old_key == 2) or (old_key == 5) or (old_key == 8) or (old_key == 11) or (old_key == 14) or (
                old_key == 17) or (old_key == 20) or (old_key == 23) or (old_key == 26) or (old_key == 29) or (
                old_key == 32) or (old_key == 35)) \
                    and ((key1 == 1) or (key1 == 4) or (key1 == 7) or (key1 == 10) or (key1 == 13) or (key1 == 16) or (
                        key1 == 19) or (key1 == 22) or (key1 == 25) or (key1 == 28) or (key1 == 31) or (key1 == 34)):
                levo = levo + 1
                # propusk_lev = 0
                propusk_lev = propusk_lev + 2
                propusk_sam = propusk_sam - 1
                propusk_prv = propusk_prv - 1
                pribul_same = pribul_same - 0.13
                # index_same = same / steps
                # index_lev = levo / steps
                # index_prv = pravo / steps

            if ((old_key == 3) or (old_key == 6) or (old_key == 9) or (old_key == 12) or (old_key == 15) or (
                old_key == 18) or (old_key == 21) or (old_key == 24) or (old_key == 27) or (old_key == 30) or (
                old_key == 33) or (old_key == 36)) \
                    and ((key1 == 3) or (key1 == 6) or (key1 == 9) or (key1 == 12) or (key1 == 15) or (key1 == 18) or (
                        key1 == 21) or (key1 == 24) or (key1 == 27) or (key1 == 30) or (key1 == 33) or (key1 == 36)):
                same = same + 1
                # propusk_sam = 0
                propusk_sam = propusk_sam + 2
                propusk_lev = propusk_lev - 1
                propusk_prv = propusk_prv - 1
                pribul_same = pribul_same + 0.23
                # index_same = same / steps
                # index_lev = levo / steps
                # index_prv = pravo / steps
            if ((old_key == 3) or (old_key == 6) or (old_key == 9) or (old_key == 12) or (old_key == 15) or (
                old_key == 18) or (old_key == 21) or (old_key == 24) or (old_key == 27) or (old_key == 30) or (
                old_key == 33) or (old_key == 36)) \
                    and ((key1 == 1) or (key1 == 4) or (key1 == 7) or (key1 == 10) or (key1 == 13) or (key1 == 16) or (
                        key1 == 19) or (key1 == 22) or (key1 == 25) or (key1 == 28) or (key1 == 31) or (key1 == 34)):
                pravo = pravo + 1
                # propusk_prv = 0
                propusk_prv = propusk_prv + 2
                propusk_sam = propusk_sam - 1
                propusk_lev = propusk_lev - 1
                pribul_same = pribul_same - 0.13
                # index_same = same / steps
                # index_lev = levo / steps
                # index_prv = pravo / steps
            if ((old_key == 3) or (old_key == 6) or (old_key == 9) or (old_key == 12) or (old_key == 15) or (
                old_key == 18) or (old_key == 21) or (old_key == 24) or (old_key == 27) or (old_key == 30) or (
                old_key == 33) or (old_key == 36)) \
                    and ((key1 == 2) or (key1 == 5) or (key1 == 8) or (key1 == 11) or (key1 == 14) or (key1 == 17) or (
                        key1 == 20) or (key1 == 23) or (key1 == 26) or (key1 == 29) or (key1 == 32) or (key1 == 35)):
                levo = levo + 1
                # propusk_lev = 0
                propusk_lev = propusk_lev + 2
                propusk_sam = propusk_sam - 1
                propusk_prv = propusk_prv - 1
                pribul_same = pribul_same - 0.13
                # index_same = same / steps
                # index_lev = levo / steps
                # index_prv = pravo / steps
                #################################################################################################################

            if ((old_key == 1) or (old_key == 4) or (old_key == 7) or (old_key == 10) or (old_key == 13) or (
                old_key == 16) or (old_key == 19) or (old_key == 22) or (old_key == 25) or (old_key == 28) or (
                old_key == 31) or (old_key == 34)) \
                    and (key1 == 0):
                nolik = nolik + 1
                propusk_sam = propusk_sam + 1
                propusk_lev = propusk_lev + 1
                propusk_prv = propusk_prv + 1
                pribul_same = pribul_same + 0.23
            if ((old_key == 2) or (old_key == 5) or (old_key == 8) or (old_key == 11) or (old_key == 14) or (
                old_key == 17) or (old_key == 20) or (old_key == 23) or (old_key == 26) or (old_key == 29) or (
                old_key == 32) or (old_key == 35)) \
                    and (key1 == 0):
                nolik = nolik + 1
                propusk_sam = propusk_sam + 1
                propusk_lev = propusk_lev + 1
                propusk_prv = propusk_prv + 1
                pribul_same = pribul_same + 0.23
            if ((old_key == 3) or (old_key == 6) or (old_key == 9) or (old_key == 12) or (old_key == 15) or (
                old_key == 18) or (old_key == 21) or (old_key == 24) or (old_key == 27) or (old_key == 30) or (
                old_key == 33) or (old_key == 36)) \
                    and (key1 == 0):
                nolik = nolik + 1
                propusk_sam = propusk_sam + 1
                propusk_lev = propusk_lev + 1
                propusk_prv = propusk_prv + 1
                pribul_same = pribul_same + 0.23
            if (old_key == 0) and (key1 == 0):
                dub_nolik = dub_nolik + 1
                propusk_sam = propusk_sam + 1
                propusk_lev = propusk_lev + 1
                propusk_prv = propusk_prv + 1
                pribul_same = pribul_same + 0.23
        # print(steps,'old:',old_key, ' key:',key1, '--- sam: ', same, ' lev: ', levo, ' prv: ', pravo, ' nol: ', nolik)
        old_key = key1
        # print(steps, ' sam_summa ', propusk_sam, ' lev_summa ', propusk_lev, ' prv_summa ', propusk_prv)
        print('pribul_same:',pribul_same -10 )
        if ((pribul_same -10)< - 1.9) or ((pribul_same -10)>1.7):
            konec = True
        if not konec:
            propusk_sam2 = propusk_sam
            pribul_same2 = pribul_same -10

    print('111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    global_pribul_same = global_pribul_same + pribul_same2
    print('pribul: ',pribul_same2 )
    same_list.append(same)
    lev_list.append(levo)
    prav_list.append(pravo)
    print(naime_file)
    pribul = pribul+ propusk_sam2
print('---------------------------------------')
# same_list.sort()
# lev_list.sort()
# prav_list.sort()
# same_list.reverse()
# lev_list.reverse()
# prav_list.reverse()
print('same: ', same)
print('levo: ', levo)
print('pravo: ', pravo)
print('nolik: ', nolik)
print('dub_nolik: ', dub_nolik)
print('pribul same: ', pribul)
print('global_pribul_same: ',global_pribul_same )
# print('pribyl2: ', pribyl2)
# print('real_pribyl_all: ', real_pribyl)
