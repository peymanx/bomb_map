import ctypes
import time
import win32gui
import win32process
import win32api
import os


START = 0x01005340
END   = 0x010056A0
SIZE  = END - START


PROCESS_VM_READ = 0x0010

# Beginner
ROWS = 9
COLS = 9
STRIDE = 32        # ساختار واقعی حافظه winmine
OFFSET = 0x21      # اصلاح ستون (0x20 + 1 بایت border)

kernel32 = ctypes.windll.kernel32

# پیدا کردن پنجره Minesweeper
hwnd = win32gui.FindWindow(None, "Minesweeper")
if not hwnd:
    print("💣 Minesweeper NOT found")
    exit(1)

# گرفتن PID و باز کردن پروسه
_, pid = win32process.GetWindowThreadProcessId(hwnd)
h_process = win32api.OpenProcess(PROCESS_VM_READ, False, pid)

buffer = ctypes.create_string_buffer(SIZE)
bytes_read = ctypes.c_size_t()

def draw_field(buf):
    print("💣 Minesweeeeeeeper 9x9 \n   Bomb Map, by peymanx\n")
    i = 0

    #print('  1 2 3 4 5 6 7 8 9')
    print('  1  2  3  4  5  6  7  8  9')
    for r in range(ROWS):  
        i=i+1        
        print(i,end=" ")     
        for c in range(COLS):
            idx = OFFSET + r * STRIDE + c
            v = buf[idx]
            if isinstance(v, bytes):
                v = v[0]

            if v == 0x8F:
                print("🚩", end=" ")
            else:
                print(". ", end=" ")
        print()


while True:
    os.system("cls")

    ret = kernel32.ReadProcessMemory(
        int(h_process),
        ctypes.c_void_p(START),
        buffer,
        SIZE,
        ctypes.byref(bytes_read)
    )

    if not ret:
        print("💣 Minesweeper NOT found")
        break

    draw_field(buffer)
    time.sleep(1.5)
