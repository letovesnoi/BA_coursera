#include<stdio.h>
#include<string.h>

int *pi;
int n, m;
int j;
int M[1001];

void computePrefixF(char *P){
    pi = new int[strlen(P) + 1];
    pi[1] = 0;
    int k = -1;
    for(int q = 2; q <= m; q++){
        while((k > 0)&&(P[k + 1] != P[q - 1])){
            k = pi[k] - 1;         
        }      
        if(P[k + 1] == P[q - 1]){
            k++;       
        }
        pi[q] = k + 1;        
    }                  
}

void KMPMatcher(char *T, char *P){
    n = strlen(T);
    m = strlen(P);
    computePrefixF(P);
    int q = 0;
    for(int i = 0; i < n; i++){
        while((q > 0)&&(P[q] != T[i])){
            q = pi[q];
        }
        if(P[q] == T[i]){
            q = q + 1;       
        }
        if(q == m){
            if(i - m + 1 != j)
                M[i - m + 1] = -1;
            M[j]++;
            q = pi[q];     
        }        
    }    
}

int main(){
    char T[1001], P[100];
    int k;
    int ans[1000];
    j = 0;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    gets(T);
    n = strlen(T);
    scanf("%d", &k);
    for(int i = 0; i < n; i++){
        M[i] = 0;            
    }
    while(j <= n - k){
        for(int i = 0; i < k; i++){
            P[i] = T[i + j];        
        }
        P[k] = '\0';
        if(M[j] != -1){
            KMPMatcher(T, P);
        }
        j++;       
    }
    int max = -1;
    for(int i = 0; i < n; i++){
        if(M[i] > max){
            max = M[i];     
        }            
    }
    for(int i = 0; i < n; i++){
        if(M[i] == max){
            for(int l = 0; l < k; l++){
                printf("%c", T[i + l]);        
            } 
            printf(" ");    
        }            
    }
    return 0;
}
