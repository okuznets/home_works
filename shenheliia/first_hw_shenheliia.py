name = input('your name')
age = input('your age')
sex = input('your sex')

name1 = input('your name1')
age1 = input('your age2')
sex1 = input('your sex3')

text = ('Hello, my name is ' +  name + '. Im ' + age + ' and Im a ' + sex + '.')
text1 = ('Hello, my name is %s.' % name + 'Im %s.' % age + 'Im %s.' %sex)
text2 = ('Hello, my name is {}. Im {}. Im {}'.format(name, age, sex))
about_me_fstring = (f'Hello, my name is {name}. Im {age}. Im {sex}.')

about_me_fstring1 = (about_me_fstring[:25])
about_me_fstring2 = (about_me_fstring[26:32])
about_me_fstring3 = (about_me_fstring[33:])

about_frnd_fstring = (f'Hello, my name is {name1}. Im {age1}. Im {sex1}.')

list_ftom_str = about_me_fstring.split()
print(list_ftom_str)

type(list_ftom_str)
print(type(list_ftom_str))


str_from_list = (' '.join(list_ftom_str))

text3 = (about_me_fstring.swapcase())
print(text3)