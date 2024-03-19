#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *cat, *dog;

	if (list == NULL || list->next == NULL)
		return (0);

	cat = list->next;
	dog = list->next->next;

	while (cat && dog && dog->next)
	{
		if (cat == dog)
			return (1);

		cat = cat->next;
		dog = dog->next->next;
	}

	return (0);
