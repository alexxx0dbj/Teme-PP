

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('testcod.txt') as file:
        x = file.read()
# f = open("readme.txt","r")
# x=f.read()

x = x.replace('!', '')
x = x.replace('?', '')
x = x.replace('.', '')
x = x.replace(',', '')
x = x.replace(':', '')
x = x.replace(';', '')
x = x.replace('\'', '')
x = x.replace('\"', '')

aux_string2 = ""
#if low letters->erase them
for w in x:
    if w.islower() == False:
        aux_string2 = aux_string2 + w

aux_string = ""
for i in range(len(aux_string2)):
# in case I have 3 consecutive spaces and a character => first two spaces will be erased
    if aux_string2[i] != ' ' or aux_string2[i + 1] != ' ':
        aux_string = aux_string + aux_string2[i]

print(aux_string)

file.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/