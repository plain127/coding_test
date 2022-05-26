#include<stdio.h>
int main() {
	int T, H, W, N,floor,room,no;
	scanf("%d",&T);
	for (int i = 0; i < T; i++) {
		scanf("%d %d %d", &H, &W, &N);
		if (1 <= H && W <= 99 && 1 <= N && N <= H * W){
			floor = 0;
			room = 0;
			if (N % H == 0) {
				floor = H;
				room = N / H;
			}
			else {
				floor = N % H;
				room = N / H + 1;
			}
			no = floor * 100 + room;
			printf("%d\n", no);
		}
	}
	return 0;
}