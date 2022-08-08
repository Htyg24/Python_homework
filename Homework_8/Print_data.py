def enum(Info, num):
    for c in range(len(Info)):
        for k in range(1, len(Info[c])):
            if Info[c][0] == f'I{num}':
                print(Info[c][k][1: len(Info[c][k])])


def Print(Info):
    Base_info = Info[0]
    Telephon_info = Info[1]
    Adress_info = Info[2]
    for i in range(len(Base_info)):
        print('')
        enum(Base_info, i)
        enum(Telephon_info, i)
        enum(Adress_info, i)