import sys, time, os
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

ret = DP100.GetDevInfo(String.Empty, String.Empty, String.Empty, String.Empty, String.Empty)
print(ret)

step = 0.1
npts = 33
vouts = [int(step*1000*i) for i in range(npts+1)]

for vo in vouts:
  print(f'Set voltage to {vo}')
  DP100.OpenOut(0, 1000, vo)
  time.sleep(0.05)
  ret = DP100.GetCurrentBasic(Byte(0), Byte(0), UInt16(0), UInt16(0), UInt16(0), UInt16(0))
  print(ret)

input('Press any key to end...')
DP100.CloseOut(0, 0, 0)
