#include <stdio.h>
#include <stdlib.h>
char *caesarCipher(char *s, int k)
{
    for (int i = 0; s[i]; ++i)
    {
        if ((s[i] >= 'a' && s[i] <= 'z'))
            s[i] = ((s[i] - 'a' + k) % 26) + 'a';
        else if ((s[i] >= 'A' && s[i] <= 'Z'))
            s[i] = ((s[i] - 'A' + k) % 26) + 'A';
    }
    return s;
}

int main()
{
    int n;scanf("%d",&n);
    char s[n];
    scanf("%s", s);
    printf("The String is: %s", s);
    int k;
    scanf("%d", &k);
    char *cipher = caesarCipher(&s, k);
    printf("\nAfter the shifting of chars by %d, the cipher is now: %s\n", k, cipher);
    return 0;
}
