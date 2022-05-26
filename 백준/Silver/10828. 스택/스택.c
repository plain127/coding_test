#include <stdio.h>
#include <string.h>
#define STACK_SIZE 10000

int stack[STACK_SIZE];
int top = -1;

int isFull() {
	if (top >= STACK_SIZE - 1) {
		return 1;
	}
	else {
		return 0;
	}
}
int isEmpty() {
	if (top == -1) {
		return 1;
	}
	else {
		return 0;
	}
}

void push(int data) {
	if (!isFull()) {
		top++;
		stack[top] = data;
	}
}

int pop() {
	if (!isEmpty()) {
		printf("%d\n",stack[top--]);
	}
	else {
		printf("-1\n");
	}
}

int main() {
	int N,n;
	char s[10];
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf("%s", &s);
		if (strcmp(s,"push")==0) {
			scanf("%d",&n);
			push(n);
		}
		else if (strcmp(s, "pop") == 0) {
			pop();
		}
		else if (strcmp(s, "size") == 0) {
			printf("%d\n",top+1);
		}
		else if (strcmp(s, "empty") == 0) {
			printf("%d\n", isEmpty());
		}
		else if (strcmp(s, "top") == 0) {
						
			if (isEmpty()){
				printf("-1\n");
			}
			else {
				printf("%d\n",stack[top]);
			}
		}
	}

	return 0;
}