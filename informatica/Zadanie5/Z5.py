# #https://education.yandex.ru/ege/inf/training/5/task/1?examTaskId=dc689476-3e8e-4da9-b84a-1b8d5ff5e705&examTaskNumber=5&categoryId=2a75d0c9-0d32-4c9c-a819-09787310235b&categoryId=6e250227-f742-4091-806a-4d76b0bed3d9&categoryId=d1779ac5-b1f8-45a0-8b08-399b18c0720c&from=main
# N=115
# def A(N):
    
#     result=''
#     while N>0:
#         result = str(N%8) + result
#         N //=8
#     filtered=''
#     i=0
    
#     while i<len(result):
#         digit = int(result[i])
        
#         if digit %2 !=0:
#             filtered += result[i]
#         i+=1
    
#     otvet=int(filtered,8)
#     return otvet
# print(A(N))


def system(N):
    result=''
    while N>0:
        result= str(N%4) + result
        N //=4
    return 
print(system(N=2))
    