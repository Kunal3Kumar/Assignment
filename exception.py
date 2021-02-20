def fun(obj, index):
    print('value at position {} is {}'.format(index,obj[index]))

L = [10,20,25,30,23]
try:
    fun(L,12)
except indexError :
    print('got exception')
print('end of the program')