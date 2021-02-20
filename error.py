#-----Rise exception------
# try:
#     print('raise exception')
#     raise IndexError
# except IndexError:
#     print('caught exception')

#--------user defin exception -------
# class acd(Exception):
#     pass

# try:
#     print('user defined exception')
#     raise acd
# except acd:
#     print('exception caugth')

#-----------try / except / else statement--------
# try:
#     a = 10
#     b = 20 
#     print(a+b) # b = c
#     l = [10,12,34,35]
#     print(l[5]) # 5 = 10
# except NameError:
#     print('name error happened ')
# except IndexError:
#     print('out of index error')
# except(NameError,IndexError):
#     print('multiple')
# else:
#     print('no error occur')
# finally:
#     print('must call')

#--------Q1---------
# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

# total_likes = 0

# for post in blog_posts:
#           total_likes = total_likes + post['Likes']

#-----Q2------
# food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "ghee", "lox", "lemonade"]
# fifth = []

# for x in food:
#     try:
#         fifth.append(x[4])
#     except IndexError:
#        # print('got exception')
#        pass
   
# print(fifth)

Add exception handling to the get_value() function so that it, if an IndexError exeception occurs because the specified index does not exist, the function returns the keyword None. Do not handle any other types of exceptions.
def get_value(data_list, index):
    return data_list[index]

# Sample list data
my_list = ['a', 'b', 'c']
Calculate the log base ten of each value in xvals and store the result in a list called solution. Use exception handling to skip any calculations that produce math domain errors.
xvals = (0.8, -0.1, 0.9, -0.1, 0.1, 0.30000000000000004, -0.1, 0.5, 1.0, -0.1, 0.9, 0.9, 0.1, 1.0, 0.2, 0.2, 0.1, 0.9, 0.0, 1.0)
solution = []

for log 10 calculation:
import math
result=math.log10(x)