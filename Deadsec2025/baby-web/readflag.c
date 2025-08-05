#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp = fopen("/flag.txt", "r");
    if (fp == NULL)
    {
        perror("Failed to open flag.txt");
        return 1;
    }

    char flag[256];
    if (fgets(flag, sizeof(flag), fp) == NULL)
    {
        perror("Failed to read flag");
        fclose(fp);
        return 1;
    }

    fclose(fp);

    printf("Flag: %s\n", flag);

    return 0;
}
