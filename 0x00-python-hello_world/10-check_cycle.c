#include "lists.h"
/**
 * check_cycle - Checks if the list has a cycle
 * @list: list to check
 * Return: 0 if it false, 1 if it true
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	if (list == NULL)
		return (0);

	while (first != NULL && second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
		{
			return (1);
		}
	}
	return (0);
}
