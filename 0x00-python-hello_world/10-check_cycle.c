#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: linked list to check.
 * Return: 1 if the list has
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *check = head;

	while (head != NULL && check != NULL && check->next != NULL)
	{
		head = head->next;
		check = check->next->next;

		if (check == head)
		{
			return (1);
		}
	}
	return (0);
}
