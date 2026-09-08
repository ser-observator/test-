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
from itertools import product

k=0
for i in product('ЭТАН', repeat=5):
    slovo = ''.join(i)
    if (slovo.count('Э') + slovo.count('А')) == 1:
        k += 1
print (k)