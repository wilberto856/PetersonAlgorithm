import threading
import time


flag = [False, False]
turno = 1


def proceso (nProceso):
    global flag, turno
    flag[0] = True
    while flag[1]:
        if turno == 1:
            flag[0]=False
            while turno ==1:
                print('Proceso '+nProceso+'Esperando...')
                time.sleep(3)
                flag[0]=True
    print('Proceso: '+nProceso + ' Trabajando ...')
    time.sleep(2)
    print('termine de trabajar proceso'+nProceso+'\n')
    time.sleep(0.5)
    turno = 1
    flag[0]=False


for i in range(5):
    thread1 = threading.Thread(target=proceso, args=('1',))
    thread2 = threading.Thread(target=proceso, args=('2',))
    thread3 = threading.Thread(target=proceso, args=('3',))

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

    thread3.start()
    thread3.join()




