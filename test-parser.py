import subprocess
import sys
import datetime

dt = datetime.datetime.now()
dt_string = dt.strftime("%d-%m-%Y-%H:%M")
sys.stdout = open(f"{dt_string}", "w")


ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]
processes = ps.decode().split("\n")
nfields = len(processes[0].split()) - 1
processes_running = []
CPU, MEM, NAME_CPU_MAX, NAME_MEM_MAX, users = 0, 0, None, None, []
for row in processes[1:]:
    process = row.split(None, nfields)
    try:
        if process[0] not in users:
            users.append(process[0])
    except IndexError:
        break
    processes_running.append(process[1])
    CPU_MAX = 0
    MEM_MAX = 0
    CPU = CPU + float(process[2])
    MEM = MEM + float(process[3])
    if float(process[2]) > CPU_MAX:
        CPU_MAX = process[2]
        NAME_CPU_MAX = process[10]
    if float(process[2]) > MEM_MAX:
        MEM_MAX = process[2]
        NAME_MEM_MAX = process[10]
    name_process_max_mem = "pass"

print("Отчёт о состоянии системы:")
print(f"Пользователи системы: '{', '.join(users)}'")
print(f"Процессов запущено: {len(processes_running)}")
print("Пользовательских процессов:")
for i in range(len(users)):
    proc1 = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', f'{users[i]}'], stdin=proc1.stdout,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc3 = subprocess.Popen(['wc', '-l'], stdin=proc2.stdout,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(users[i], ":", (proc3.communicate()[0].decode().split("\n")[0]))
print(f"Всего памяти используется: {round(CPU, 1)}%")
print(f"Всего CPU используется: {round(MEM, 1)}%")
print(f"Больше всего памяти использует: {str(NAME_CPU_MAX)[:21]}")
print(f"Больше всего CPU использует: {str(NAME_MEM_MAX)[:21]}")

sys.stdout.close()
