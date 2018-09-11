#Написать скрипт который выполняется только интерпретатором.
#Скрипт должен принимать от пользователя список покупок, пока пользователь не введёт слово 'готово'.
#После этого скрипт должен вывести на экран пронумерованный список.
if __name__ == '__main__':
    print('Run as script.')
 #   user_input = input('Enter a number: ')
 #   print(f'You\'ve entered: {user_input})

user_input = input('add any purchase: ')
shopping_list = []
if user_input == 'done':
    print('shopping list is empty')
else:
    while user_input != 'done' :
    	shopping_list.append (user_input)
    	print('purchase is added, to complete - enter "done"')
    	user_input = input('add any purchase: ')
for j in range(len(shopping_list)):
        print('purchase ', j, ': ', shopping_list[j])