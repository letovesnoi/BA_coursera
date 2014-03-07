#include<stdio.h>
#include<string.h>
#include <iostream>
#include <fstream>
using namespace std;

int main(){
    int *ans;
    int min;
    freopen("output.txt", "w", stdout);
    ifstream f("input.txt");
    string DNA;
    f >> DNA;
    int n = strlen(DNA.c_str());
    ans = new int[n];
    ans[0] = 0;
    if(DNA[0] == 'C'){
        ans[0] = -1;          
    } 
    if(DNA[0] == 'G'){
        ans[0] = 1;          
    } 
    for(int i = 1; i < n; i++){
        if(DNA[i] == 'C'){
            ans[i] = ans[i - 1] - 1;          
        }
        else{ 
            if(DNA[i] == 'G'){
                ans[i] = ans[i - 1] + 1;          
            }
            else{
                ans[i] = ans[i - 1];      
            }
        }  
                   
    }
    min = ans[0];
    for(int i = 1; i < strlen(DNA.c_str()); i++){
        if(ans[i] < min){
            min = ans[i];          
        }        
    }
    for(int i = 0; i < strlen(DNA.c_str()); i++){
        if(ans[i] == min){
            printf("%d ", i);          
        }        
    }
    return 0;    
}
