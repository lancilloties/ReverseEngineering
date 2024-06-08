#!/usr/bin/env python3
import sys

# Aisuru bot encryption scheme, reverse engineering from the decryption code.

strings = [
	"hqlogpf2",
	"2frus2"
]

plaintext_strings = [
	"/cmdline",
	"/proc/"
]

def encrypt_str(s):
	enc_str = ""
	for c in s:
		enc_str = enc_str + chr(ord(c)+3)
	return enc_str[::-1] # Reverse string

def decrypt_str(s):
	dec_str = ""
	for c in s:
		dec_str = dec_str + chr(ord(c)-3)
		# chr returns the string associated to the number.
		# ord returns the number associated to the string.
	#dec_str = "".join([chr(ord(c)-3) for c in s])[::-1] # Original line of code
	return dec_str[::-1] # Strings are encrypted & inversed([::-1] reverses a string)

print("Decrypting strings:")
i = 0
for s in strings:
	print("%d: %s" %(i, decrypt_str(s)))
	i += 1

print("Encrypting strings:")
i = 0
for s in plaintext_strings:
	print("%d: %s" %(i, encrypt_str(s)))
	i += 1
