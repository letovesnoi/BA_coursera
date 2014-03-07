#include<stdio.h>
#include<string.h>
#include<conio.h>

int *p, *count; 
char peptide[1001];
int countS = 0;
int arr[10001];

void generate(){
    int N = strlen(peptide);
    int flag = 0;
    int i = N - 1;
    while(flag != 1){
        if(p[i] + 1 < count[i]){
            p[i]++;
            flag = 1;
        }
        else{
            p[i] = 0;
            i--;         
        }
    }    
}

void DNAintoRNA(char *sDNA, char *sRNA){
    for(int i = 0; i < strlen(sDNA); i++){
        if(sDNA[i] == 'T'){
            sRNA[i] = 'U';           
        }
        else{
            sRNA[i] = sDNA[i];     
        }        
    }
    sRNA[strlen(sDNA)] = '\0';    
}

void RNAintoDNA(char *sDNA, char *sRNA){
    for(int i = 0; i < strlen(sRNA); i++){
        if(sRNA[i] == 'U'){
            sDNA[i] = 'T';           
        }
        else{
            sDNA[i] = sRNA[i];     
        }        
    }
    sDNA[strlen(sRNA)] = '\0';    
}

void complement(char *s, char *sc){
    int i = 0;
    int n = strlen(s);
    while(i < n){
        if(s[i] == 'A'){
           sc[n - 1 - i] = 'U';            
        } 
        if(s[i] == 'U'){
           sc[n - 1 - i] = 'A';            
        }  
        if(s[i] == 'C'){
           sc[n - 1 - i] = 'G';            
        }  
        if(s[i] == 'G'){
           sc[n - 1 - i] = 'C';            
        }       
        i++;   
    }
    sc[i] = '\0';    
}

int *pi;
int M[1001];
int n, m;

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

int KMPMatcher(char *T, char *P){
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
                q = pi[q];
                arr[countS] = i - m + 1;
                countS++; 
                return 0;    
           }        
        }
    return 0;    
}

void funct(int i, int j, char *s1){
    if(arr[j] != -1){
        int d = 0;
        while(s1[arr[i] + d] == s1[arr[j] + d]){
            d++;
            if(d == strlen(peptide) * 3){
                arr[j] = -1;
                break;     
            }              
        }             
    }     
}

void printSubStr(char *sDNA){
    for(int i = 0; i < countS; i++){
            //printf("arr[i]=%d ", arr[i]);
            for(int j = 0; j < 3 * strlen(peptide); j++){
                if(arr[i] != -1){
                    printf("%c", sDNA[arr[i] + j]); 
                     
                }           
            } 
            if(arr[i] != -1){
                printf("\n"); 
            }         
        }             
}

int main(){
    char sDNA[10001], ALPHacids[64][4], ALPHcodons[64][3];
    char a[500][100];
    freopen("input.txt", "r", stdin);
    gets(sDNA);
    char *sRNA = new char[strlen(sDNA)];
    //char *scRNA = new char[strlen(sDNA)];
    DNAintoRNA(sDNA, sRNA);
    //complement(sRNA, scRNA);
    gets(peptide);
    int n = strlen(peptide);
    count = new int[n];
    for(int i = 0; i < n; i++){
        count[i] = 0;        
    }

    freopen("input1.txt", "r", stdin);
    for(int i = 0; i < 64; i++){
       for(int j = 0; j < 3; j++)
           scanf("%c", &ALPHcodons[i][j]);
       getchar(); 
       gets(ALPHacids[i]);      
    }
    freopen("output.txt", "w", stdout);
    int i = 0, l = 0, j = 0, k = 0;
    while(peptide[i] != '\0'){
        j = 0;
        l = 0;
        while(j <= 63){
            while(((ALPHacids[j][0] != peptide[i])||(strlen(ALPHacids[j]) != 1))&&(j <= 63)){
                j++;
            }
            if(j == 64){
                break;     
            }
            k = 0;
            a[i][l] = ALPHcodons[j][k];
            a[i][l + 1] = ALPHcodons[j][k + 1];
            a[i][l + 2] = ALPHcodons[j][k + 2]; 
            count[i]++;
            l = l + 3;
            j++;  
        }
        i++; 
    }
    
    int nG = 1;
    for(int i = 0; i < n; i++){
        nG = nG * count[i];            
    }
    
    char *s = new char[3 * n];
    char *sc = new char[3 * n];
    char *sD = new char[3 * n];
    p = new int[n + 1];
    for(int i = 0; i < n; i++){
        p[i] = 0;        
    }
    p[n] = '\0';
    for(int i = 0; i < nG; i++){
        for(int j = 0; j < n; j++){
            s[3 * j] = a[j][3 * p[j]];
            s[3 * j + 1] = a[j][3 * p[j] + 1];
            s[3 * j + 2] = a[j][3 * p[j] + 2];
        }
        s[3 * n] = 0;
        KMPMatcher(sRNA, s); 
        generate();          
    }
    for(int i = 0; i < n; i++){
        p[i] = 0;        
    }
    for(int i = 0; i < nG; i++){
        for(int j = 0; j < n; j++){
            s[3 * j] = a[j][3 * p[j]];
            s[3 * j + 1] = a[j][3 * p[j] + 1];
            s[3 * j + 2] = a[j][3 * p[j] + 2];
        }
        s[3 * n] = 0;
        complement(s, sc);
        KMPMatcher(sRNA, sc);   
        generate();          
    }
        
    for(int i = 0; i < countS; i++){
        for(int j = i + 1; j < countS; j++){
            funct(i, j, sDNA);  
        }        
    }
    printSubStr(sDNA);
return 0;    
}
