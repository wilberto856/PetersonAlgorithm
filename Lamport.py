import threading
import time


nprocesos = int(input('Ingrese Cantidad de procesos -> '))
procesos = [0]*nprocesos
procesosConTuno = []


def asignarTurno(idProceso):
    for i in range(nprocesos):
        procesos[i] = max(procesos) + 1
        procesosConTuno.append([procesos[i], idProceso])


def proceso(idProceso):
    asignarTurno(idProceso)
    print('Asignando turno ...')


for j in range(nprocesos):
    thread = threading.Thread(target=proceso, args=(j,))
    thread.start()
    thread.join()
    print('Proceso no. ' + str(j) + ' Obtuvo turno ' + str(procesosConTuno[j][0]) + '\n')
