import string

name = input('enter your name')
age = input('enter your age')
sex = input('enter your gender')

about_me_concat = 'Hello! My name is '+ name +'. I\'m '+ age +' and I\'m a '\
+ sex +'.'
print(about_me_concat)
about_me_percent = 'Hello! My name is %s. ' % name + 'I\'m %s ' % age + \
'and I\'m a %s.' % sex
print(about_me_percent)
about_me_format = 'Hello! My name is {}. I\'m {} and I\'m a {}.'.format(name, age, sex)
print(about_me_format)
about_me_fstring = f'Hello! My name is {name}. I\'m {age} and I\'m a {sex}.'
print(about_me_fstring)

str = about_me_fstring.split('.')
str1 = str[0]
str2 = str[1]
print(str)
print(str1)
print(str2)

name1 = 'Nata'
age1 = 26
sex1 = 'female'
about_my_friend = f'Hello! My friend\'s name is {name1}. She\'s {age1} \
and She\'s a {sex1}.'
print(about_my_friend)

print(type(about_me_fstring))

list_from_str = about_me_fstring.split()
print(list_from_str)

print(type(list_from_str))

str_from_list = ' '.join(list_from_str)
print(str_from_list)
print(type(str_from_list))

print(about_me_fstring.swapcase())
