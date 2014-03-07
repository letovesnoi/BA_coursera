#include<stdio.h>
#include<conio.h>

void qsort(int low, int high, int *sp){
    int i = low, j = high;
    int middle, temp;
    middle = sp[(i + j) / 2];
    while(i <= j){
        while(sp[i] < middle){
            i++;                       
        } 
        while(sp[j] > middle){
            j--;                       
        } 
        if(i <= j){
            temp = sp[i];
            sp[i] = sp[j];
            sp[j] = temp;
            i++;
            j--;
        }
    }
  if(low < j){
      qsort(low, j, sp);
  }
  if(i < high){
      qsort(i, high, sp);
  }
}

int main(){
    int inputSpectrum[100001];
    int countInput = 0, current = 0, currentSort = 0;
    FILE *f;
    f = freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    while(!feof(f)){
        scanf("%d ", &inputSpectrum[countInput]); 
        countInput++;               
    } 
    int N = countInput * (countInput - 1) / 2;
    int *m = new int[N];
    qsort(0, countInput - 1, inputSpectrum);
    for(int i = 1; i < countInput; i++){
        for(int j = i - 1; j >= 0; j--){
            if(inputSpectrum[i] != inputSpectrum[j]){
                m[current] = inputSpectrum[i] - inputSpectrum[j];
                current++;  
            }
        }        
    }
    int max = m[0];
    for(int i = 1; i < current; i++){
        if(m[i] > max){
            max = m[i];        
        } 
    }
    int *count = new int[max + 1];
    int *ans = new int[max + 1];
    for(int i = 0; i <= max; i++){
        count[i] = 0;        
    }
    for(int i = 0; i < current; i++){
        count[m[i]]++;        
    }
    int currentMax, temp = 0;
    for(int i = 0; i <= max; i++){
        currentMax = count[0];
        ans[temp] = 0;
        for(int j = 0; j <= max; j++){
            if((count[j] >= currentMax)&&(count[j] != 0)){
                currentMax = count[j];
                ans[temp] = j;            
            }        
        }
        if(count[ans[temp]] != 0){
            count[ans[temp]] = 0;
            temp++;
        }        
    }
    for(int i = 0; i < temp; i++){
        printf("%d ", ans[i]);               
    }
return 0;    
}
