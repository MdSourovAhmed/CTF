#include <bits/stdc++.h>
using namespace std;

int main()
{
  FILE *fptr;
  char myString[10000];

  // char freq[26] = {0};

  vector<int> freq(26, 0);

  const char *fl = "hellow1.txt";

  fptr = fopen(fl, "r");

  // If the file exist
  if (fptr != NULL)
  {

    // Read the content and print it
    while (fgets(myString, 10000, fptr))
    {
      // printf("%s", myString);
    }

    // If the file does not exist
  }
  else
  {
    printf("Not able to open the file.");
  }
  printf("%s", myString);
  puts("\n");

  for (int i = 0; myString[i]; ++i)
    if (myString[i] != ' ')
    {
      freq[myString[i] - 'A']++;
    }

  fclose(fptr);

  vector<pair<int, char>> ans;

  for (int i = 0; i < 26; i++)
  {
    ans.push_back({freq[i], i + 'A'});
  }
  sort(ans.rbegin(), ans.rend());

  for (auto p : ans)
    printf("%d--> %c\n", p.first, p.second);
}
