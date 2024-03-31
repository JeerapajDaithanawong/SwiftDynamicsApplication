
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def intToText(num):
 
    # Storing roman values of digits from 0-9
    # when placed at different places
    words = {
        0: '', 1: 'หนึ่ง', 2: 'สอง', 3: 'สาม', 4: 'สี่',
        5: 'ห้า', 6: 'หก', 7: ' เจ็ด', 8: 'แปด', 9: 'เก้า'
    }
    words2 = {
        0: '', 1: '', 2: 'ยี่', 3: 'สาม', 4: 'สี่',
        5: 'ห้า', 6: 'หก', 7: ' เจ็ด', 8: 'แปด', 9: 'เก้า'
    }

    words3 = {
        0: '', 1: '​เอ็ด', 2: 'สอง', 3: 'สาม', 4: 'สี่',
        5: 'ห้า', 6: 'หก', 7: ' เจ็ด', 8: 'แปด', 9: 'เก้า'
    }
    
    millions = num // 1000000
    hundred_thousands = (num % 1000000) // 100000
    ten_thousands = (num % 100000) // 10000
    thousands = (num % 10000) // 1000
    hundreds = (num % 1000) // 100
    tens = (num % 100) // 10
    ones = num % 10
    
    ans = ''
    if millions > 0:
        ans += words[millions] + 'ล้าน'
    if hundred_thousands > 0:
        ans += words[hundred_thousands] + 'แสน'
    if ten_thousands > 0:
        ans += words[ten_thousands] + 'หมื่น'
    if thousands > 0:
        ans += words[thousands] + 'พัน'
    if hundreds > 0:
        ans += words[hundreds] + 'ร้อย'
    if tens > 0: 
        ans += words2[tens] + 'สิบ'
    if ones > 0 and tens > 0: #depends if integer contains something in the tens place or not given that it changes based on thai grammar
        ans += words3[ones]
    elif ones > 0 and tens == 0:
        ans += words[ones]

 
    return ans

valid = True
while valid:
    arabic = int(input("Enter an Arabic Number: "))
    if arabic <= 0 or arabic > 10000000:
        print("Arabic number out of range.")
        valid = False
    print(intToText(arabic))