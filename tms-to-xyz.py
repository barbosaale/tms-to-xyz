# -*- coding: utf-8 -*-
# -+-+-+-+-+-+-+-+-+-+-+-+
''' ---------------------------------------
https://github.com/barbosaale/tms-to-xyz
barbosa.ale@gmail.com
--------------------------------------- '''
import sys
import os
import glob


def Main():
    if len(sys.argv) < 2:
        print 'Enter the path of the folder containing the tiles after the script name. Example: ( $ python tms-to-xyz.py C:\tiles )'
    else:
        pasta = sys.argv[1] + '\\'
        ConvertTms(pasta)


def ConvertTms(pasta):
    contentz = os.listdir(pasta)
    print contentz
    for z in contentz:
    
        if os.path.isdir(pasta + z):
            print 'Z: ' + z
            nz = float(z)
            os.chdir(pasta + z)
            contentx = os.listdir(pasta + z)
            
            for x in contentx:
                
                if os.path.isdir(pasta + z + "\\" + x):
                    print 'X: ' + x
                    os.chdir(pasta + z + "\\" + x)
                    
                    for png in sorted(glob.glob('*.png')):
                        ny = float(png.split('.')[0])
                        
                        ny_new = int( (2 ** nz) - ny - 1 )
                        
                        os.rename(png, str(ny_new) + ".png" )
                        
                        print 'Y: ' + png.split('.')[0] + ' | ' + str(ny_new)
                    
                    
                print '\n'
                
        print '\n'    
        
    print('Tiles successfully converted ...!')
    
    
    
if __name__ == "__main__":
    Main()