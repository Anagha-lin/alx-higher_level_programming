#include <Python.h>
#include <floatobject.h>
#include <bytesobject.h>
#include <listobject.h>

/**
 * print_python_list - Print information about a Python list.
 * @p: Pointer to a PyObject representing a Python list.
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        item = ((PyListObject *)p)->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: Pointer to a PyObject representing a Python bytes object.
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *data;

    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    data = ((PyBytesObject *)p)->ob_sval;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", data);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; ++i) {
        printf("%02x", data[i] & 0xff);
        if (i < size - 1 && i < 9)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: Pointer to a PyObject representing a Python float object.
 */
void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  type: %s\n", Py_TYPE(p)->tp_name);
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

