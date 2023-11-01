# # # def prime_numbers(n):
# # #   primes = []
# # #   for i in range(2, n + 1):
# # #     if not any(i % j == 0 for j in range(2, int(i**0.5) + 1)):
# # #       primes.append(i)
# # #   return primes
# # # if len(prime_numbers(int(input()))) % 2 == 0:
# # #   print('Bobur')
# # # else:
# # #   print('Ali')




# # a = list(map(int, input()))
# # x1, v1, x2, v2 = a[0], a[1], a[2], a[3]
# # if abs(x1 - v1) - abs(x2 - v2) == 1:
# #   print('YES')
# # else:
# #   print('NO')




# x1 = 1
# # v1 = 3
# # x2 = 6
# # v2 = 2
# # i = 0
# # while x1 != x2:
# #     x1 += v1
# #     x2 += v2
# #     i += 1
# # print(x1, x2, i)

# def find_n(a):
#   """Returns the value of n that satisfies the condition a^10 + 1 = 0 (mod 10)."""
#   for n in range(1, 10):
#     if (a**10 + 1) % 10 == 0:
#       return n
#   return None

# # Find the values of n that satisfy the condition a^10 + 1 = 0 (mod 10) for a = 1, 2, 3, ..., 9.
# n_values = []
# for a in range(1, 10):
#   n = find_n(a)
#   if n is not None:
#     n_values.append(n)

# # Print the values of n.
# print(n_values)

