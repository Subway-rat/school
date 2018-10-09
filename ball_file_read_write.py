#-*- codeing: utf-8 -*-
def read_file(data):
    '''
    leser all data i en fil.
    data er en string.
    output er en tuppel med v0 og t liste.
    '''
    file = open(data,'r')
    v0 = float(file.readline().split()[1])
    file.readline() #hopper over en linje som ikke er viktig.
    t = []
    for n in file: #leser relevante linjer
        t += [float(i) for i in n.split()]
    file.close()
    return v0, t 

def test_ball():
    '''
    lager en testfil med bestemte variabler
    og deretter skjekker om de er det samme
    '''
    v0 = 5.0
    t = [0.45,0.12,'\n',0.4,0.6,'\n',0.7,0.2] #test variabler
    test_file = open('test_ball.dat','w') #lager filen
    test_file.write('v0: ' + str(v0) + '\n')
    test_file.write('t:\n')
    for s in t:
        test_file.write(str(s) + ' ')
    test_file.close()
    file = read_file('test_ball.dat')
    listr = tuple([str(v0),t]) #Gjør listene ekvivalente
    listr[1].remove('\n') #fjerner unødvendige linjeskift
    test1 = (str(listr[0]) == str(file[0])) #tester første element
    test2 = (listr[1] == file[1]) #tester listen
    assert test1, test2

def print_file(data, boolian = False):
    '''
    printer ut en formatert liste med t verdier og y verdier basert på formel
    boolian er om man vil ha listen i revers eller ikke
    Outputter en fil med resutat som heter Res_ball.dat
    '''
    new_file = open('Res_ball.dat','w') #lager fil
    g = 9.81
    file_list = read_file(data)
    time = []
    new_file.write('v0= '+ str(file_list[0]) + '\n')
    new_file.write(' {:^20} -->   {:^10}'.format('tid (s)','Høyde (m)') + '\n')
    for num in sorted(file_list[1],reverse = boolian): #sorterer liste
        time.append(num)
    #print('v0 = ' + str(file_list[0]))
    for t in time: #skriver hver linje
        y = (float(file_list[0])*t)-(0.5*g*t**2)
        new_file.write('{:^20}s --> {:^10}m'.format(t,round(y,4)) + '\n')
    new_file.close()
test_ball()
print_file('ball.dat') #aktiverer funksjon

'''
terminal> python ball_file_read_write.py

'''