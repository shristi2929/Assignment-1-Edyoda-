even_count=0
odd_count=0
list=[1,2,3,4,5,6,7,8,9]
for n in list:
    if n%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("count of even number:",even_count)
print("count of odd numbers:",odd_count)