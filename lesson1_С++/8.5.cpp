#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
#include<conio.h>
using namespace std;

int h, k, n, d;
int *T, *P, *rcP, *a;

void from10to4(int del){
    for(int p = 0; p < k; p++){
        P[k - p - 1] = del % 4;
        del = del / 4;            
    }     
}

void reverseComplement(){
     int i = 0;
     while(i != k){
        if(P[i] == 0){
           rcP[k - 1 - i] = 3;            
        } 
        if(P[i] == 1){
           rcP[k - 1 - i] = 2;            
        }  
        if(P[i] == 2){
           rcP[k - 1 - i] = 1;            
        }  
        if(P[i] == 3){
           rcP[k - 1 - i] = 0;            
        }       
        i++;   
    }            
}

void countD(int *count, int flag){
    for(int i = 0; i < h; i++){
        count[i] = 0;     
    }    
    for(int l = 0; l < h; l++){
        from10to4(l);
        if(flag == 1){
            reverseComplement();        
        }                  
        for(int i = 0; i <= n - k; i++){
            a[i] = 0;        
        }
        for(int i = 0; i <= n - k; i++){
            for(int j = 0; j < k; j++){
                if((flag == 0) && (T[i + j] != P[j])){
                    a[i]++;       
                } 
                if((flag == 1) && (T[i + j] != rcP[j])){
                    a[i]++;       
                }        
            }      
        } 
        for(int i = 0; i <= n - k; i++){
            if(a[i] <= d){
                count[l]++;        
            }        
        }
    }
}

int main(){
    freopen("output.txt", "w", stdout);
    ifstream f("input.txt");
    string DNA;
    int *count, *countR;
    f >> DNA;
    f >> k;
    f >> d;
    n = strlen(DNA.c_str());
    T = new int[n];
    P = new int[k];
    rcP = new int[k]; 
    a = new int[n - k + 1];
    for(int i = 0; i < n; i++){
        if(DNA[i] == 'A'){
            T[i] = 0;          
        }  
        if(DNA[i] == 'C'){
            T[i] = 1;          
        }  
        if(DNA[i] == 'G'){
            T[i] = 2;          
        }  
        if(DNA[i] == 'T'){
            T[i] = 3;          
        }          
    }
    h = 1;
    for(int i = 0; i < k; i++){
        h = h * 4;        
    }
    count = new int[h];
    countR = new int[h];
    countD(count, 0);
    countD(countR, 1);
    for(int i = 0; i < h; i++){
        count[i] = count[i] + countR[i];           
    }
    int max = count[0];
    for(int i = 0; i < h; i++){
        if(count[i] > max){
            max = count[i];            
        }            
    }
    char *S = new char[k];
    for(int i = 0; i < h; i++){
        if(count[i] == max){
            from10to4(i);
            for(int i = 0; i < k; i++){
                if(P[i] == 0){
                    S[i] = 'A';          
                }  
                if(P[i] == 1){
                    S[i] = 'C';          
                }  
                if(P[i] == 2){
                    S[i] = 'G';          
                }  
                if(P[i] == 3){
                   S[i] = 'T';          
                }
                printf("%c", S[i]);          
            }
            printf(" ");
                            
        }            
    }
    return 0;
}
