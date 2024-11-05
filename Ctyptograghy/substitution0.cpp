#include <bits/stdc++.h>
using namespace std;

int main()
{
    string k = "OHNFUMWSVZLXEGCPTAJDYIRKQB";
    string s = "Suauypcg Xuwaogf oacju, rvds o waoiu ogf jdoduxq ova, ogf hacywsd eu dsu huudxumace o wxojj noju vg rsvns vd roj ugnxcjuf. Vd roj o huoydvmyx jnoaohouyj, ogf, oddsod dveu, yglgcrg dc godyaoxvjdj—cm ncyaju o wauod pavbu vg o jnvugdvmvn pcvgdcm ivur. Dsuau ruau drc acygf hxonl jpcdj guoa cgu ukdauevdq cm dsu honl, ogf oxcgw cgu guoa dsu cdsua. Dsu jnoxuj ruau uknuufvgwxq soaf ogf wxcjjq, rvds oxx dsuoppuoaognu cm hyagvjsuf wcxf. Dsu ruvwsd cm dsu vgjund roj iuaq aueoalohxu, ogf,dolvgw oxx dsvgwj vgdc ncgjvfuaodvcg, V ncyxf soafxq hxoeu Zypvdua mca svj cpvgvcgaujpundvgw vd.";
    //     "Suauypcg Xuwaogf oacju, rvds o waoiu ogf jdoduxq ova, ogf hacywsd eu dsu huudxu
    // mace o wxojj noju vg rsvns vd roj ugnxcjuf. Vd roj o huoydvmyx jnoaohouyj, ogf, od
    // dsod dveu, yglgcrg dc godyaoxvjdj—cm ncyaju o wauod pavbu vg o jnvugdvmvn pcvgd
    // cm ivur. Dsuau ruau drc acygf hxonl jpcdj guoa cgu ukdauevdq cm dsu honl, ogf o
    // xcgw cgu guoa dsu cdsua. Dsu jnoxuj ruau uknuufvgwxq soaf ogf wxcjjq, rvds oxx dsu
    // oppuoaognu cm hyagvjsuf wcxf. Dsu ruvwsd cm dsu vgjund roj iuaq aueoalohxu, ogf,
    // dolvgw oxx dsvgwj vgdc ncgjvfuaodvcg, V ncyxf soafxq hxoeu Zypvdua mca svj cpvgvcg
    // aujpundvgw vd.";
    map<int, int> m;
    for (int i = 0; k[i]; ++i)
        m[k[i]-'A'] = i;

    // for (auto a : m)
    //     cout << a.first << "<--->" << a.second << endl;

    string fl = "Dsu mxow vj: pvncNDM{5YH5717Y710G_3I0XY710G_03055505}";
    for (char &c : fl)
    {
        if (c >= 'a' && c <= 'z')
            c = m[c-'a'] + 'a';
        
        if (c >= 'A' && c <= 'Z')
            c = m[c-'A'] + 'A';
    }
    cout << fl;
}