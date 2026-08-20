#https://education.yandex.ru/ege/inf/task/d3bde6f0-4eae-4994-bb5d-f757607b9d5f
# import ipaddress

# def ip_to_int(ip: str) -> int:
#     return int(ipaddress.IPv4Address(ip))

# ip1 = "118.187.59.255"
# ip2 = "118.187.65.115"

# a = ip_to_int(ip1)
# b = ip_to_int(ip2)

# x = a ^ b  # биты, где IP отличаются
# if x == 0:
#     cp = 32  # совпали полностью (в задаче такого нет)
# else:
#     # длина общего префикса (сколько старших бит совпадает)
#     p = x.bit_length() - 1          # позиция старшего отличающегося бита (от 0 снизу)
#     cp = 31 - p                     # из 32 бит -> сколько слева совпало

# k_max = 30  # т.к. в подсети должны быть минимум: адрес сети и broadcast зарезервированы
# # нужно: k > cp и k <= k_max, максимально возможное k
# ans = k_max if cp < k_max else min(k_max, cp + 1)

# print(ans)




#https://education.yandex.ru/ege/inf/task/4cb38e00-cf16-4ae7-bf88-9a33e46ff749
#решено ии, тяжело было понимать

# from ipaddress import ip_network

# net = ip_network("123.222.99.192/255.255.255.248", strict=False)

# count = 0
# for ip in net:  # включает network и broadcast
#     ones = int(ip).bit_count()
#     if ones > 16:
#         count += 1

# print(count)