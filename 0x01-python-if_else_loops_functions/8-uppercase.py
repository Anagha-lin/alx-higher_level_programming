#!/usr/bin/python3
def uppercase(str):
	upercase_str = ''

	for char in str:
		ascii_val = ord(char)
		if 97<= ascii_val <= 122:
			uppercase_char = chr(ascii_val - 32)
		else:
			uppercase_char = char
		upercase_str += uppercase_char
