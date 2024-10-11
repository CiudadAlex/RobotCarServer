from managers.LedStripManager import LedStripManager
import time

if __name__ == '__main__':

    ledStripManager = LedStripManager()
    ledStripManager.police()

    time.sleep(10)

    ledStripManager.rainbow()

    time.sleep(10)

    ledStripManager.stop()

