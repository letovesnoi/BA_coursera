#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
using namespace std;

int *pi;
int *index;
long int n, m, countI = 0;
//int j;
int *M;
int k, cMN;
long int **meet;
long int *countMeet;

/*void computePrefixF(char *P){
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
}*/

void RKMatcher(int *T){
    cMN = 1;
    for(int i = 0; i < k - 1; i++){
        cMN = cMN * 4;        
    }
    meet = new long int*[cMN];
    for (int i = 0; i < n; ++i){
        meet[i] = new long int[n];
    }
    countMeet = new long int[n];
    for(int i = 0; i < n; i++){
        countMeet[i] = 0;        
    }
        
    long int h = 1;
    for(int i = 0; i < m - 1; i++){
        h = h * 4;        
    }
    
    long int t = 0;     
    for(int i = 0; i < m; i++){
        t = 4 * t + T[i];        
    } 
    for(long int s = 0; s < n - m; s++){
        meet[t][countMeet[t]] = s;
        countMeet[t]++;
        t = 4 * (t - T[s + 1] * h) + T[s + m + 1];        
    }        
}


/*void KMPMatcher(const char *T, char *P){
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
            if(i - m + 1 != j){
                M[i - m + 1] = -1;
                index[countI] = i - m + 1;
                countI++;
            }
            M[j]++;
            q = pi[q];     
        }        
    }    
}*/

int main(){
    //char *P;
    string DNA;
    int *T;
    int L, t;
    //j = 0;  
    freopen("output.txt", "w", stdout);
    ifstream a("input.txt");
    ofstream c("output.txt");
    a >> DNA;
    n = strlen(DNA.c_str());
    
    T = new int[n];
    for(int i = 0; i < n; i++){
        if(DNA[i] == 'A'){
            T[i] = 0;          
        }  
        if(DNA[i] == 'C'){
            T[i] = 1;          
        }  
        if(DNA[i] == 'T'){
            T[i] = 2;          
        }  
        if(DNA[i] == 'G'){
            T[i] = 3;          
        }          
    }
    
    //M = new int[n + 1];
    a >> k >> L >> t;
    RKMatcher(T);
    int tE = t;
    int tB = 1;
    for(int i = 0; i < cMN; i++){
        while((meet[i][tE] - meet[i][tB] + k - 1 > L) && (tE < countMeet[i])){
            tE++;
            tB++;        
        }
        if((meet[i][tE] - meet[i][tB] + k - 1 <= L) && (tE < countMeet[i])){
                printf("%d ", meet[i][0]);                         
        }
    }
    //P = new char[k + 1];  
    
    /*index = new int[n + 1];
    for(int i = 0; i < n; i++){
        M[i] = 0;            
    }
    while(j <= n - k){
        countI = 0;
        for(int i = 0; i < k; i++){
            P[i] = DNA[i + j];        
        }
        P[k] = '\0';
        if(M[j] != -1){
            index[countI] = j;
            countI++;
            KMPMatcher(DNA.c_str(), P);

            int tE = t - 1;
            int tB = 0;
            while((index[tE] - index[tB] + k - 1 > L) && (tE < countI)){
                tE++;
                tB++;        
            }
            if((index[tE] - index[tB] + k - 1 <= L) && (tE < countI)){
                for(int l = 0; l < m; l++){
                    printf("%c", P[l]);        
                } 
                printf(" ");                 
            }
        }
        j++;       
    }*/
    return 0;
}
