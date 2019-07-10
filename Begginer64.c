#include<stdio.h>
void main()
{
    int apple,ball,cat;
    scanf("%d",&apple);
    scanf("%d",&ball);
    cat=apple+ball;
    if(cat%2==0)
    {
        printf("even");
    }
    else
    {
        printf("odd");
    }
    return 0;
}
