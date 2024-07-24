"===============Циклы================================"
 # цикл - это блок кода который отрабатывает несколько раз 
 # for - цикл, который работает с итерируемым обьектом. Цикл заканчивает работу когда он доходит до последнего элемента итерируемого обьета
  # while- цикл который работает до тех пор пока условие верное


# list_ = ['hello world', 1, 2, 3, 4, None, False, True, [1,2,3]]

# for element in list_:
#     print(element)

# for letter in 'hello world':
#     print(letter)

# n = 1
# while n >=10:
#     print(n)
#     # n = n + 1
#     n += 1
# # 1 2 3 4 5 6 7 8 9 10

# n = 0
# while n:
#     n+=1
#     print(0)
    # не запустится потому что 0 это False

"=====================операторы break/continue============================="
#break-полностью прерывает работу цикла (выйти из цикла)
#continue - пропускает 1 итерацию и переходит к следующей
# for i in range(10):
#     if i == 3:
#         continue
#     print(i)
#     # 0 1 2 4 5 6 7 8 9

# for i in range(10):
#     print(i)
#     if i == 3:
#         continue
#     # 0 1 2 3 4 5 6 7 8 9 

# for i in range (10):
#     print(i)
#     if i == 3:
#         break
#     # 0 1 2 3

# for i in range(10):
#     print(i)
#     break
# # 0

# for torokul in range(10):
#     if torokul == 3:
#         break
#     print(torokul)
#     # 0 1 2

# for i in range(10):
#     if i < 3:
#         continue
#     print(i)
    # 3 4 5 6 7 8 9 
    
# list1 = [1,1,1,1,2,3,4,5,1,59,1,1]
# new_list = []

# for num in list1:
#     # if num == 1:
#     #     continue
#     # new_list.append(num)
#     if num !=1:
#         new_list.append(num)
# print(new_list)
# # одно и тоже выведится просто условие разные
# list1 = [1, 1, 1, 1, 2, 3, 4, 5, 1, 59, 1, 1]

# while 1 in list1:
#     list1.remove(1)
# print(list1)
# #[2, 3, 4, 5, 59]

# for i in range(10):
#     for j in range(10):
#         print(i,j)

"=================== 0 exercise ==================="
#for i in range(1,11):
#    print(i)

# a = 1

# while a < 11:
#     print(a)
#     a = a+1
# print('Цикл окончен')

"===================1 exercise ========================"
# for i in range(0,21,2):
#     print(i)

# n = 0

# while n < 21:
#      print(n)
#      n = n+2
# print('Цикл окончен')

"===================2 exercise==================="
# for i in range(0,101,3):
#     print(i)

# n = 0
# while n < 101:
#     print(n)
#     n += 3

'=====================3 exercise========================'
# new_list = []
# for i in range(0,100,15):
#     new_list.append(i)
#     print(new_list)

# new_list = []
# n = 0
# while n <= 85:
#     n += 15
#     new_list.append(n)
#     print(new_list)

'=======================4 exercise ================='
# for i in range(0,101,18):
#     print(i)
    

# n = 0
# while n < 101:
#     print(n)
#     n += 18

'======================5 exercise===================='

# for i in range(0,300,2):
#     if i >= 237:
#         break
#     print(i)

# n = 0
# while n <= 300:
#     if n >= 237:
#         break
#     print(n)
#     n += 2

"======================6 exercise========================"
# new_list = "Ботнет IPStorm, в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем"

# for i in new_list:
#     if i.isdigit():  
#         n = int(i)  
#         result = n * 2  
#         print(i)

"==================7 exercise =========================="
# new_list = "20210419-2021071914424/..H/][[102e//==::'/:13-=---1234l][23-13lo31w323'/.,,o32r;;ld"

# for i in new_list:
#     if i.isalpha():
#         n = str(i)
#         print(f)
"==========================8 exercise==================="
# for i in range(5,0,-1):
#     print(i)

"======================9 exercise=================="
# for i in range(1, 8): 
#     print(i**2)
