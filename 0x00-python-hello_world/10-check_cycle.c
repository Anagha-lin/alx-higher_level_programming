#include "lists.h"

/**
 * check_cycle - a function which checks if a all has a cycle in it.
 * @list: ptr to the first node
 * Return: returns 0 if no cycle and 1 if a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
