# Задание 1

# my_list = [2, 3, 5, 9, 3]
# print(sum(my_list[1::2]))

# 2.
 
# my_list = [2, 3, 4, 5, 6]
# itog_list = []
# for i in range((len(my_list)+1)//2):
#     itog_list.append(my_list[i]*my_list[len(my_list)-1-i])
# print(itog_list)

# 3. 

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in my_list:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)  
# print(max-min)