# Write code with santuy
# ./SultanRajaMarlindo
import base64
import os
import time
import datetime
import pyfiglet
from pyfiglet import Figlet


def encode64():

    # -> Encode Aman URL dan Nama File Dengan Base64
    print(os.system('cls'))
    cutom = Figlet(font='graffiti')
    print('-' * 50)
    print('\t\t\t{ Baturaja1337 }\n', cutom.renderText("Enco64"))
    print('-' * 50)
    string = input('Masukan Teks :')
    encode = string

    # Main Code
    urlSafeEncode = base64.urlsafe_b64encode(encode.encode("utf-8"))
    urlSafeEncodeStr = str(urlSafeEncode, "utf-8")
    print('Base64 Encode \t:', urlSafeEncodeStr)

    # Output Code
    # path output sesuaikan dengan keinginan anda
    path = r"C:\Users\ASUS\Desktop\Encode64.txt"
    f = open(path,'w')
    f.write(str("Encode Result :"))
    f.write(str(urlSafeEncodeStr))
    f.writelines('\n')
    f.close()
    print('Output in your desktop...')
    input('press any key...')
    print(os.system('cls'))
    return menu()

def decode64():
    # -> Decode Base64
    print(os.system('cls'))
    cutom = Figlet(font='graffiti')
    print('-' * 50)
    print('\t\t\t{ Baturaja1337 }\n', cutom.renderText("Deco64"))
    print('-' * 50)

    # Main Code
    string = input('Masukan Teks :')
    data = base64.standard_b64decode(string)
    print('Base64 Decode \t:', data)

    # Output Code
    # path output sesuaikan dengan keinginan anda
    path = r"C:\Users\ASUS\Desktop\Decode64.txt"
    f = open(path, 'w')
    f.write(str("Decode Result :"))
    f.write(str(data))
    f.writelines('\n')
    f.close()
    print('Output in your desktop...')
    input('press any key...')
    print(os.system('cls'))
    return menu()

def menu():
    globals()
    cutom = Figlet(font='graffiti')
    waktu = datetime.datetime.now()
    print('-' * 50)
    print('\t\t\t{ Baturaja1337 }\t', waktu.strftime('%d'), waktu.strftime('%m'), waktu.strftime('%Y'), '\n', cutom.renderText("Base64"))
    print('-' * 50)
    print('1. Encode Text\n2. Decode Text\n3. Exit')
    cho = int(input("~> "))
    if cho == 1:
        return encode64()
    elif cho == 2:
        return decode64()
    elif cho == 3:
        print('Good bye bro !')
        waktu.sleep(3)
        os.system('exit')
    else:
        print('Restart....')
        input()
        os.system('cls')
        return menu()


if "__name__" == menu():
    main()
