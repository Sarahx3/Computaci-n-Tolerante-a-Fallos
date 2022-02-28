import psutil, os

while True:
    procesos = 0
    for proc in psutil.process_iter():
        if proc.name().lower() == 'python.exe':
            procesos += 1
        
    if procesos == 1:
        os.system('python main.py')

    else:
        print('Ya se esta ejecutando')