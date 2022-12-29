import random
number_arr_first=[]
number_arr_second=[]
result_arr=[]
while(True):
    try:
        n=int(input("Введите кол-во элементов первого массива: "))
        m=int(input("Введите кол-во элементов второго массива: "))
        if(n<1 or m<1):
            raise
        for i in range (n):
            number_arr_first.append(random.randint(-128,128))           # пускай будет sbyte. 
        for i in range (m):
            number_arr_second.append(random.randint(-128,128))
        break
    except:
        print("неккоректный ввод элементов")
print(number_arr_first)
print(number_arr_second)
if(n<m):                                            #небольшая попытка оптимизации. проходиться нужно по списку с меньшей длиной. также переменные number_arr теперь задублированы а значит уже не нужны
    arr_min_len=number_arr_first
    arr_max_len=number_arr_second
else:
    arr_min_len=number_arr_second
    arr_max_len=number_arr_first
del number_arr_first
del number_arr_second
for i in range(len(arr_min_len)):
    if(arr_max_len.count(arr_min_len[i])>0 and not(any([x==arr_min_len[i] for x in result_arr]))): ##условие конечно получилось длинным и трудно читаемым,зато оно одно
        result_arr.append(arr_min_len[i])
if(len(result_arr)==0):
    print("совпадений в массиве нет")
else:
    result_arr.sort()
    print(f'массив совпадений = {result_arr}')        
# задача выполняется, однако попытался написать так коротко как смог. по хорошему, т.к. any под капотом постоянно разворачивает список
# для лучшей производительности корректней было бы сделать так- сначала создаем  временный массив куда складываем все совпадения с 
# повторениями а затем удаляем дубликаты проходясь по всему списку (например так result_arr_without_repit = list(set(result_arr)) или создав времееный массив
# с условим заполнения if x not in temp:)