#include<stdio.h>
void main()
{
    int mango,prod=1,rem;
    scanf("%d",&mango);
    while(mango!=0)
    {
        rem = mango% 10; 
        prod *= rem; 
        mango /=  10;
    }
    printf("%d",prod);
    return 0;
}
