#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>

// a*l-----l*()a
/*
    Big(O) = O(n)
*/

struct ListNode {
    int val;
    struct ListNode *next;
};

void print_list_backwards(struct ListNode *head) {
    if (head == NULL) {
        return;
    };

    int capacity = 1;
    int *stack = (int*)malloc(sizeof(int) * 1);
    int count = 0;

    while (head) {
        if (capacity == count) {
            capacity += 1;
            stack = (int*)realloc(stack, sizeof(int) * capacity);
        }
        stack[count] = head->val;
        head = head->next;
        count++;
    }

    // count is top of the stack
    for (int i = count - 1; i >= 0; i--) {
        printf("%d ", stack[i]);
    }
    free(stack);
    printf("\n");
}

int main()
{   
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->val = 1;
    head->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->next->val = 2;
    head->next->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->next->next->val = 3;
    head->next->next->next = NULL;
    head->next->next->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->next->next->next->val = 4;
    head->next->next->next->next = NULL;
    print_list_backwards(head);
    return 0;
}