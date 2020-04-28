#include "lists.h"
/**
 * insert_node - function that inserts a number into a sorted linked list.
 * @head: double pointer that points to the first element of the linked list.
 * @number: number to insert.
 * Return: The new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *current = *head;

	if (head == NULL)
		return(NULL);
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	new->n = number;
	new->next = current->next;
	current->next = new;

	return (new);
}
