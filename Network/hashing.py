# -*- coding: utf-8 -*-
"""Hashing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kSgv_6NonWlCYG7ieVnXRGYo9wTQOnD8
"""

#TO-DO :-https://i.imgur.com/asgoQhK.png

import hashlib
toHash = input("Enter the string to be hashed: ")
result = hashlib.md5(toHash.encode())
print (result.hexdigest())