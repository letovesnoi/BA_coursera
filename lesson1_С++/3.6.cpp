#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
using namespace std;

int *pi;
int n, m;
int j;
int M[1001];

void computePrefixF(const char *P){
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

void KMPMatcher(const char *T, const char *P){
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
            printf("%d ", i - m + 1);
            q = pi[q];     
        }        
    }    
}

int main(){
//    char *T = new char, *P = new char;
//    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ifstream a("input.txt");
    ofstream c("output.txt");
    string T, P;
    a >> P;
    a >> T;
    KMPMatcher(T.c_str(), P.c_str());   
//   gets(P);
//   gets(T);
//   KMPMatcher(T, P);
    return 0;
}
