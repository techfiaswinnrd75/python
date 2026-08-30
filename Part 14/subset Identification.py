# Subset Identification

l1 = [10, 20, 30, 40, 50]
l2 = [20, 40, 50, 60]


for i in l2:
    if i not in l1:
        print(f"{l2} is not a subset of {l1}")
        break
else:
    print(f"{l2} is a subset of {l1}")

'''Linear Search'''
# n = int(input("Enter a Number to search: "))

# for i in l1:
#     if n == i:
#         print(f"{n} is found")
#         break

# else:
#     print(f"{n} Not Found")



'''Logic using linear Search'''
# for i in l2:
#     for j in l1:
#         if i == j:
#             break
#     else:
#         print(f"{l2} is not a subset of {l1}")
#         break
# else:
#     print(f"{l2} is a subset of {l1}")


