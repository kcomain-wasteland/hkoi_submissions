#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int x,a,b;
int main(){
    scanf("%d", &x);
    a = (x - 1) / 2;
    b = (x + 1) / 2;
    if (a < b){
        printf("<");
    }
    if (a == b){
        printf("=");
    }
    if (a > b){
        printf(">");
    }
    return 0;
}