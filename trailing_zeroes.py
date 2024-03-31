# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:57:40 2024
เขียนโปรแกรมหาจำนวนเลข 0 ที่อยู่ติดกันหลังสุดของค่า factorial ด้วย Python โดยห้ามใช้ math.factorial เช่น 7! = 5040 มีเลข 0 ต่อท้าย 1 ตัว, 10! = 3628800 มีเลข 0 ต่อท้าย 2 ตัว
@author: vindi
"""

def count_trailing_zeroes(n):
    if n < 0:
        return 0

    count = 0
    i = 5
    while n // i > 0: #basically counting factors
        count += n // i
        i *= 5

    return count


number = 10
trailing_zeroes = count_trailing_zeroes(number)
print("Number of trailing zeroes in", number, "factorial:", trailing_zeroes)