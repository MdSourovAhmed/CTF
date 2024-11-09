#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s = "L|k¤y+*^*zo¤*¤kvsno|*k¤om*vo*zk}}*cyvksr";
    for (int i = 0; i < 256; ++i)
    {
        cout << i << ")) ";
        for (char c : s)
        // cout << long(c) << " ";
        // cout << hex << int(c) << " ";
        {
            int r = (int(c) + i) % 256;
            if (r < 128)
                cout << char(r);
        }
        cout << endl;
    }

    // cout<<int('Ü');
    // Brao! T pe alider aec le pass Yolaih
    // Brao! T pe alider aec le pass Yolaih
    // for(int i=0;i<256;++i)cout<<char(i)<<"-->"<<i<<endl;
}
