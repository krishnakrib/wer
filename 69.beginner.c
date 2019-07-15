#include <stdio.h>

int main() 
 {
    int appple;
    int mango;
    int fruit;
    scanf("%d",&appple);
    scanf("%d",&mango);
    fruit=appple-mango;
    if(fruit%2==0)
    {
        printf("even",fruit);
    }
    else
    {
        printf("odd",fruit);
    }
  return 0;
}
