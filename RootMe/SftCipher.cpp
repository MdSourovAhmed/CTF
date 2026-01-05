#include <bits/stdc++.h>
using namespace std;

int main()
{
    FILE *fptr;
    char myString[100];

    const char *fl = "ch7.bin";

    fptr = fopen(fl, "r");

    // If the file exist
    if (fptr != NULL)
    {

        // Read the content and print it
        while (fgets(myString, 100, fptr))
        {
            // printf("%s", myString);
        }
    }

    fclose(fptr);

    for (int i = 0; i < 256; ++i)
    {
        for (char c : myString)
            cout << (char)((int(c) + i) % 256);
        cout << endl;
    }

    // cout<<myString<<endl;
    cout << sizeof(myString) / sizeof(myString[0]);
}
