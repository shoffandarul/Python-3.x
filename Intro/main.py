import time
start_time = time.time()

print("Hello")
print("World")
print("Hello World")

a = 10
print(a)

# ini adalah komentar
"""
    kita bisa meng-compile
    python ke bentuk bytecode

    caranya: ketik python -m py_compile main.py
"""

for i in range(1,1000):
    a = 10

print(time.time() - start_time, "detik")