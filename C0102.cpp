#include <stdio.h>
int main(){
  //resolve o problema para qualquer número de retangulos, como o problema são 4, basta setar 4 ao executar
	int n;
	char tab[1000010];
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		tab[i]='>';
	}
	tab[n]='_';
	for (int i=n+1;i<2*n+1;i++){
		tab[i]='<';
	}
	int vazio=n;
	int movimentos=-1;
	bool alternou=false;
	bool terminou=false;
	while (!terminou){
		movimentos++;
		for (int i=0;i<2*n+1;i++)printf("%c",tab[i]);
		printf("\n");
		int antvazio=vazio;
		if (vazio>0 && vazio<2*n){
			if (tab[vazio-1]!=tab[vazio+1] && !alternou){
				if (vazio<n && tab[vazio-1]=='>'){
					tab[vazio]=tab[vazio-1];
					tab[vazio-1]='_';
					vazio--;
				}else if (vazio>=n && tab[vazio+1]=='<'){
					tab[vazio]=tab[vazio+1];
					tab[vazio+1]='_';
					vazio++;
				}
			}
			else if (!alternou){
				if (tab[vazio+2]=='<' && tab[vazio+2]!=tab[vazio-1]){
					tab[vazio]=tab[vazio+2];
					tab[vazio+2]='_';
					vazio+=2;
				}else if (tab[vazio-2]=='>' && tab[vazio-2]!=tab[vazio+1]){
					tab[vazio]=tab[vazio-2];
					tab[vazio-2]='_';
					vazio-=2;
				}	
			}
			if (alternou){
				if (tab[vazio+2]=='<'){
					tab[vazio]=tab[vazio+2];
					tab[vazio+2]='_';
					vazio+=2;
				}else if (tab[vazio-2]=='>'){
					tab[vazio]=tab[vazio-2];
					tab[vazio-2]='_';
					vazio-=2;
				}
				else if (tab[vazio-1]=='>'){
					tab[vazio]=tab[vazio-1];
					tab[vazio-1]='_';
					vazio--;
				}else if (tab[vazio+1]=='<'){
					tab[vazio]=tab[vazio+1];
					tab[vazio+1]='_';
					vazio++;
				}
			}
		}else {
			if (vazio==0 && tab[vazio+2]=='<'){
				tab[vazio]=tab[vazio+2];
				tab[vazio+2]='_';
				vazio+=2;
			}
			else if (vazio==0 && tab[vazio+1]=='<'){
				tab[vazio]=tab[vazio+1];
				tab[vazio+1]='_';
				vazio++;
			}
			else if (vazio==2*n && tab[vazio-1]=='>'){
				tab[vazio]=tab[vazio-1];
				tab[vazio-1]='_';
				vazio--;
			}
			else if (vazio==2*n && tab[vazio-2]=='>'){
				tab[vazio]=tab[vazio-2];
				tab[vazio-2]='_';
				vazio-=2;
			}
			alternou=true;
		}
		if (vazio==antvazio)terminou=true;
	}
	printf("Acabou em %d movimentos\n",movimentos);
	return 0;
}
