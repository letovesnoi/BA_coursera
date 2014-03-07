#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
#include<conio.h>

using namespace std;

int *minI;
int j;
int *pi;
int m;
long int n;
int M[501];
int countMin = 0;
char *DNA = new char[6000000];
char *P = new char[10];
char *T = new char[501];
int L = 500, k = 9;


int findLocOric(){
    int *skew;
    int min;
    skew = new int[n];
    skew[0] = 0;
    if(DNA[0] == 'C'){
        skew[0] = -1;          
    } 
    if(DNA[0] == 'G'){
        skew[0] = 1;          
    } 
    for(int i = 1; i < n; i++){
        if(DNA[i] == 'C'){
            skew[i] = skew[i - 1] - 1;          
        }
        else{ 
            if(DNA[i] == 'G'){
                skew[i] = skew[i - 1] + 1;          
            }
            else{
                skew[i] = skew[i - 1];      
            }
        }  
                   
    }
    min = skew[0];
    for(int i = 1; i < n; i++){
        if(skew[i] < min){
            min = skew[i];          
        }        
    }
    countMin = 0;
    minI = new int[n];
    for(int i = 0; i < n; i++){
        if(skew[i] == min){
            minI[countMin] = i;
            countMin++;          
        }        
    }
}

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
    m = strlen(P);
    computePrefixF(P);
    int q = 0;
    for(int i = 0; i < L; i++){
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

void findDNABox(char *T){
    for(int i = 0; i <= L - k; i++){
        M[i] = 0;            
    }
    while(j <= L - k){
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
    for(int i = 0; i < L - k; i++){
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
}

int main(){
    FILE *f;
    f = freopen("input.txt", "r", stdin);;
    char *sDNA = new char;
    DNA[0] = '\0';
    while(!feof(f)){
        scanf("%s\n", sDNA);
        for(int i = 0; i < strlen(sDNA); i++){
            DNA[strlen(DNA) + i] = sDNA[i];         
        }                   
    }
    freopen("output.txt", "w", stdout);
    n = strlen(DNA);
    findLocOric();
    for(int i = 0; i < countMin; i++){
        if(minI[i] + L - 1 < strlen(DNA)){
            for(int l = 0; l < L; l++){
                T[l] = DNA[minI[i] + l];    
            } 
            printf("%d: ", minI[i]);
            findDNABox(T);
            printf("\n");
        }       
    }
    return 0;    
}
