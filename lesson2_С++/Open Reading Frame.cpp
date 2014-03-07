#include<stdio.h>
#include<string.h>

char ALPHacids[65][5], ALPHcodons[65][4], sPROT[10000][340], codon[4];
char s[15], sDNA[1001] = "", gDNA[1001] = "", gCDNA[1001] = "";
int countPROT, k[10000];

void complement(){
    int i = 0;
    int n = strlen(gDNA);
    while(i != n){
        if(gDNA[i] == 'A'){
           gCDNA[n - 1 - i] = 'T';            
        } 
        if(gDNA[i] == 'T'){
           gCDNA[n - 1 - i] = 'A';            
        }  
        if(gDNA[i] == 'C'){
           gCDNA[n - 1 - i] = 'G';            
        }  
        if(gDNA[i] == 'G'){
           gCDNA[n - 1 - i] = 'C';            
        }       
        i++;   
    } 
    gCDNA[n] = '\0';    
}

void find(char *DNA){
    int i = 0, j = 0, ist = 0, ktemp = 0;
    while(i <= strlen(DNA) - 6){
        j = 0;
        codon[0] = DNA[ist];
        codon[1] = DNA[ist + 1];
        codon[2] = DNA[ist + 2];
        while(!((codon[0] == 'A')&&(codon[1] == 'T')&&(codon[2] == 'G'))){  
            codon[0] = DNA[ist];
            codon[1] = DNA[ist + 1];
            codon[2] = DNA[ist + 2]; 
            ist++;      
        } 
        ist--;
        i = ist;
        while(i + 2 <= strlen(DNA) - 1){
            j = 0;
            while(!((ALPHcodons[j][0] == codon[0])&&(ALPHcodons[j][1] == codon[1])&&
                (ALPHcodons[j][2] == codon[2]))&&(j < 64)){
                j++;
            }
            if(j == 64){
                break;
            } 
            if(strlen(ALPHacids[j]) == 1){
                sPROT[countPROT][ktemp] = ALPHacids[j][0];
                ktemp++;
                i = i + 3;
                codon[0] = DNA[i];
                codon[1] = DNA[i + 1];
                codon[2] = DNA[i + 2];
            }    
            else{
                k[countPROT] = ktemp; 
                sPROT[countPROT][ktemp] = '\0';
                countPROT++;   
                //strcpy(sPROT[countPROT], "");
                ktemp = 0;
                break;     
            }
        }
        ist = ist + 3;
    } 
}

int main(){
    FILE *f;
    f = freopen("input.txt", "r", stdin);
    for(int i = 0; i < 10000; i++){
        k[i] = 0;        
    }
    countPROT = 0;
    scanf("%s", s);
    while(!feof(f)){
        strcpy(gDNA, "");
        scanf("%s\n", sDNA); 
        while(sDNA[0] != '>'){
            strcat(gDNA, sDNA);
            if(feof(f))
                break;  
            scanf("%s\n", sDNA);          
        }                    
    }
    freopen("input1.txt", "r", stdin);
    for(int i = 0; i < 64; i++){
       for(int j = 0; j < 3; j++)
           scanf("%c", &ALPHcodons[i][j]);
       getchar(); 
       gets(ALPHacids[i]);      
    }
    freopen("output.txt", "w", stdout);
    find(gDNA);
    complement();
    find(gCDNA);
    int t = 0;
    for(int i = 0; i < countPROT; i++){
        for(int j = i + 1; j < countPROT; j++){
            if(k[i] == k[j]){
                while((sPROT[i][t] == sPROT[j][t])&&(t < k[i])){
                    t++;
                } 
                if(t == k[j]){
                    k[j] = 0;   
                }
            }     
        }        
    }
    for(int i = 0; i < countPROT; i++){
        for(int l = 0; l < k[i]; l++){
            printf("%c", sPROT[i][l]);        
        }
        if(k[i] != 0){
            printf("\n");
        } 
    }
    return 0;    
}
