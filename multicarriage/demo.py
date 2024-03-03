from multicarriage import MultiCarriage as mc
import random
import shutil
import time

def showcase():
    distance = int(shutil.get_terminal_size().columns * 0.5)
    r1 = "random numbers: "
    r2, r3 = str(r1), str(r1)
    mc.create_newline(3)
    for i in range(distance):
        mc.write(r1, 3, clearline=True, flushtxt=True)
        mc.write(r2, 2, clearline=True, flushtxt=True)
        mc.write(r3, 1, clearline=True, flushtxt=True)
        r1 += str(random.randint(0,9))
        r2 += str(random.randint(0,9))
        r3 += str(random.randint(0,9))
        time.sleep(0.075)

if __name__ == "__main__":
    showcase()
