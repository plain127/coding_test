#include<stdio.h>
#include<string.h>
#define N 1000000
int main() {
	char s1[N];
	int sum[26] = { 0, },max, n = 0, m = 0, len;
	scanf("%s", s1);
	len = strlen(s1);
	for (int j = 'a'; j <= 'z'; j++) {
		for (int i = 0; i < len; i++) {
			if (s1[i]==j) {
				sum[j-'a'] += 1;
			}
		}
	}
	for (int i = 'A'; i <= 'Z'; i++) {
		for (int j = 0; j < len; j++) {
			if (s1[j] == i) {
				sum[i-'A'] += 1;
			}
		}
	}
	max = sum[0];
	for (int i = 0; i < 26; i++) {
		if (max < sum[i]) {
			max = sum[i];
			n = i;
		}
	}
	for(int i = 0; i < 26; i++){
		if (max == sum[i]){
			m++;
		}
	}
	if (m>1) {
			printf("?\n");
	}	
	else {
		printf("%c", n+'A');
	}
	return 0;
}