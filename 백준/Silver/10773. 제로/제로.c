#include <stdio.h>
#define STACK_SIZE 100000

int stack[STACK_SIZE] = {0,};
int top = -1;

int isFull() {
	if (top >= STACK_SIZE - 1) {
		return 1;
	}
	return 0;
}

int isEmpty() {
	if (top == -1) {
		return 1;
	}
	return 0;
}

void push(int data) {
	if (!isFull()) {
		top++;
		stack[top] = data;
	}
}

int pop() {
	if (!isEmpty()) {
		return stack[top--];
	}
}

int main() {
	int K,N,sum=0;
	scanf("%d", &K);
	for (int i = 0; i < K; i++) {
		scanf("%d", &N);
		if (N == 0) {
			pop();
		}
		else {
			push(N);
		}
	}
	if (top > -1) {
		for (int i = 0; i <= top; i++) {
			sum += stack[i];
		}
		printf("%d", sum);
	}
	else {
		printf("0");
	}
	return 0;
}