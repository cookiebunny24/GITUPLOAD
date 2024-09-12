# def find_Missing(arr1, arr2):
#     n1 = len(arr1)
#     n2 = len(arr2)
#
#     for i in range(n1):
#         found = False
#         for j in range(n2):
#             if arr1[i] == arr2[j]:
#                 found = True
#                 break
#         if not found:
#             return arr1[i]  # Return the missing element
#
#     return -1  # Return -1 if no missing element found
#
#
# # Driver Code
# arr1 = [1, 4, 5, 7, 9]
# arr2 = [4, 5, 7, 9]
#
# missing = find_Missing(arr1, arr2)
#
# if missing == -1:
#     print("No missing element")
# else:
#     print(missing)  # Print the missing element


def lostElement(A, B):
    # convert lists into set
    A = set(A)
    B = set(B)

    # take difference of greater set with smaller
    if len(A) > len(B):
        print(list(A - B))
    else:
        print(list(B - A))

    # Driver program

a='my name is kevin'
b='my nam kevin'

A = a
B=b
# A = [4, 5, 7, 9,10]
# B = [4, 5, 7, 9]
lostElement(A, B)