using ATK_DP100DLL;
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("DP100 Control Test C#\r");
        Console.WriteLine("------------------------\n");

        ATKDP100API api = new ATKDP100API();

        Console.WriteLine("Connect State:" + api.ConnState);
        api.DevOpenOrClose();
        Console.WriteLine("Connect State:" + api.ConnState);
        
        string Dev = string.Empty;
        string HWVer = string.Empty;
        string AppVer = string.Empty;
        string DevSN = string.Empty;
        string DevState = string.Empty;

        Console.WriteLine("Get Device Info" + api.GetDevInfo(ref Dev, ref HWVer, ref AppVer, ref DevSN, ref DevState));
        Console.WriteLine(Dev);
        Console.WriteLine(HWVer); 
        Console.WriteLine(AppVer);

        byte index = 0;
        byte state= 0;
        UInt16 vset = 0;
        UInt16 iset = 0;
        UInt16 ovp = 0;
        UInt16 ivp = 0;

        Console.WriteLine(api.GetCurrentBasic(ref index, ref state, ref vset, ref iset, ref ovp, ref ivp));
        Console.WriteLine(index);
        Console.WriteLine(state);
        Console.WriteLine(vset);
        Console.WriteLine(iset);
        Console.WriteLine(ovp);
        Console.WriteLine(ivp);

        return;
    }
}