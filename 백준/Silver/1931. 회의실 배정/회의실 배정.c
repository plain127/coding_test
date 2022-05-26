#include <stdio.h>
#include <stdlib.h>

typedef struct arr {
	int sta,end;
}Arr;

int compare(const void*, const void*);

int main() {
	int N,s,e,last=0,count=0;
	scanf("%d", &N);
	Arr* num;
	num = (Arr*)calloc(N, sizeof(Arr));
	if (N <= 100000 && N >= 1) {
		for (int i = 0; i < N; i++) {
			scanf("%d %d", &s, &e);
			num[i].sta = s;
			num[i].end = e;
		}
	}
	qsort(num,N,sizeof(Arr),compare);
	for (int i = 0; i < N; i++) {
		if (num[i].sta >= last) {
			count++;
			last = num[i].end;
		}
	}
	printf("%d", count);
	free(num);
	return 0;
}

int compare(const void *a, const void *b) {
	const Arr* n1, * n2;
	n1 = (const Arr*)a;
	n2 = (const Arr*)b;
	if (n1->end != n2->end) {
		if (n1->end < n2->end) {
			return -1;
		}
		else if (n1->end == n2->end) {
			return 0;
		}
		else {
			return 1;
		}
	}
	else {
		if (n1->sta < n2->sta) {
			return -1;
		}
		else if (n1->sta == n2->sta) {
			return 0;
		}
		else {
			return 1;
		}
	}
}