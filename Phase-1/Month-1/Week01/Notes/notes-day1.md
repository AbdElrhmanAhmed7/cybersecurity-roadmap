
# اليوم 1 — 18/06/2026

## Phase 0 · Warm-Up


### **Built-in function**   
- 'open()' علشان افتح ملف جديد
- 'close()' علشان اقفل الملف وميعملش overflow
- 'read()' بتقرا كل الي موجود في الملف
- 'readline()' بتقرا سطر سطر ممكن تحطها جوا لوب وبتحرك الcursor معاها
- 'readlines()' بتقرا الملف كلوا وبتسقموا علي سطور في صيغة ليست وبتحرك الcursor معاها
    - يعني انا مقدرش اعمل 'readline()' بعديها علشان هيكون وصل EOF نهاية الملف يعني
- 'with open() as f:' بيفتح ويقفل الملف طول ما انا موجود في indented block


  ### *Modes for 'open()'*
  - 'r'دا الوضع الافتراضي بيقرا الملف
  - 'w' دا بكتب علي الملف وبيعمل resource leak
  - 'a' 
# اليوم 1 — 18/06/2026


## Reading and Writing files


## Phase 0 · Warm-Up


### **Built-in function**   
- 'open()' علشان افتح ملف جديد
- 'close()' علشان اقفل الملف وميعملش overflow
- 'read()' بتقرا كل الي موجود في الملف
- 'readline()' بتقرا سطر سطر ممكن تحطها جوا لوب وبتحرك الcursor معاها
- 'readlines()' بتقرا الملف كلوا وبتسقموا علي سطور في صيغة ليست وبتحرك الcursor معاها
    - يعني انا مقدرش اعمل 'readline()' بعديها علشان هيكون وصل EOF نهاية الملف يعني
- 'with open() as f:' بيفتح ويقفل الملف طول ما انا موجود في indented block


  ### *Modes for 'open()'*
  - 'r'دا الوضع الافتراضي بيقرا الملف
  - 'w' دا بكتب علي الملف وبيعمل resource leak
  - 'a' دا apppend بيعمل اضافة للملف عكس 'w'
    
    دول الي هستخدمهم عمتا والأساس
  - 'rb' & 'wb' دول نفس حوار الي فوق بس دا تبع ملغات ال binary  

#
## from pathlib import Path 

     'help()' is always your friend!!
- 'mkdir(exist_ok=True)' علشان لو الملف كان موجود ميعمبش ايرور
- 'touch()' علشان نعمل ملف نفس لينكس
- Path("a") / "b" / "c" → دمج مسارات
- read_text() / write_text() → قراءة/كتابة سريعة
- exists() / is_file() / is_dir() → فحص الملف
- glob("*.txt") → بحث عن ملفات
- rename() / replace() → نقل ملفات

## ❌ الغلطات
- rename() فشل لأن الملف موجود → استخدم replace() أو افحص exists()
- glob("*") جاب المجلدات كمان → استخدم is_dir() أو glob("*.*")
دا apppend بيعمل اضافة للملف عكس 'w'
    
    دول الي هستخدمهم عمتا والأساس
  - 'rb' & 'wb' دول نفس حوار الي فوق بس دا تبع ملغات ال binary  

#
## from pathlib import Path 

     'help()' is always your friend!!
- 'mkdir(exist_ok=True)' علشان لو الملف كان موجود ميعمبش ايرور
- 'touch()' علشان نعمل ملف نفس لينكس