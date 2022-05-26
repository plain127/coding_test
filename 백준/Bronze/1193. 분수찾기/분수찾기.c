#include<stdio.h>
int cal(int i);

int main() {
	int X,i=1,cnt=0,a=0,b=0;
	scanf("%d", &X);
	if (1 <= X && X <= 10000000) {
		while (1) {
			if (cal(i - 1) <= X && X <= cal(i)) {
				break;
			}
			i++;
		}
		if (i % 2 == 0) {
			cnt = cal(i) - X;
			a = i - cnt;
			b = cnt + 1;
		}
		else if (i % 2 != 0) {
			cnt = cal(i) - X;
			a = cnt + 1;
			b = i - cnt;
		}
	}
	printf("%d/%d", a, b);
	return 0;
}

int cal(int i) {
	int n;
	n = i * (i + 1) / 2;
	return n;
}