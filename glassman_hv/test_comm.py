import time

from HVController import HvController

hv_controller = HvController()

hv_controller.openPortHV('COM1')
hv_controller._configureHV(timeoutMode='disable')

res = hv_controller.queryHV(verbosity=True)

print(res)

res = hv_controller.setHV(voltToSet=5, curToSet=0.01,verbosity=True)

print(res)

time.sleep(30)

res = hv_controller.setHV(voltToSet=0, curToSet=0.00,verbosity=True)
hv_controller._configureHV(timeoutMode='enable')


hv_controller.closePortHV()
