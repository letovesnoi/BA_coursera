#include<stdio.h>
#include<string.h>

char key[1000001][100];
int next[10000001], prev[10000001];
int head, countS = 0, strl = 0;
char amAcids[21];
int mass[21];;

int *spectrum, inputSpectrum[10001];
char *peptide;
int countM, countMInput;

void insert(int i){
    next[i] = head;
    if((head != '\0')||(countS == 1)){
        prev[head] = i;
    }
    head = i;    
    prev[i] = '\0';
}

void del(int i){
    if(prev[i] != '\0'){
        next[prev[i]] = next[i];           
    }
    else{
        head = next[i];     
    }
    if(next[i] != '\0'){
        prev[next[i]] = prev[i];               
    }    
}

void init(){
    key[0][0] = '\0';
    countS++;
    head = 0;
    next[head] = 0;
    prev[head] = 0; 
    for(int i = 0; i < 10000001; i++){
        next[i] = 0;
        prev[i] = 0;        
    }    
}

void expand(){
    int i = head;
    while((next[i] != 0)||(countS == 1)){
        for(int j = 0; j < 18; j++){
            for(int l = 0; l < strl; l++){
                key[countS][l] = key[i][l];
            }
            key[countS][strl] = amAcids[j];
            
            insert(countS);
            countS++;          
        }
     del(i);
     i = prev[i];
     }
     strl++;
     /*for(int j = 0; j < countS; j++){
         for(int i = 0; i < strl; i++){
             printf("%c", key[j][i]);        
         }
         printf("\n");
     }*/           
}

void qsort(int low, int high){
    int i = low, j = high;
    int middle, temp;
    middle = spectrum[(i + j) / 2];
    while(i <= j){
        while(spectrum[i] < middle){
            i++;                       
        } 
        while(spectrum[j] > middle){
            j--;                       
        } 
        if(i <= j){
            temp = spectrum[i];
            spectrum[i] = spectrum[j];
            spectrum[j] = temp;
            i++;
            j--;
        }
    }
  if(low < j){
      qsort(low, j);
  }
  if(i < high){
      qsort(i, high);
  }
}

void getSpectrumLPeptide(char *peptide){
    char T[10001], P[10001];
    int l = strlen(peptide);
    int N = l * (l + 1) / 2 + 2;
    spectrum = new int[N + 1];
    
    countM = 1;
    for(int i = 0; i < N; i++){
        spectrum[i] = 0;
    }
    spectrum[N] = '\0';
    int k, j;
    for(int count = 1; count < l; count++){
        for(int i = 0; i < l; i++){
            T[i] = peptide[i];        
        }
        for(int pos = 0; pos <= l - count; pos++){
            for(int i = 0; i < count; i++){
                P[i] = peptide[pos + i];
            }
            for(int i = 0; i < count; i++){
                j = 0;
                while(amAcids[j] != P[i]){
                    j++;    
                }
                spectrum[countM] = spectrum[countM] + mass[j];
            }
            countM++;
        }      
    }
    for(int i = 0; i < l; i++){
        j = 0;
        while(amAcids[j] != peptide[i]){
            j++;    
        }
        spectrum[countM] = spectrum[countM] + mass[j];
    }
    countM++;
    qsort(0, countM - 1);
    for(int i = 0; i < countM; i++){
        printf("%d ", spectrum[i]);        
    }
}

int compareSpectrum(int i){
    peptide = new char[strl + 1];
    for(int j = 0; j < strl; j++){
        peptide[j] = key[i][j];        
    }
    peptide[strl] = '\0';
    getSpectrumLPeptide(peptide);
    if(countM == countMInput){
        for(int j = 0; j < countM; j++){
            if(inputSpectrum[j] != spectrum[j]){
                return 0;                 
            }        
        }
        return 1;          
    } 
    return 0;    
}

int consistent(int i){
    int l = 0;
    peptide = new char[strl + 1];
    for(int j = 0; j < strl; j++){
        peptide[j] = key[i][j];        
    }
    peptide[strl] = '\0';
    getSpectrumLPeptide(peptide);
    for(int j = 0; j < countM; j++){
        while((inputSpectrum[l] != spectrum[j])&&(l < countMInput)){
            l++;                     
        }   
        if(l > countMInput){
            return 0;     
        }              
    } 
    return 1;   
}

int main(){
    FILE *f;
    freopen("input2.txt", "r", stdin);
    for(int i = 0; i < 18; i++){
        scanf("%c ", &amAcids[i]);
        scanf("%d\n", &mass[i]);
    }
    f = freopen("input0.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int i = 0;
    countMInput = 0;
    while(!feof(f)){
        scanf("%d ", &inputSpectrum[countMInput]); 
        countMInput++;               
    }     
    inputSpectrum[countMInput] = '\0';
    init();
    expand();
    while(head != 0){
        int i = head;
        while(next[i] != '\0'){
            if(compareSpectrum(i) == 1){
                puts(peptide);
                del(i);                     
            }
            else{
                if(consistent(i) == 0){
                    del(i);                       
                }     
            }
            i = next[i];              
        } 
        expand();      
    }  
    return 0;    
}
