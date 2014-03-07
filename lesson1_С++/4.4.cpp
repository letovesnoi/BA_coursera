#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
#include<math.h>

using namespace std;

int n, m;
int k;

int meet[300000][1009];
int countMeet[5000000];

void RKMatcher(int *T, int q){    
    for(int i = 0; i < n; i++){
        countMeet[i] = 0;    
    }     
    int h = 1;
    for(int i = 0; i < k - 1; i++){
        h = h * 4 ;        
    }
    int t = 0;     
    for(int i = 0; i < k; i++){
        t = (4 * t + T[i]) % q;        
    } 
    meet[t][countMeet[t]] = 0;
    countMeet[t]++;
    for(int s = 1; s <= n - k; s++){
            t = (4 * (t - T[s - 1] * h) + T[s + k - 1]) % q;
            meet[t][countMeet[t]] = s;
            countMeet[t]++;       
    }      
}

int main(){
    string DNA;
    int *T;
    int L, t, countAns = 0; 
    freopen("output.txt", "w", stdout);
    ifstream f("input.txt");
    f >> DNA;
    n = strlen(DNA.c_str());
    
    T = new int[n];
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
    
    f >> k >> L >> t;
    
    int q = 1;
    for(int i = 0; i < k; i++){
        q = q * 4;        
    }
    RKMatcher(T, q);
    
    int tE = t - 1;
    int tB = 0;
    for(int i = 0; i < q; i++){
        if(meet[i][0] != 0){
            while((meet[i][tE] - meet[i][tB] + k - 1 > L) && (tE <= countMeet[i])){
                tE++;
                tB++;        
            }
            if((meet[i][tE] - meet[i][tB] + k - 1 <= L) && (tE <= countMeet[i])){
                countAns++;                         
            }
        }
    }
    printf("%d", countAns);
    return 0;
}
