#include<stdio.h>
#define num 100
int main() {
	int T, k, n;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d", &k);
		scanf("%d", &n);
		int result = 0;
		if (k >= 1 && n <= 14) {
			int count[num][14];
			for (int i = 0; i < n; i++) {
				count[0][i] = i+1;
			}
			for (int i = 0; i < k; i++) {
				count[i][0] = 1;
			}
			int i = 1;
			while (i != k) {
				int j = 1;
				while (j != n) {
					count[i][j] = count[i][j-1] + count[i-1][j];
						j++;
				}
				i++;
			}
			for (int i = 0; i < n; i++) {
				result += count[k - 1][i];
			}
			printf("%d\n", result);
		}
	}
	return 0;
}