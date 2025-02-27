#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>


struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry = 0;
    struct ListNode* res = NULL;
    struct ListNode* curr = NULL;

    while (l1 || l2 || carry) {
        int n1 = l1 ? l1->val : 0;
        int n2 = l2 ? l2->val : 0;
        int sum = n1 + n2 + carry;

        if(res == NULL) {
            res = (struct ListNode*)malloc(sizeof(struct ListNode));    
            res->val = sum % 10;
            curr = res;
        }
        else {
            struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));    
            node->val = sum % 10;
            curr->next = node;
            curr = curr->next;
        }

        carry = sum / 10;

        l1 = l1 ? l1->next : NULL;
        l2 = l2 ? l2->next : NULL;
    }

    return res;
}

int main()
{   
    struct ListNode* l1 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l1->val = 2;
    l1->next = NULL;

    struct ListNode* l2 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l2->val = 9;
    l2->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    l2->next->val = 9;
    l2->next->next = (struct ListNode*)malloc(sizeof(struct ListNode));
    l2->next->next->val = 9;
    l2->next->next->next = NULL;

    struct ListNode* res = addTwoNumbers(l1, l2);

    while (res) {
        printf("%d ", res->val);
        res = res->next;
    }
    return 0;
}