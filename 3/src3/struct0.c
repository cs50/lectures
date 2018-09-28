// Demonstrates lack of structs

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Space for students
    int enrollment = get_int("Enrollment: ");
    string names[enrollment];
    string dorms[enrollment];

    // Prompt for students' names and dorms
    for (int i = 0; i < enrollment; i++)
    {
        names[i] = get_string("Name: ");
        dorms[i] = get_string("Dorm: ");
    }

    // Print students' names and dorms
    for (int i = 0; i < enrollment; i++)
    {
        printf("%s is in %s.\n", names[i], dorms[i]);
    }
}
