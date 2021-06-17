# Реализуйте шифратор и дешифратор по шифру Цезаря.
# Спросить пользователя, что он хочет сделать - зашифровать или расшифровать файл.
# Если зашифровать, попросить у него ввести имя шифруемого файла, имя файла, который мы получим на выходе(зашифрованного) и ключ(ключем будет уроваень сдвига).
# Если расшифровать, попросить ввести имя зашифрованного файла, имя файла на выходе(расшифрованного) и ключ.
import string

alphabet_en_low_or = list(string.ascii_lowercase)
alphabet_en_up_or = list(string.ascii_uppercase)
alphabet_en_or = alphabet_en_low_or+alphabet_en_up_or


def shift_alphabet(shift,flag): # Function is creating alphabet for encryption (flag == '1')  or decryption
    shift = shift%len(alphabet_en_low_or)
    alphabet_en_low_new = []
    alphabet_en_up_new = []
    if flag =='1':
        min_range = -len(alphabet_en_low_or) + shift
        max_range = shift
    else:
        min_range = -shift
        max_range = len(alphabet_en_low_or) - shift
    for i in range(min_range, max_range):
        alphabet_en_low_new.append(alphabet_en_low_or[i])
        alphabet_en_up_new.append(alphabet_en_up_or[i])
    return alphabet_en_low_new + alphabet_en_up_new


def crypto_func(file_inp, file_out): # Function for work with input file
    while True:
        try:
            file_in_gen = (row for row in open(file_inp))
            break
        except IOError:
            file_inp = input(f'File {file_inp} is not exist! please write correct file name:')
    with open(file_out, 'w') as f:
        while True:
            try:
                str_new = ''
                str = next(file_in_gen)
                for i in str:
                    try:
                        str_new += shift_alphabet(shift, choice)[alphabet_en_or.index(i)]
                    except Exception:
                        str_new += i
            except StopIteration:
                print(f'Result is completed in {file_out}')
                break
            f.write(str_new)


while True:
    choice = input('What do you want to do with file: \n 1 - encrypt \n 2 - decrypt \n')
    if choice == '1' or choice == '2':
        inp_file = input('Enter the name of original file:\n')
        out_file = input('Enter the name of resulted file:\n')
        shift = input('Enter a key for your code (int):')
        while True:
            try:
                shift = int(shift)
                crypto_func(inp_file, out_file)
                break
            except ValueError:
                shift = input(f'Your key {shift} is not int! Please enter correct key:')
        break
    else:
        print('Please make correct choice!')

