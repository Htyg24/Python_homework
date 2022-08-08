def New_contact(Info):
    contact = 'N' + input('Введите ФИО')
    contact += ',T' + ',T'.join(input('Введите телефоны').split())
    contact += ',B' + input('Введите дату рождения')
    contact += ',B' + input('Введите отдел')
    contact += ',A' + input('Введите адрес') + '\n'
    contact = contact.split(',')
    return Add_contact(contact, Info)



def Add_contact(info, Info):
    i = len(Info[0]) - 1
    Info[0][i].append(f'I{i}')
    Info[1][i].append(f'I{i}')
    Info[2][i].append(f'I{i}')
    Info[0].append([])
    Info[1].append([])
    Info[2].append([])
    for text in info:
        if text[0] == 'N' or text[0] == 'B' or text[0] == 'O' or text == 'B':
            Info[0][i].append(text)
        elif text[0] == 'T':
            Info[1][i].append(text)
        elif text[0] == 'A':
            Info[2][i].append(text[0: -1])
    return Info
