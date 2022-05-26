#include <stdio.h>

int main() {
	int A,B,C,n,N[10] = {0,},k,l,count=0,num,result;
	scanf("%d\n%d\n%d", &A, &B, &C);
	if ((A >= 100 && A < 1000) && (B >= 100 && B < 1000) && (C >= 100 && C < 1000)) {
		n = A * B * C;
		k = n;
		while(1){
			l = k / 10;
			if (l == 0) {
				break;
			}
			count += 1;
			k = l;
		}
		for(int i = 0; i <= count; i++) {				
			int j = 0;
			int t = 1;
			while (j<i) {
				t *= 10 ;
				j++;
			}
			num = n%(t*10);
			if (num == 0) {
					N[0] += 1;
			}
			else {
				result=num / t;
				N[result] +=1;
			}		
		}
	}
	for (int i = 0; i < 10; i++) {
		printf("%d\n",N[i]);
	}
	return 0;
}