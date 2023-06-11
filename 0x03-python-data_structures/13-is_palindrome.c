#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse_list - Reverses the order of a linked list
 * @head: pointer to the linked list
 * Return: pointer to the reversed linked list
*/
listint_t *reverse_list(listint_t **head)
{
	listint_t *current_nd = *head;
	listint_t *previous_nd = NULL;
	listint_t *next_node = NULL;

	while (current_nd != NULL)
	{
		next_node = current_nd->next;
		current_nd->next = previous_nd;
		previous_nd = current_nd;
		current_nd = next_node;
	}
	*head = previous_nd;
	return (*head);
}

/**
 * is_palindrome - Checks if a linked list is palindrome
 * @head: pointer to the linked list
 * Return: (0) if false, (1) if true
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *current = *head;
	listint_t *reverse;
	listint_t *half;

	/* Empty list or single node list is a palindrome */
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	/* if the length of the linked list is odd */
	if (fast != NULL)
	{
		slow = slow->next;
	}
	/* else if the length of the linked list is even */
	half = slow->next;
	/* Break the link between the first and second halves */
	slow->next = NULL;

	reverse = reverse_list(&half);
	/* Compare the first half with the reversed second half */
	while (current != NULL && reverse != NULL)
	{
		if (current->n != reverse->n)
		{
			reverse_list(&half);
			return (0); /* Not a palindrome */
		}
		current = current->next;
		reverse = reverse->next;
	}
	reverse_list(&half);
	return (1); /* Linked list is a palindrome */
}
