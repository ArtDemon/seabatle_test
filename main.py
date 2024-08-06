import random as rnd


# сгенерировать пустое поле  из двумерного массива


# config = {
#     vertical_range: 10,
#     horizontal_range: 10,
# }

# vertical = config['vertical_range']


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
        if x <= item[0] + 1 and x >= item[0] - 1:
            if y <= item[1] + 1 and y >= item[1] - 1:
                # debug
                # print (x,y, 'совпадает с ', item[0],item[1])
                proverka = False
                break
        else:
            proverka = True
            # debug
            # print(x, y, 'не совпадает с ', item[0], item[1])
            # print(cart)
    return proverka


def generator_korabley(yacheiki):
    x = 1
    cart = set()
    korabl_x_nach = rnd.randint(0, 9)
    korabl_y_nach = rnd.randint(0, 9)
    cart.add((korabl_x_nach, korabl_y_nach))
    napravlenie = hor_vert_rnd()
    # if proverka_yacheeck3x3(korabl_x_nach,korabl_y_nach,cart) == True:
    #     cart.add(korabl_x_nach, korabl_y_nach)
    #     print (cart)
    if napravlenie == 1:  # vertical
        while yacheiki != 0:
            korabl_y_nach = korabl_y_nach + x
            if proverka_yacheeck3x3(korabl_x_nach, korabl_y_nach, cart):
                cart.add((korabl_x_nach, korabl_y_nach))
                yacheiki -= 1
                x += 1
            else:
                while yacheiki != 0:
                    korabl_y_nach = korabl_y_nach - x
                    if proverka_yacheeck3x3(korabl_x_nach, korabl_y_nach, cart):
                        cart.add((korabl_x_nach, korabl_y_nach))
                        yacheiki -= 1
                        x += 1
    else:
        while yacheiki != 0:
            korabl_x_nach = korabl_x_nach + x
            if proverka_yacheeck3x3(korabl_x_nach, korabl_y_nach, cart):
                cart.add((korabl_x_nach, korabl_y_nach))
                yacheiki -= 1
                x += 1
            else:
                while yacheiki != 0:
                    korabl_x_nach = korabl_x_nach - x
                    if proverka_yacheeck3x3(korabl_x_nach, korabl_y_nach, cart):
                        cart.add((
                            korabl_x_nach, korabl_y_nach))
                        yacheiki -= 1
                        x += 1
    return list(cart)


def start_game():
    pole_AI = generiryi_pole()
    list_cart = generator_korabley(3)
    for x in list_cart:
        pole_AI[x[0]][x[1]] = '$'

    for item in pole_AI:
        print(item)


start_game()
