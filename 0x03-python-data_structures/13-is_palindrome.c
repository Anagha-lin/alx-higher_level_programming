#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head)
{
    if (*head == NULL) {
        return 1;  // An empty list is considered a palindrome
    }

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    // Find the middle of the list and reverse the first half
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        // Reverse the first half of the list
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // If the list has an odd number of elements, skip the middle element
    if (fast != NULL) {
        slow = slow->next;
    }

    // Compare the reversed first half with the second half
    while (slow != NULL) {
        if (prev->n != slow->n) {
            return 0;  // Not a palindrome
        }
        prev = prev->next;
        slow = slow->next;
    }

    return 1;  // It's a palindrome
}

int main()
{
    listint_t *head = NULL;

    // Example 1: A palindrome list
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 1);
    printf("Is palindrome: %d\n", is_palindrome(&head));  // Output: 1 (True)

    // Example 2: Not a palindrome list
    listint_t *head2 = NULL;
    add_nodeint_end(&head2, 1);
    add_nodeint_end(&head2, 2);
    add_nodeint_end(&head2, 3);
    printf("Is palindrome: %d\n", is_palindrome(&head2));  // Output: 0 (False)

    return 0;
}

