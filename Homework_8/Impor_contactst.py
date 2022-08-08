from Add_contact import Add_contact

def Start_add_contacts(file_name:str = 'dossier.txt'):
    Info = [
    [[]],
    [[]],
    [[]]
    ]
    with open(file_name, 'r', encoding='UTF-8') as h:
        l = h.readline()
        while l != '':
            info = l.split(',')
            Add_contact(info, Info)
            l = h.readline()

    return Info

