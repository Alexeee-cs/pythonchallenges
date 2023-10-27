import random
array = [random.randint(0, 100) for i in range(51)]
print('maximum is:',round(max(array),2))
print('minimum is:',round(min(array),2))
mean = sum(array)/50
print('mean average is:',round(mean,2))
