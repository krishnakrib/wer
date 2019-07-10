#include<stdio.h>
#include<conio.h>

int main()
{
    char a[100];
    char b[100];
    int i,k,l;
    printf("enter the string1:");
    scanf("%s",&a);
    printf("enter the :");
    scanf("%s",&b);
    for(i=0;a[i]!='\0';i++)
    {
        k=i+1;
    }
    for(i=0;b[i]!='\0';i++){
        l=i+1;
    }
    if((k>l)&&(k<l))
    {
        printf("k is larger");
    }
    else if(k==l)
    {
        printf("k and l are equal");
    }
    return 0;
}
