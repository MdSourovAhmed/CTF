#include<bits/stdc++.h>
using namespace std;

int main()
{
string s="picoCTF{";
vector<int>v(22);
for(int &i:v)
{
cin>>i;
i%=37;
if(i==36)s.push_back('_');
else if(i>25){
i%=26;
s.push_back(i+'0');}
else
s.push_back(i+'A');
}
s.push_back('}');
cout<<s<<endl;
}
