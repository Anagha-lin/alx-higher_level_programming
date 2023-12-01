class ShashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.snext = None
        self.sprev = None


class ShashTable:
    def __init__(self, size):
        self.size = size
        self.shead = None
        self.stail = None
        self.array = [None] * size

    def add_to_sorted_list(self, node):
        temp_var = self.shead

        if not temp_var and not self.stail:
            self.shead = self.stail = node
            return

        while temp_var:
            if node.key < temp_var.key:
                node.snext, node.sprev = temp_var, temp_var.sprev
                temp_var.sprev = node
                if node.sprev:
                    node.sprev.snext = node
                else:
                    self.shead = node
                return
            temp_var = temp_var.snext

        node.sprev = self.stail
        self.stail.snext = node
        self.stail = node

    def shash_table_set(self, key, value):
        if not self.array or self.size == 0 or not key or not value:
            return False

        index = hash(key) % self.size
        temp_var = self.array[index]

        while temp_var:
            if temp_var.key == key:
                temp_var.value = value
                return True
            temp_var = temp_var.next

        sh_node = ShashNode(key, value)
        sh_node.next, self.array[index] = self.array[index], sh_node
        self.add_to_sorted_list(sh_node)
        return True

    def shash_table_get(self, key):
        if not self.array or self.size == 0 or not key:
            return None

        index = hash(key) % self.size
        temp_var = self.array[index]

        while temp_var:
            if temp_var.key == key:
                return temp_var.value
            temp_var = temp_var.next

        return None

    def shash_table_print(self):
        if not self.array:
            return

        result = "{"
        temp_var = self.shead

        while temp_var:
            result += f"'{temp_var.key}': '{temp_var.value}'"
            temp_var = temp_var.snext
            if temp_var:
                result += ", "

        result += "}"
        print(result)

    def shash_table_print_rev(self):
        if not self.array:
            return

        result = "{"
        temp_var = self.stail

        while temp_var:
            result += f"'{temp_var.key}': '{temp_var.value}'"
            temp_var = temp_var.sprev
            if temp_var:
                result += ", "

        result += "}"
        print(result)

    def shash_table_delete(self):
        if not self.array or self.size == 0:
            return

        for i in range(self.size):
            while self.array[i]:
                next_node, self.array[i] = self.array[i].next, None
                del next_node

        self.array = None
        self.shead = self.stail = None
        self.size = 0


# Example usage:
# Uncomment the lines below to test the ShashTable class

# shash_table = ShashTable(10)
# shash_table.shash_table_set("key1", "value1")
# shash_table.shash_table_set("key2", "value2")
# shash_table.shash_table_print()
# shash_table.shash_table_print_rev()
# print(shash_table.shash_table_get("key1"))
# print(shash_table.shash_table_get("key3"))
# shash_table.shash_table_delete()

