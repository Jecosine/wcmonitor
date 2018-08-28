from PIL import Image
import numpy as np
import sys
im = Image.open("QR.png",'r').convert('L')
imdata = np.array(im)

for i in range(45,405,10):
    for j in range(45,405,10):
        if imdata[i][j] == 0:
            sys.stdout.write('  ')
        else:
            sys.stdout.write('\x1b[7m  \x1b[0m')
        sys.stdout.write('\n')

