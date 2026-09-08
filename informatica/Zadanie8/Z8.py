#https://education.yandex.ru/ege/inf/task/ddc54ae6-f1ac-46ef-8a7b-15dd11634375
# from itertools import permutations
# for _ in permutations('bpg', 3):
#     print(_)


# https://education.yandex.ru/ege/inf/task/6420d873-dfac-4b7d-a0ff-4f1762b24476
# from itertools import product
# lists=['A','И','M','Р','Я',]
# count=0
# for _ in product(lists, repeat=4):
    # count +=1
    # print(count,''.join(_))
    # if count==211:
        # break

#https://youtu.be/BudEmjf_RvM?si=7s5ozK-NrMLMGcgy
# from itertools import product

# k=0
# for i in product('ЭТАН', repeat=5):
#     slovo = ''.join(i)
#     if (slovo.count('Э') + slovo.count('А')) == 1:
#         k += 1
# print (k)

# from itertools import product
# k=0

# for i in product('0123456', repeat=5):
#     number= ''.join(i)
#     if number[0] != '0':
#         if number.count('6') == 1:
#             if number[0] != number[1] != number[2] != number[3] != number[4]:
#                 k += 1
# print (k)

# from itertools import product
# k=0
# for i in product('0123456789ab', repeat=5):
#     number= ''.join(i)
#     if number[0] != '0':
#         if number.count('7') == 1:
#             if (number.count('9') + number.count('a') + number.count('b')) <=3:
#                 k += 1
# print (k)


# from itertools import product, permutations
# k=0
# for i in permutations(range(10), 4):
#     if i[0] != 0:
#         if i[0] % 2 != i[1] % 2 != i[2] % 2 != i[3] % 2:
#             k += 1
    

# print (k)

# from itertools import product
# number=0
# for i in product(sorted('БАТЫР'), repeat=5):
#     slovo = ''.join(i)
#     number +=1
#     if slovo.count('Ы') == 0 and slovo.count('АА') == 0:
#         print(number)
#         break

# from itertools import product
# number=0
# for i in product(sorted('ЛАЙМ'), repeat=5):
#     slovo = ''.join(i)
#     number +=1
#     if slovo.count('М') <=1 and slovo.count('ЛЛ')==0:
#         print(number)


# from itertools import product
# number=0
# for i in product(sorted('СТРОКА'), repeat=5):
#     slovo = ''.join(i)
#     number +=1
#     if number % 2 == 0 and slovo[0] not in 'АСТ' and slovo.count ('О') == 2:
#         print (number)




#Практика в яндексе
#https://education.yandex.ru/ege/inf/training/8/task/1?examTaskId=7e0b4dbb-b87d-4f1a-80e3-fdf2a1a50a3e&examTaskNumber=8&solveLinked=true&categoryId=ed62f12f-ceed-4bde-a9f4-a7418677f2fa&categoryId=cb6e105f-1d6a-43fb-8a80-51dd775a3188&from=main
# 216, но ответ нужно отнимать 2, т.е. 214
# from itertools import product
# k=0
# for i in product('АКЛМНЯ', repeat=5):
#     slovo= ''.join(i)
#     if slovo.startswith('МН'):
#         k+=1
#         print (k, slovo)

#https://education.yandex.ru/ege/inf/training/8/task/2?examTaskId=7e0b4dbb-b87d-4f1a-80e3-fdf2a1a50a3e&examTaskNumber=8&solveLinked=true&categoryId=ed62f12f-ceed-4bde-a9f4-a7418677f2fa&categoryId=cb6e105f-1d6a-43fb-8a80-51dd775a3188&from=main
#1003, ответ
# from itertools import product
# k=0
# for i in product('ИНЬЮ', repeat=5):
#     slovo = ''.join(i)
#     k+=1
#     if slovo.count('И') + slovo.count('Ю')==2:
#        last_k= k
# print(last_k)