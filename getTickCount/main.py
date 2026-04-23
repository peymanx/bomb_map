import ctypes

def get_tick_count():
    return ctypes.windll.kernel32.GetTickCount()
    
save = get_tick_count()
while True:
    current = get_tick_count()
    if current > save:
        print(f'{save}  =>  {current-save}')
        save = current

