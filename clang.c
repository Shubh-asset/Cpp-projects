#include<stdio.h>
#include<string.h>

int main(int argc, char const *argv[])
{
    char str[10];

    //scanf("%[^\n]s", str);
    fgets(str, 10, stdin);
    printf("%s", str);

    return 0;
}
