#include<stdio.h>
#include<conio.h>

int count = 0, mass[21];
int M;
int *p;

void generate(int length){
    int flag = 0;
    int i = length - 1;
    while(flag != 1){
        if(p[i] + 1 < 18){
            p[i]++;
            flag = 1;
        }
        else{
            p[i] = 0;
            i--;         
        }
    }
    /*for(int i = 0; i < length; i++){
        printf("%d ", p[i]);        
    }   
    printf("\n");*/ 
}

int main(){
    freopen("input.txt", "r", stdin);
    scanf("%d", &M);
    freopen("input3.txt", "r", stdin);
    for(int i = 0; i < 18; i++){
        scanf("%d ", &mass[i]);        
    }
    int nG = 1, sum, j;
    p = new int[1000001];
    for(int i = 0; i < M / 186; i++){
            nG = nG * 18;            
    }
    for(int length = M / 186 + 1; length <= M / 57; length++){
        nG = nG * 18;
        for(int i = 0; i < length; i++){
            p[i] = 0;        
        }
        p[length] = '\0';
        
        for(int i = 0; i < nG; i++){
            sum = M;
            j = 0;
            while((sum > 0)&&(j < length)){
                sum = sum - mass[p[j]];
                j++;          
            }
            if((j == length)&&(sum == 0)){
                count++; 
                printf("%d\n",count);
                /*for(int i = 0; i < length; i++){
                    printf("%d ", p[i]);        
                }   
                printf("\n");*/    
            }
            generate(length);
        }        
    }
    freopen("output.txt", "w", stdin);
    printf("%d", count);   
    getch();
    return 0;
}
