import random as rnd
# сгенерировать пустое поле  из двумерного массива
def generiryi_pole():
    return [[0 for _ in range(10)] for _ in range(10)]



# 10 рандомных значений(зачем?) я хуй знает, Вова сказал
def cortegei_10_RND_s_proverkoi():
    cart=set()
    cart.add((rnd.randint(0,9),rnd.randint(0,9)))
    while len(cart)!=10:
        proverka = False
        x = rnd.randint(0, 9)
        y = rnd.randint(0, 9)
        for item in cart:
            if x <= item[0]+1 and x >= item[0]-1:
                if y <= item[1]+1 and y >= item[1]-1:
                    # print (x,y, 'совпадает с ', item[0],item[1])
                    proverka = False
                    break
            else:
                proverka = True
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
        pole_AI[x[0]][x[1]] = (7)

    for item in pole_AI:
        print (item)

start_game()














def generui_raspolozhenya_korabley():
    return ()
