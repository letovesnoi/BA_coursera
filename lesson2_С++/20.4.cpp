#include<stdio.h>
#include<string.h>
#include<conio.h>

int *pi;
int n, m;
int pos;
int M[10001];
int *cyclospectrum;

void qsort(int low, int high){
    int i = low, j = high;
    int m, temp;
    m = cyclospectrum[(i + j) / 2];
    while(i <= j){
        while(cyclospectrum[i] < m){
            i++;                       
        } 
        while(cyclospectrum[j] > m){
            j--;                       
        } 
        if(i <= j){
            temp = cyclospectrum[i];
            cyclospectrum[i] = cyclospectrum[j];
            cyclospectrum[j] = temp;
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
    n = strlen(T);
    m = strlen(P);
    for(int i = 0; i <= n - m; i++){
        M[i] = 0;            
    }
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
            if(i - m + 1 != pos)
                M[i - m + 1] = -1;
            q = pi[q];     
        }        
    }    
}

int main(){
    char peptide[10001], amAcids[21];
    char T[10001], P[10001];
    int mass[21];
    freopen("input.txt", "r", stdin);
    gets(peptide);
    int l = strlen(peptide);
    for(int i = 0; i < l; i++){
        peptide[l + i] = peptide[i];        
    }
    int N = strlen(peptide) * (strlen(peptide) - 1) + 2;
    cyclospectrum = new int[N + 1];
    freopen("input2.txt", "r", stdin);
    for(int i = 0; i < 20; i++){
        scanf("%c ", &amAcids[i]);
        scanf("%d\n", &mass[i]);
    }
    freopen("output.txt", "w", stdout);
    int countM = 1;
    for(int i = 0; i < N; i++){
        cyclospectrum[i] = 0;
    }
    int k, j;
    for(int count = 1; count < l; count++){
        for(int i = 0; i < l + count - 1; i++){
            T[i] = peptide[i];        
        }
        for(pos = 0; pos < l; pos++){
            for(int i = 0; i < count; i++){
                P[i] = peptide[pos + i];
            }
            /*if(M[pos] != -1){
                KMPMatcher(T, P);
            }*/
            for(int i = 0; i < count; i++){
                j = 0;
                while(amAcids[j] != P[i]){
                    j++;    
                }
                cyclospectrum[countM] = cyclospectrum[countM] + mass[j];
            }
            //if(M[pos] != -1){
                countM++;
            //}
        }
        /*for(int i = 0; i < l; i++){
            M[i] = 0;            
        }*/        
    }
    for(int i = 0; i < l; i++){
        j = 0;
        while(amAcids[j] != peptide[i]){
            j++;    
        }
        cyclospectrum[countM] = cyclospectrum[countM] + mass[j];
    }
    countM++;
    qsort(0, countM - 1);
    for(int i = 0; i < countM; i++){
        printf("%d ", cyclospectrum[i]);        
    }
return 0;
}
