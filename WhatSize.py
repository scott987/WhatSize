import sys
from os import system

file_size_correct = False
file_size = input("Please input file size you want(can use 'KB' or 'MB', no for bytes):")
while not file_size_correct :
    if file_size.isdigit():
        file_size = int( float( file_size ) )
        file_size_correct=True
    elif "K" in file_size.upper():
        if file_size.upper().replace('.','',1).replace('KB','',1).replace('K','',1).isdigit():
            file_size = int(float(file_size.replace('KB','',1).replace('K','',1))*1024)
            file_size_correct=True
    elif "M" in file_size.upper():
        if file_size.upper().replace('.','',1).replace('MB','',1).replace('M','',1).isdigit():
            file_size = int(float(file_size.replace('MB','',1).replace('M','',1))*1024*1024)
            file_size_correct=True

    if not file_size_correct:
        file_size = input("input wrong!\nPlease input correct size(can use 'KB' or 'MB', no for bytes):")

file_name = input("Please input the output file name(default:foo):")

if file_name == "":
    file_name="foo"

file = open(file_name,'w')

ten_percent = 10

if file_size < 100:
    str_len = 1
elif file_size < 1000:
    str_len = 100
else:
    str_len = 1000

rest = file_size
while rest > 0:
    if rest > str_len:
        file.write(chr(0)*str_len)
        rest -= str_len
    else:
        file.write(chr(0)*rest)
        rest -= rest
    
    finish_rate = 100-100*(float(rest)/file_size)
    if finish_rate >= ten_percent :
        if sys.platform == "win32":
            system("CLS")
        else:
            system("clear")
        print("Total bytes:"+str(file_size))
        print(str( round(finish_rate,2) )+"%")
        ten_percent += 10


file.close()
print("Complete !")
input("input any key to exit....")
exit()