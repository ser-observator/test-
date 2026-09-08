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


from itertools import product
k=0
for i in product('0123456789', repeat=4):
    number = ''.join(i)
    if number[0] != '0':
        if len(set(number)) == len(number):
            number = number.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')
            number = number.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
            if number.count ('00') == 0 and number.count('11')==0:
                k += 1
print (k)