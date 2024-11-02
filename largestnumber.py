#to find the largest number in a list
def largest(x):
    max=x[0]
    for i in x:
        if i>max:
            max=i

    return max
a=[5,8,9,7]
print(largest(a))
