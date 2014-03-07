#include<stdio.h>
#include<string.h>
#include<conio.h>
int main(){
    int i = 0, j = 0, k = 0;
    char sRNA[10001], ALPHacids[64][4], ALPHcodons[64][3], sPROT[3400], codon[3];
    freopen("input.txt", "r", stdin);
    gets(sRNA);
    freopen("input1.txt", "r", stdin);
    for(int i = 0; i < 64; i++){
       for(int j = 0; j < 3; j++)
           scanf("%c", &ALPHcodons[i][j]);
       getchar(); 
       gets(ALPHacids[i]);      
    }
    freopen("output.txt", "w", stdout);
    i = 0;
    while(sRNA[i] != '\0'){
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
            break;   
        }
    }
    puts(sPROT);
    return 0;    
}
