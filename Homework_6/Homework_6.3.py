# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

file_to_code = 'read_file.txt'
file_to_decode = 'write_file.txt'
file = open(file_to_code, 'r')

massage = file.read()
print (massage)
last_simbol = massage[0]
text = ""
count = 0
code = []
for i in massage:
    if i == last_simbol:
        count += 1
    else:
        text += last_simbol + str(count)
        last_simbol = i
        count = 1
text += last_simbol + str(count)
print(text)
file = open(file_to_decode, 'w')
file.write(text)
file.close()

decode = ''
for i in range(0, len(text), 2):
    for c in range(int(text[i + 1])):
        decode += text[i]
print(decode)



