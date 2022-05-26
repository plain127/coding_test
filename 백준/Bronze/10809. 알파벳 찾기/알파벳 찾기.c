#include<stdio.h>
#include<string.h>
int checking(char *s1, int a) {
	int n=0;
	char b = a;
	char*ch = strchr(s1,b);
	if(ch == NULL){
		return -1;
	}
	else {
		n += strlen(s1) - strlen(ch);
		return n;
	}
}
int main() {
	char s1[100];
	scanf("%s", s1);
	for (int i = 97; i < 123; i++) {
		printf("%d ", checking(s1,i));
	}
	return 0;
}