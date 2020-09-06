// Demonstrates file I/O

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "struct.h"

int main(void)
{
    // allocate memory for students
    int enrollment = get_int("enrollment: ");
    student students[enrollment];

    // prompt for students' names and dorms
    for (int i = 0; i < enrollment; i++)
    {
        students[i].name = get_string("name: ");
        students[i].dorm = get_string("dorm: ");
    }

    // save students to disk
    FILE *file = fopen("students.csv", "w");
    if (file)
    {
        for (int i = 0; i < enrollment; i++)
        {
            fprintf(file, "%s,%s\n", students[i].name, students[i].dorm);
        }
        fclose(file);
    }
}
