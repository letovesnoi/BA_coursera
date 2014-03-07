#include<stdio.h>
#include<conio.h>

int count = 0, mass[21], array[19];
int M;

void funct(int sum){
    if(sum < 0){
        sum = M;    
        return;     
    } 
    //printf("M=%d\n", M);
    if(sum == 0){
        //printf("M=%d\n", M);
        //getch();
        count++;
        printf("%d\n", count);
        return;     
    }     
    for(int i = 0; i < 18; i++){
        funct(sum - mass[i]);        
    }
   return; 
}

int main(){
    freopen("input.txt", "r", stdin);
    scanf("%d", &M);
    freopen("input3.txt", "r", stdin);
    for(int i = 0; i < 18; i++){
        scanf("%d ", &mass[i]);        
    }
    funct(M); 
    freopen("output.txt", "w", stdin);
    printf("%d", count);   
    getch();
}
