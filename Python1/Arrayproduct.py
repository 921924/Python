def product(arr):
    n = len(arr)
    output = [1] * n

    prefix_product = 1
    for i in range(n):
        output[i] *= prefix_product
        prefix_product *= arr[i]

    suffix_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix_product
        suffix_product *= arr[i]

    return output

arr = [1, 2, 3, 4]
output = product(arr)
print(output)  
arr = [4,5,1,8,2]
output = product(arr)
print(output)