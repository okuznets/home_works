                                    #1 homewrok #1, strings
#1
intro_name = input('Введите имя :')
intro_age = str(input('Введите возраст :'))
intro_gender = input('Укажите пол :')

#2
var_name_conc = 'Hello! My name is ' + intro_name + '. '
var_age_conc = 'I\'m ' + intro_age + '-years old '
var_gender_conc = 'and I\'m a ' + intro_gender + '.'
var_conc = var_name_conc + var_age_conc + var_gender_conc
print(f'2: {var_conc}')

#3
var_format_percent = 'Hello! My name is %s. I\'m %s-years old and I\'m a %s.' % (intro_name, intro_age, intro_gender)
print(f'3: {var_format_percent}')

#4
var_format = 'Hello! My name is {}. I\'m {}-years old and I\'m a {}.'.format(intro_name, intro_age, intro_gender)
print(f'4: {var_format}')

#5
about_me_fstring = f'Hello! My name is {intro_name}. I\'m {intro_age}-years old and I\'m a {intro_gender}.'
print(f'5: {about_me_fstring}')

#6
index1 = about_me_fstring.index('!')+1
s1 = about_me_fstring[:index1]
index2 = about_me_fstring.index('.')+1
s2 = about_me_fstring[index1+1:index2]
s3 = about_me_fstring[index2+1:]
print(f'6: s1=\'{s1}\', s2=\'{s2}\', s3=\'{s3}\'')

#6 - альтернативный метод:
import re
string_splitted = re.split('([!|.*])', about_me_fstring)
s2_1 = string_splitted[0] + string_splitted[1]
s2_2 = string_splitted[2] + string_splitted[3]
s2_3 = string_splitted[4] + string_splitted[5]
# print(s2_1, s2_2, s2_3)

#7
friend_name = 'Alex'
friend_age = '24'
friend_gender = 'male'
friend_string = about_me_fstring.replace(intro_name, friend_name).replace(
    intro_age, friend_age).replace(intro_gender, friend_gender).replace('My name', 'My friend\'s name').replace(
    'I\'m', 'He is')
print(f'7: {friend_string}')

#8
list_from_str = list(about_me_fstring)

#9
print(f'9: {type(list_from_str)}')

#10
str_from_list = ''.join(list_from_str)
print(f'10: {str_from_list}')

#11
swapped_string = about_me_fstring.swapcase()
print(f'11: {swapped_string}')




