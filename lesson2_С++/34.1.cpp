#include<stdio.h>
#include<math.h>

int main(){
    FILE *f;    
    f = freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int L = 0;
    int m[10000];
    while(!feof(f)){
        scanf("%d ", &m[L]); 
        L++;              
    }
    double N = sqrt(L);
    int inc, dec;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            for(int l = 0; l < N; l++){
                inc = inc + m[N * i + l] + m[N * j + l]; 
                dec = dec + m[N * i + l] - m[N * j + l];      
            }        
        }        
    }
    return 0;    
}
