#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Inserts number into a sorted linked list
 * @head: double pointer to the linked list
 * @number: number to be inserted
 * Return: pointer to the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node;

	if (*head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	/* if new node is the head */
	if (current == NULL || current->n >= new_node->n)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	/* else */
	while (current->next != NULL && current->next->n < new_node->n)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
