import math

standard_list = [1, 2, 3, 4, 5]
reversed_list = [5, 4, 3, 2, 1]

sum_list = sum(standard_list)
sum_reversed_list = sum(reversed_list)

print(f"The sum of the list is : {sum_list}")
print("")

print(f"The sum of the reversed list is : {sum_reversed_list}")
print("")

product_list = math.prod(standard_list)
product_reversed_list = math.prod(reversed_list)

print(f"The product of the list is : {product_list}")
print("")

print(f"The product of the reversed list is : {product_reversed_list}")
print("")
