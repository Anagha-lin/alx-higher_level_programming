#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic information about a Python list.
 * @p: Python object representing a list.
 */
void print_python_list_info(PyObject *p)
{
    int size;
    int allocated;
    int i;

    size = Py_SIZE(p);
    allocated = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n");

    for (i = 0; i < size; i++)
    {
        printf("Element %d: ", i);
        printf("%s\n", Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

