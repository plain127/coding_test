#include<stdio.h>
#include<string.h>
int main() {
	int T,R,i = 0;
	char S[21];
	scanf("%d",&T);
	if (T <= 1000 && T >= 1) {
		while (i < T) {
			scanf("%d %s",&R, S);
			for (int j = 0; j < strlen(S); j++) {
				for (int k = 0; k < R; k++) {
					printf("%c",S[j]);
				}
			}
			i++;
			printf("\n");
		}
	}
	return 0;
}