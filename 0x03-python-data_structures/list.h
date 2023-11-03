#ifndef ALX_LISTS_H
#define ALX_LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct alx_listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for the ALX project
 */
typedef struct alx_listint_s
{
    int n;
    struct alx_listint_s *next;
} alx_listint_t;

size_t print_alx_listint(const alx_listint_t *h);
alx_listint_t *add_alx_nodeint_end(alx_listint_t **head, const int n);
void free_alx_listint(alx_listint_t *head);

int is_palindrome(alx_listint_t **head);

#endif /* ALX_LISTS_H */

