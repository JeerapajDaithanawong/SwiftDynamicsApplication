# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:50:19 2024
เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน Array ด้วยภาษา python เช่น [1,2,1,3,5,6,4] ลำดับที่มีค่ามากที่สุด คือ index = 5 โดยไม่ให้ใช้ฟังก์ชั่นที่มีอยู่แล้ว ให้ใช้แค่ลูปกับการเช็คเงื่อนไข
@author: vindi
"""

def find_max_index(lst):
    if not lst:
        return None  # Handle empty list case
    
    max_index = 0
    max_value = lst[0]

    for i in range(len(lst)):
        if lst[i] > max_value:
            max_index = i
            max_value = lst[i]

    return max_index

my_list = [10, 50, 20, 15, 30]
index_of_max = find_max_index(my_list)
print("Index of the largest item:", index_of_max)