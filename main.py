from managers.LedStripManager import LedStripManager
import time
import os

if __name__ == '__main__':

    steps = 20
    for k in range(0, steps + 1):
        print(f"(k) = {k}")

    ledStripManager = LedStripManager()
    ledStripManager.rainbow()

    time.sleep(10)

    ledStripManager.police()

    time.sleep(10)

    ledStripManager.stop()

    time.sleep(1)

os._exit(0)



# FIXME LED breathe
# FIXME LED alert
# FIXME LED individually

