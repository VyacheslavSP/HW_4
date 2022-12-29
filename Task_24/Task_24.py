import random
class MyError(Exception):
    def __init__(self, text):
        self.txt = text
while(True):
    try:
        N = int(input("Введите количество кустов N: "))
        if(N<3):                # искуственно ограничил 3 кустами, иначе какие то модули не собирают
            raise ValueError
        bushes = list(random.randint(0, 256) for i in range(N))
        break
    except ValueError:
        print("Некорректный ввод кустов")

print('На кустах выросли ягоды ', bushes)
try:
    file1 = open("bush.txt", "r")
    bush = int(file1.readline())
    if(not(1<=bush<=N)):
        raise MyError("такого куста нет на грядке")
    elif(bush==len(bushes)):
        right_neighbour=0
        left_neighbour=bush-2
    elif(bush==0):
        left_neighbour=len(bushes)
        right_neighbour=bush
    else:
        left_neighbour=bush-2
        right_neighbour=bush
    print('находимся непосредственно перед ',bush, 'кустом ')
    berries_count = list()
    berries_count.append(bushes[left_neighbour] + bushes[bush-1] + bushes[right_neighbour])
    print('за один заход находясь перед ',str(bush), 'кустом можно собрать ягод: ', max(berries_count))
except MyError as mr:
        print(mr)
except ValueError:
        print("в текстовом файле некорректный номер куста")
# если убрать искуственное ограничение в 3 куста тогда  append необходимо выделять отжельно, при этом проверяя что левый сосед!=правому соседу
# или наоборот(при их наличии) и в зависисости от результата складывать, лобо просто вручную прописать варианты для 1 и 2х кустов

