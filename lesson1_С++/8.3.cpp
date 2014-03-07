#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
#include<conio.h>
using namespace std;

int main(){
    int d;
    freopen("output.txt", "w", stdout);
    ifstream f("input.txt");
    string T, P;
    f >> P;
    f >> T;
    f >> d;
    int n = strlen(T.c_str());
    int m = strlen(P.c_str());
    int *a;
    a = new int[n - m + 1];
    for(int i = 0; i <= n - m; i++){
        a[i] = 0;        
    }
    for(int i = 0; i <= n - m; i++){
            for(int j = 0; j < m; j++){
                if(T[i + j] != P[j]){
                    a[i]++;       
                }        
            }
            
    } 
    for(int i = 0; i <= n - m; i++){
        if(a[i] <= d){
            printf("%d ", i);        
        }        
    } 
    return 0;
}
