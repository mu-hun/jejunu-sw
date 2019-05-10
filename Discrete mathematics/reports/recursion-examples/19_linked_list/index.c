#include <stdio.h>
#include <stdlib.h>

typedef struct _node {
    int key;
    struct _node *next;
} node_t;

node_t *head = NULL, *tail = NULL;

void insert_node(int k)
{
    node_t *new_node = (node_t *) malloc(sizeof(node_t));

    new_node->key = k;
    new_node->next = NULL;
    if (head == NULL) {
        head = new_node;
        tail = new_node;
    } else {
        tail->next = new_node;
        tail = new_node;
    }
}

int delete_node()
{
	node_t *node;

	if (head == NULL) {
		return -1;
	}
	
	node = head;
	head = head->next;
	if (head == NULL) {
		tail = NULL;
	}
	return node->key;
}

void print_list(node_t * from)
{
    node_t *node;

    node = from;
    while (node != NULL) {
        printf("%d ", node->key);
        node = node->next;
    }
}

void print_list2(node_t * from)
{
    if (from == NULL)
        return;
    printf("%d ", from->key);
    print_list2(from->next);
}

void print_list_r(node_t * from)
{
    if (from == NULL)
        return;
    print_list_r(from->next);
    printf("%d ", from->key);
}

int main()
{
	int number;

	do {
		printf("input number: ");
		scanf("%d", &number);

		if (number > 0) {
			insert_node(number);
		}
		else if (number == 0) {
			int r;
			r = delete_node();
			printf("[%d]\n", r);
		}
	} while (number >= 0);

	print_list(head);
	//print_list_r(head);
	printf("\n");
	return 0;
}
