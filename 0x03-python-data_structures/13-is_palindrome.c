#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: pointer to the first element of a linked list
 * Return: 1 if the list is palindrome or 0 if is not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *list = (*head);
	int elements[4096];
	int i = 0, j;

	if (head == NULL || *head == NULL)
		return (1);

	while (list)
	{
		elements[i] = list->n;
		i++;
		list = list->next;
	}
	i--;
	for (j = 0; j <= i ; i--, j++)
	{
		if (elements[i] != elements[j])
			return (0);
	}
	return (1);
}
