import numpy as np
import time
from picamera import PiCamera


cam = PiCamera()
cam.resolution = (1024, 768)
cam.start_preview()

time.sleep(0.5)
output = np.empty( (768,1024,3),dtype=np.uint8)
cam.capture(output,'rgb')
print(output)
