from managers.LedStripManager import LedStripManager
import time

if __name__ == '__main__':

    ledStripManager = LedStripManager()
    ledStripManager.rainbow()

    time.sleep(10)

    ledStripManager.police()

    time.sleep(10)

    ledStripManager.stop()


# FIXME LED breathe
# FIXME LED alert
# FIXME LED individually

