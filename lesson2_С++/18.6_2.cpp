#include<stdio.h>
#include<string.h>
#include<conio.h>

char peptide[10001];
char sDNA[10001], ALPHacids[64][4], ALPHcodons[64][3], codon[3];
int count, pos;
int arr[10001];
int *pi;
int n, m;

void translateRNAintoPRT(char *sPROT, char *sRNA, int pos){
    freopen("input1.txt", "r", stdin);
    for(int i = 0; i < 64; i++){
       for(int j = 0; j < 3; j++)
           scanf("%c", &ALPHcodons[i][j]);
       getchar(); 
       gets(ALPHacids[i]);      
    }    
    int i = 0, j = 0, k = 0;
    i = pos;
    while(i <= strlen(sRNA) - 3){
        j = 0;
        for(int l = 0; l < 3; l++){
            codon[l] = sRNA[i];
            i++;
        }
        while(!((ALPHcodons[j][0] == codon[0])&&(ALPHcodons[j][1] == codon[1])&&
                (ALPHcodons[j][2] == codon[2]))){
            j++;
        }      
        if(strlen(ALPHacids[j]) == 1){
            sPROT[k] = ALPHacids[j][0];
            k++;
        }
        else{
            sPROT[k] = '\0'; 
            return;   
        }
    }
    sPROT[k] = '\0';  
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

void complement(char *s, char *sc){
    int i = 0;
    int n = strlen(s);
    while(i < n){
        if(s[i] == 'A'){
           sc[n - 1 - i] = 'T';            
        } 
        if(s[i] == 'T'){
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
            arr[count] = 3 * (i - m + 1) + pos;
            count++;
            q = pi[q];     
        }        
    }    
}

void funct(int i, int j, char *s1, char *s2){
    if(arr[j] != -1){
        int d = 0;
        while(s1[arr[i] + d] == s2[arr[j] + d]){
            d++;
            if(d == strlen(peptide) * 3){
                arr[j] = -1;
                break;     
            }              
        }             
    }     
}

void printSubStr(char *sDNA, char *scDNA, int sect){
    for(int i = 0; i < count; i++){
        if(i < sect){
            for(int j = 0; j < 3 * strlen(peptide); j++){
                if(arr[i] != -1){
                    printf("%c", sDNA[arr[i] + j]); 
                }           
            } 
            if(arr[i] != -1){
                printf("\n"); 
            }         
        } 
        if(i >= sect){
            for(int j = 0; j < 3 * strlen(peptide); j++){
                if(arr[i] != -1){
                    printf("%c", scDNA[arr[i] + j]); 
                }           
            }
            if(arr[i] != -1){
                printf("\n"); 
            }        
        }         
    }              
}

int main(){
    char a[500][100];
    char sPRT[3400], scPRT[3400];
    int sect;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    gets(sDNA);
    gets(peptide);
    char *scDNA = new char[strlen(sDNA)];
    char *sRNA = new char[strlen(sDNA)];
    char *scRNA = new char[strlen(sDNA)];
    complement(sDNA, scDNA);
    DNAintoRNA(sDNA, sRNA);
    DNAintoRNA(scDNA, scRNA);  
    
    count = 0;
    for(pos = 0; pos < 3; pos++){
        translateRNAintoPRT(sPRT, sRNA, pos);
        KMPMatcher(sPRT, peptide);
    }
    sect = count;
    for(pos = 0; pos < 3; pos++){        
        translateRNAintoPRT(scPRT, scRNA, pos);
        KMPMatcher(scPRT, peptide);  
    }
        
    for(int i = 0; i < count; i++){
        for(int j = i + 1; j < count; j++){
            if((i < sect) && (j < sect)){
                funct(i, j, sRNA, sRNA);     
            }
            if((i < sect) && (j >= sect)){
                funct(i, j, sRNA, scRNA);     
            }
            if((i >= sect) && (j >= sect)){
                funct(i, j, scRNA, scRNA);     
            }          
        }        
    }
    
    printSubStr(sDNA, scDNA, sect);
     
return 0;    
}

