#include <stdio.h>

int main() 
 {
    int appple;
    int mango;
    int orange;
    int fruit;
    scanf("%d",&appple);
    scanf("%d",&mango);
    scanf("%d",&orange);
    fruit=appple*mango%orange;
    printf("%d",fruit);
  return 0;
}
