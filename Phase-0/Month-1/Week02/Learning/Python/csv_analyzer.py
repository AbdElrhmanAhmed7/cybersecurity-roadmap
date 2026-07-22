# Day 10

from sys import argv
from os import path
from csv import DictReader
from json import dump

def detect_encoding(file_path):
    """
    تحاول تفتح الملف بأكتر من ترميز عشان متقفش قدام UTF-16 أو UTF-8.
    """
    encodings = ['utf-8', 'utf-16']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                f.read()
            return enc
        except UnicodeDecodeError:
            continue
    return None

def read_csv(file_path):
    """
    تقرأ ملف CSV وتحوله لـ list of dicts.
    لو حصل أي مشكلة، ترجع None عشان البرنامج ميكسرش.
    """
    try:
        encoding = detect_encoding(file_path)
        if encoding is None:
            print("Error: Unable to detect file encoding (tried UTF-8 and UTF-16).")
            return None

        with open(file_path, 'r', encoding=encoding) as f:
            return list(DictReader(f))
    
    except Exception as e:
        print(f"Error: Invalid CSV format or corrupted file. Details: {e}")
        return None

def calculate_stats(rows, column_name):
    """
    تحسب التكرارات، القيم الفريدة، والقيمة الأكثر تكراراً.
    """
    freq = {}
    
    for row in rows:
        value = row[column_name]
        # الطريقة الاحترافية (بتاعت .get) عشان توفر السطور
        freq[value] = freq.get(value, 0) + 1

    # القيم الفريدة = عدد المفاتيح في القاموس (أسهل من الـ loop اللي كنت بتعمله)
    unique_count = len(freq)
    
    # العنصر الأكثر تكراراً باستخدام max (اختصر الـ loop الطويل بتاعك)
    most_common = max(freq, key=freq.get) if freq else None

    return {
        "total_rows": len(rows),
        "column_analyzed": column_name,
        "unique_values": unique_count,
        "most_common": most_common,
        "frequency": freq
    }

def save_to_json(data):
    """
    تحفظ النتيجة في ملف JSON.
    """
    with open("analysis_report.json", "w", encoding='utf-8') as f:
        dump(data, f, indent=4)
    print("✅ Report saved successfully to analysis_report.json")

def main():
    # 1. استقبال اسم الملف
    if len(argv) != 2:
        file_path = input("Please enter the CSV file name: ")
    else:
        file_path = argv[1]

    # 2. التحقق من وجود الملف ونوعه (إصلاح الـ AND لـ OR)
    if not path.exists(file_path):
        print("Error: File not found.")
        return
    if not path.isfile(file_path) or not file_path.lower().endswith(".csv"):
        print("Error: The provided path is not a valid CSV file.")
        return

    # 3. قراءة الملف (مع Try/Except)
    rows = read_csv(file_path)
    if rows is None:
        return  # لو حصل خطأ، نقف هنا

    # 4. التحقق من وجود العمود المطلوب (عشان ميحصلش KeyError)
    column = "age"
    if rows and column not in rows[0]:
        print(f"Error: Column '{column}' not found in CSV. Available columns: {list(rows[0].keys())}")
        return

    # 5. حساب الإحصائيات وحفظها
    stats = calculate_stats(rows, column)
    save_to_json(stats)

if __name__ == "__main__":
    main()