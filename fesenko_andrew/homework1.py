import string

print('Hi! What\'s your name?')
name = input('My name is:')
print(name, ', enter your age.')
age = input('My age is:')
print('Who are you:')
sex = input('My gender is:') #1 (done)

about_me_fstring = ('Hello, my name is ' +  name + '. I\'m ' + age + ' and I\'m a ' + sex + '.')    #2 (done)
print(about_me_fstring)

about_me_fstrin_1 = ('Hello, my name is %s' % name + '. I\'m %s' % age + ' and I\'m a %s' % sex + '.')  #3 (done)
print(about_me_fstrin_1)

about_me_fstring_2 = 'Hello, my name is {0}. I\'m {1} and I\'m a {2}.'.format(name, age, sex)    #4 (done)
print(about_me_fstring_2)

about_me_fstring_3 = f'Hello, my name is {name}. I\'m {age} and I\'m a {sex}.'    #5 (done)
print(about_me_fstring_3)

# 6 (done)

print('What\'s your friend\'s name?')
name_f = input('His/Her name:')
print(name, ', enter your friend\'s age.')
age_f = input('His/Her age:')
print('Who is your friend:')
sex_f = input('His/Her gender:')
about_friend_fstring = f'He/She is {name_f}. He/She is {age_f} and he/she is a {sex_f}.' #7 (done)
print(about_friend_fstring)

list_from_str = list(about_me_fstring_3)    #8 (done)
print(list_from_str)

print(type(list_from_str))  #9 (done)

str_from_list = ''.join(list_from_str)   #10 (done)
print(str_from_list)

print(about_me_fstring_3.swapcase())    #11 (done)