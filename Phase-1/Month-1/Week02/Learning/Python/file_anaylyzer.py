# Day 5 Exercise

import sys
import os
import json

def analyze_file(file_path):
    """تحليل ملف نصي وإرجاع إحصائياته."""
    if not os.path.exists(file_path):
        print(f"❌ خطأ: الملف '{file_path}' مش موجود.")
        return None
    if not os.path.isfile(file_path):
        print(f"❌ خطأ: '{file_path}' مش ملف صحيح.")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ خطأ أثناء القراءة: {e}")
        return None

    return {
        "filename": os.path.basename(file_path),
        "lines": len(content.splitlines()),
        "words": len(content.split()),
        "characters": len(content)
    }

def save_to_json(data, output_path="analysis.json"):
    """حفظ البيانات في ملف JSON."""
    if data is None:
        return
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ تم حفظ النتيجة في: {output_path}")

if __name__ == "__main__":
    # استقبال اسم الملف
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input("ادخل مسار الملف النصي: ")

    result = analyze_file(file_path)
    save_to_json(result)