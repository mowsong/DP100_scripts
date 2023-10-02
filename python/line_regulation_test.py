import sys, time, os
# require pythonnet
import clr
clr.AddReference(r'./ATK-DP100DLL(x64)')
import ATK_DP100DLL
from System import Byte, UInt16, String, Console, IO

# send the Console.Writeline to null
Console.SetOut(IO.TextWriter.Null)

print('DP100 Python Test')
DP100 = ATK_DP100DLL.ATKDP100API()
if DP100.ConnState == False:
  ret = DP100.DevOpenOrClose()
  if ret == False:
    print('Device not fount!')
    sys.exit()

try:
  print('Press CTRL-C to end.')
  while True:
    DP100.OpenOut(0, 1000, 5000)
    time.sleep(0.1)
    DP100.OpenOut(0, 1000, 0)
    time.sleep(0.1)
    
except KeyboardInterrupt:
  pass

DP100.CloseOut(0, 0, 0)
