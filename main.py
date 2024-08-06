import random as rnd

global_ai_set_ships = set()


# сгенерировать пустое поле  из двумерного массива
def generiryi_pole():
    return [[0 for _ in range(10)] for _ in range(10)]


def hor_vert_rnd():
    vertical = 1
    horizontal = 2
    return rnd.choice([vertical, horizontal])


# 10 рандомных значений(зачем?) я хуй знает, Вова сказал
# def cortegei_10_RND_s_proverkoi():
#     cart=set()
#     korabl_4_1 = rnd.randint(0,9)
#     korabel_4_2 = rnd.randint(0,9)
#     cart.add((korabl_4_1,korabel_4_2))
#
#     rotate = hor_vert_rnd()
#     if rotate == 1:
#         if korabl_4_1<5:
#             cart.add((korabl_4_1,korabel_4_2))
#             cart.add(((korabl_4_1+1),korabel_4_2))
#             cart.add(((korabl_4_1 + 2), korabel_4_2))
#             cart.add(((korabl_4_1 +3), korabel_4_2))
#         else:
#             cart.add((korabl_4_1,korabel_4_2))
#             cart.add(((korabl_4_1-1),korabel_4_2))
#             cart.add(((korabl_4_1 -2), korabel_4_2))
#             cart.add(((korabl_4_1 -3), korabel_4_2))
#     else:
#         if korabel_4_2<5:
#             cart.add((korabl_4_1,korabel_4_2))
#             cart.add((korabl_4_1,korabel_4_2+1))
#             cart.add((korabl_4_1, korabel_4_2+2))
#             cart.add((korabl_4_1, korabel_4_2+3))
#         else:
#             cart.add((korabl_4_1,korabel_4_2))
#             cart.add((korabl_4_1,korabel_4_2-1))
#             cart.add((korabl_4_1, korabel_4_2-2))
#             cart.add((korabl_4_1, korabel_4_2-3))
#
#     while len(cart)!=9:
#         proverka = False
#         x = rnd.randint(0, 9)
#         y = rnd.randint(0, 9)
#         for item in cart:
#             if x <= item[0]+1 and x >= item[0]-1:
#                 if y <= item[1]+1 and y >= item[1]-1:
#                     # debug
#                     # print (x,y, 'совпадает с ', item[0],item[1])
#                     proverka = False
#                     break
#             else:
#                 proverka = True
#                 # debug
#                 # print(x, y, 'не совпадает с ', item[0], item[1])
#                 # print(cart)
#         if proverka == True:
#             cart.add((x,y))
#     print (cart)
#     return list(cart)

def proverka_yacheeck3x3(x, y, cort):
    proverka = False
    for item in cort:
        if x == item[0] + 1 or x == item[0] - 1 or x == item[0]:
            if y == item[1] + 1 or y == item[1] - 1 or y == item[1]:
                # debug
                # print (x,y, 'совпадает с ', item[0],item[1])
                proverka = False
                break
        else:
            proverka = True
            # debug
            # print(x, y, 'не совпадает с ', item[0], item[1])
            # print(cort)
    return proverka


def generator_korabley(yacheiki):
    x = 1
    global global_ai_set_ships
    cart = set()
    cart.add((20, 99))
    global_ai_set_ships.add((20, 99))
    korabl_x_nach = rnd.randint(0, 9)
    korabl_y_nach = rnd.randint(0, 9)
    # cart.add((korabl_x_nach, korabl_y_nach))
    # print(cart)
    napravlenie = hor_vert_rnd()
    # if proverka_yacheeck3x3(korabl_x_nach,korabl_y_nach,cart) == True:
    #     cart.add(korabl_x_nach, korabl_y_nach)
    #     print (cart)
    while x > 0:
        if napravlenie == 1:  # vertical
            if proverka_yacheeck3x3(korabl_x_nach, korabl_y_nach, global_ai_set_ships) and proverka_yacheeck3x3(
                    korabl_x_nach, korabl_y_nach + yacheiki, global_ai_set_ships) and korabl_y_nach + yacheiki in range(0, 9):
                # print('proverka proidena')
                for y_smeshenie in range(korabl_y_nach, korabl_y_nach + yacheiki):
                    cart.add((korabl_x_nach, y_smeshenie))
                    x -= 1
                global_ai_set_ships.remove((20, 99))
                cart.remove((20, 99))
                # print(cart)
            else:
                if proverka_yacheeck3x3(korabl_x_nach, korabl_y_nach, global_ai_set_ships) and proverka_yacheeck3x3(
                        korabl_x_nach, korabl_y_nach - yacheiki,
                        global_ai_set_ships) and korabl_y_nach - yacheiki in range(0, 9):
                    # print('proverka proidena2')
                    for y_smeshenie in range(korabl_y_nach - yacheiki, korabl_y_nach):
                        cart.add((korabl_x_nach, y_smeshenie))
                        x -= 1
                    global_ai_set_ships.remove((20, 99))
                    cart.remove((20, 99))
                    # print(cart)

                else:
                    # print('proverka ne proidena')
                    # print (cart)
                    korabl_x_nach = rnd.randint(0, 9)
                    korabl_y_nach = rnd.randint(0, 9)
        else:
            if proverka_yacheeck3x3(korabl_x_nach, korabl_y_nach, global_ai_set_ships) and proverka_yacheeck3x3(korabl_x_nach+ yacheiki, korabl_y_nach , global_ai_set_ships) and korabl_x_nach + yacheiki in range(0, 9):
                # print('proverka proidena')
                for x_smeshenie in range(korabl_x_nach, korabl_x_nach + yacheiki):
                    cart.add((x_smeshenie, korabl_y_nach))
                    x -= 1
                global_ai_set_ships.remove((20, 99))
                cart.remove((20, 99))
                # print(cart)
            else:
                if proverka_yacheeck3x3(korabl_x_nach, korabl_y_nach, global_ai_set_ships) and proverka_yacheeck3x3(korabl_x_nach- yacheiki, korabl_y_nach ,global_ai_set_ships) and korabl_x_nach - yacheiki in range(0, 9):
                    # print('proverka proidena2')
                    for x_smeshenie in range(korabl_x_nach - yacheiki, korabl_x_nach):
                        cart.add((x_smeshenie, korabl_y_nach))
                        x -= 1
                    global_ai_set_ships.remove((20, 99))
                    cart.remove((20, 99))
                    # print(cart)

                else:
                    # print('proverka ne proidena')
                    # print (cart)
                    korabl_x_nach = rnd.randint(0, 9)
                    korabl_y_nach = rnd.randint(0, 9)
    global_ai_set_ships = global_ai_set_ships.union(cart)
    return list(cart)


def start_game():
    pole_ai = generiryi_pole()
    list_corabley = list()
    list_corabley.append(generator_korabley(4))
    for x in range(2):
        list_corabley.append((generator_korabley(3)))
    for x in range(3):
        list_corabley.append((generator_korabley(2)))
    for x in range(4):
        list_corabley.append((generator_korabley(1)))
    # print(global_ai_set_ships, 'ЭТО ГЛОБАЛ')
    for ship in list_corabley:
        for cell in ship:
            pole_ai[cell[1]][cell[0]] = 5
    for item in pole_ai:
        print(item)
    # for item in list_corabley:
    #     print(item)


if __name__ == '__main__':
    start_game()
