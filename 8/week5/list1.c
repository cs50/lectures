/**
 * Demonstrates a linked list for students.
 */

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "list1.h"

// linked list
node *first = NULL;

// prototypes
void delete(void);
void insert(void);
void search(void);
void traverse(void);

int main(void)
{
    int c;
    do
    {
        // print instructions
        printf("\nMENU\n\n"
            "1 - delete\n"
            "2 - insert\n"
            "3 - search\n"
            "4 - traverse\n"
            "0 - quit\n\n");

        // get command
        printf("Command: ");
        c = get_int();

        // try to execute command
        switch (c)
        {
            case 1: delete(); break;
            case 2: insert(); break;
            case 3: search(); break;
            case 4: traverse(); break;
        }
    }
    while (c != 0);

    // free list before quitting
    node *ptr = first;
    while (ptr != NULL)
    {
        node *predptr = ptr;
        ptr = ptr->next;
        if (predptr->student != NULL)
        {
            if (predptr->student->name != NULL)
            {
                free(predptr->student->name);
            }
            if (predptr->student->dorm != NULL)
            {
                free(predptr->student->dorm);
            }
            free(predptr->student);
        }
        free(predptr);
    }
}

/**
 * Tries to delete a student.
 */
void delete(void)
{
    // prompt user for ID
    printf("ID to delete: ");
    int n = get_int();

    // get list's first node
    node *ptr = first;

    // try to delete student from list
    node *predptr = NULL;
    while (ptr != NULL)
    {
        // check for ID
        if (ptr->student->id == n)
        {
            // delete from head
            if (ptr == first)
            {
                first = ptr->next;
                free(ptr->student->name);
                free(ptr->student->dorm);
                free(ptr->student);
                free(ptr);
            }

            // delete from middle or tail
            else
            {
                predptr->next = ptr->next;
                if (ptr->student->name != NULL) 
                {
                    free(ptr->student->name);
                }
                if (ptr->student->dorm != NULL) 
                {
                    free(ptr->student->dorm);
                }
                free(ptr->student);
                free(ptr);
            }

            // all done
            break;
        }
        else
        {
            predptr = ptr;
            ptr = ptr->next;
        }
    }

    // traverse list
    traverse();
}

/**
 * Tries to insert a student into list.
 */
void insert(void)
{
    // try to instantiate node for student
    node *newptr = malloc(sizeof(node));
    if (newptr == NULL)
    {
        return;
    }

    // initialize node
    newptr->next = NULL;

    // try to instantiate student
    newptr->student = malloc(sizeof(student));
    if (newptr->student == NULL)
    {
        free(newptr);
        return;
    }

    // try to initialize student
    printf("Student's ID: ");
    newptr->student->id = get_int();
    printf("Student's name: ");
    newptr->student->name = get_string();
    printf("Student's dorm: ");
    newptr->student->dorm = get_string();
    if (newptr->student->name == NULL || newptr->student->dorm == NULL)
    {
        if (newptr->student->name != NULL)
        {
            free(newptr->student->name);
        }
        if (newptr->student->dorm != NULL)
        {
            free(newptr->student->dorm);
        }
        free(newptr->student);
        free(newptr);
        return;
    }

    // check for empty list
    if (first == NULL)
    {
        first = newptr;
    }

    // else check if student belongs at list's head
    else if (newptr->student->id < first->student->id)
    {
        newptr->next = first;
        first = newptr;
    }

    // else try to insert student in middle or tail
    else
    {
        node *predptr = first;
        while (true)
        {
            // avoid duplicates
            if (predptr->student->id == newptr->student->id)
            {
                free(newptr->student->name);
                free(newptr->student->dorm);
                free(newptr->student);
                free(newptr);
                break;
            }

            // check for insertion at tail
            else if (predptr->next == NULL)
            {
                predptr->next = newptr;
                break;
            }

            // check for insertion in middle
            else if (predptr->next->student->id > newptr->student->id)
            {
                newptr->next = predptr->next;
                predptr->next = newptr;
                break;
            }

            // update pointer
            predptr = predptr->next;
        }
    }

    // traverse list
    traverse();
}


/**
 * Searches for student in list via student's ID.
 */
void search(void)
{
    // prompt user for ID
    printf("ID to search for: ");
    int id = get_int();

    // get list's first node
    node *ptr = first;

    // search for student
    while (ptr != NULL)
    {
        if (ptr->student->id == id)
        {
            printf("\nFound %s of %s (%i)!\n", ptr->student->name, ptr->student->dorm, id);
            sleep(1);
            break;
        }
        ptr = ptr->next;
    }
}

/**
 * Traverses list, printing its numbers.
 */
void traverse(void)
{
    // traverse list
    printf("\nLIST IS NOW: ");
    node *ptr = first;
    while (ptr != NULL)
    {
        printf("%s of %s (%i)  ", ptr->student->name, ptr->student->dorm, ptr->student->id);
        ptr = ptr->next;
    }

    // pause before continuing
    sleep(1);
    printf("\n\n");
}
