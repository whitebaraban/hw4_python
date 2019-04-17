# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

numbers_list = [1, 2, 4, 0]
new_numbers_list = [x**2 for x in numbers_list]
print(new_numbers_list)

second_new_numbers_list = []
for i in numbers_list:
    second_new_numbers_list.append(i**2)
print(second_new_numbers_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

first_fruits_list = ['apple', 'orange', 'banana']
second_fruits_list = ['apple', 'kiwi', 'banana']

new_fruits_list = [x for x in first_fruits_list if x in second_fruits_list]
print(new_fruits_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

numbers_lst = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 0]
new_numbers_lst = [x for x in numbers_lst if x % 3 == 0 and x % 4 != 0 and x >= 0]
print(new_numbers_lst)
