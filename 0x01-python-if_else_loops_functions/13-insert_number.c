#include "lists.h"
/**
 * insert_node - function that inserts a number into a sorted linked list.
 * @head: double pointer that points to the first element of the linked list.
 * @number: number to insert.
 * Return: The new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (*head == NULL)
	{
		*head = new;
		new->n = number;
		new->next = NULL;
		return (new);
	}

	while (current)
	{
		if (number <= current->n)
		{
			new->n = number;
			new->next = current;
			*head = new;
			return (new);
		}
		if (current->next == NULL && number >= current->n)
		{
			new->n = number;
			new->next = NULL;
			current->next = new;
			return (new);
		}
		if (number >= current->n && number <= current->next->n)
		{
			new->n = number;
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}
