#include <Python.h>

void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        // Extract information about the Python string
        Py_ssize_t length = PyUnicode_GET_LENGTH(p);
        const char *utf8_str = PyUnicode_AsUTF8(p);

        // Print the information
        printf("  [.] string object info\n");
        printf("    type: %s\n", Py_TYPE(p)->tp_name);
        printf("    length: %ld\n", length);
        printf("    value: %s\n", utf8_str);
    } else {
        // Print an error message for non-string objects
        fprintf(stderr, "[ERROR] Invalid Python string object\n");
    }
}

int main(void) {
    // Initialize the Python interpreter
    Py_Initialize();

    // Create a Python string object
    PyObject *py_string = PyUnicode_FromString("Hello, Python!");

    // Print information about the Python string
    print_python_string(py_string);

    // Clean up
    Py_XDECREF(py_string);
    Py_Finalize();

    return 0;
}

