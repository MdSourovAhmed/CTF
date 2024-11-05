#include <bits/stdc++.h>
using namespace std;
const int m = 41;
int inv(int a)
{
  return a <= 1 ? a : m - (long long)(m / a) * inv(m % a) % m;
}
int main()
{
  string s = "picoCTF{";
  vector<int> v(23);
  for (int &i : v)
  {
    cin >> i;
    i %= 41;
    i = inv(i);
    // cout << i << " ";
    if (i == 37)
      s.push_back('_');
    else if (i > 26)
    {
      i %= 27;
      s.push_back(i + '0');
    }
    else
      s.push_back(i + 'a' - 1);
  }
  s.push_back('}');
  cout << s << endl;
}
