#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
#include<conio.h>
using namespace std;

int h, k;
int *P;

void from10to4(int del){
    for(int p = 0; p < k; p++){
        P[k - p - 1] = del % 4;
        del = del / 4;            
    }     
}

int main(){
    int d;
    int *count;
    freopen("output.txt", "w", stdout);
    ifstream f("input.txt");
    string DNA;
    int *T;
    f >> DNA;
    f >> k;
    f >> d;
    int n = strlen(DNA.c_str());
    T = new int[n];
    P = new int[k];
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
    for(int i = 0; i < h; i++){
        count[i] = 0;        
    } 
    int del;   
    for(int l = 0; l < h; l++){
        from10to4(l);                  
        int *a;
        a = new int[n - k + 1];
        for(int i = 0; i <= n - k; i++){
            a[i] = 0;        
        }
        for(int i = 0; i <= n - k; i++){
            for(int j = 0; j < k; j++){
                if(T[i + j] != P[j]){
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
