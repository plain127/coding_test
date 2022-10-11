#include <stdio.h>
#include <string.h>
#define STACK 51

int main() {
	int T;
	char stack[STACK];
	scanf("%d",&T);
	for(int i = 0; i < T; i++){
		int j=0,sum = 0;
		scanf("%s", stack);
		while(stack[j]!=NULL) {
				if (stack[j] == '(') {
					sum++;
				}
				if (stack[j] == ')') {
					sum--;
				}
				if (sum < 0)
				{
					printf("NO\n");
					break;
				}
				j++;
		}
		if (sum == 0) {
			printf("YES\n");
		}
		else if(sum>0) {
			printf("NO\n");
		}
	}
	return 0;
}