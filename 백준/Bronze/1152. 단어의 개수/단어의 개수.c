#include<stdio.h>
#include<string.h>
#define N 1000000
int main() {
	char arr[N];
	int num,count=0;
	scanf("%[^\n]", arr);
	num = strlen(arr);
	if (num == 1) {
		if (arr[0] == ' ') {
			printf("0\n");
			return 0;
		}
	}
	for (int i = 1; i < num-1; i++) {
		if (arr[i] == ' ') {
			count++;
		}
	}
	printf("%d", count+1);
	return 0;
}