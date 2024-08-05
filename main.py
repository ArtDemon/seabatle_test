import random as rnd
# сгенерировать пустое поле  из двумерного массива
def generiryi_pole():
    return [[0 for _ in range(10)] for _ in range(10)]


def hor_vert_rnd():
    vertical=(1)
    horizontal=(2)
    rnd.choice([vertical, horizontal])

# 10 рандомных значений(зачем?) я хуй знает, Вова сказал
def cortegei_10_RND_s_proverkoi():
    cart=set()
    korabl_4_1 = rnd.randint(0,9)
    korabel_4_2 = rnd.randint(0,9)
    cart.add((korabl_4_1,korabel_4_2))

    rotate = hor_vert_rnd()
    if rotate == 1:
        if korabl_4_1<5:
            cart.add((korabl_4_1,korabel_4_2))
            cart.add(((korabl_4_1+1),korabel_4_2))
            cart.add(((korabl_4_1 + 2), korabel_4_2))
            cart.add(((korabl_4_1 +3), korabel_4_2))
        else:
            cart.add((korabl_4_1,korabel_4_2))
            cart.add(((korabl_4_1-1),korabel_4_2))
            cart.add(((korabl_4_1 -2), korabel_4_2))
            cart.add(((korabl_4_1 -3), korabel_4_2))
    else:
        if korabel_4_2<5:
            cart.add((korabl_4_1,korabel_4_2))
            cart.add((korabl_4_1,korabel_4_2+1))
            cart.add((korabl_4_1, korabel_4_2+2))
            cart.add((korabl_4_1, korabel_4_2+3))
        else:
            cart.add((korabl_4_1,korabel_4_2))
            cart.add((korabl_4_1,korabel_4_2-1))
            cart.add((korabl_4_1, korabel_4_2-2))
            cart.add((korabl_4_1, korabel_4_2-3))

    while len(cart)!=9:
        proverka = False
        x = rnd.randint(0, 9)
        y = rnd.randint(0, 9)
        for item in cart:
            if x <= item[0]+1 and x >= item[0]-1:
                if y <= item[1]+1 and y >= item[1]-1:
                    # debug
                    # print (x,y, 'совпадает с ', item[0],item[1])
                    proverka = False
                    break
            else:
                proverka = True
                # debug
                # print(x, y, 'не совпадает с ', item[0], item[1])
                # print(cart)
        if proverka == True:
            cart.add((x,y))
    print (cart)
    return list(cart)



def start_game():
    pole_AI = generiryi_pole()
    list_cart = cortegei_10_RND_s_proverkoi()
    for x in list_cart:
        pole_AI[x[0]][x[1]] = (9)

    for item in pole_AI:
        print (item)

start_game()














def generui_raspolozhenya_korabley():
    return ()
