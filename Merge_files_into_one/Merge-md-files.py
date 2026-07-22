import os
import json
import argparse
from datetime import datetime

def is_git_related(path):
    """تتحقق إذا كان المسار متعلق بـ Git (مجلد .git أو ملفات .git*)"""
    basename = os.path.basename(path)
    # تجاهل مجلد .git بالكامل، وأي ملف يبدأ بـ .git (زي .gitignore)
    return basename == '.git' or basename.startswith('.git')

def read_file_content(file_path):
    """تقرأ محتوى الملف وتحدد نوعه، وتتعامل مع الملفات الثنائية (Binary)"""
    ext = os.path.splitext(file_path)[1].lower()
    
    # ------ معالجة ملفات Jupyter (.ipynb) ------
    if ext == '.ipynb':
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            code_cells = []
            markdown_cells = []
            
            for cell in data.get('cells', []):
                cell_type = cell.get('cell_type')
                source = ''.join(cell.get('source', []))
                if cell_type == 'code':
                    code_cells.append(source)
                elif cell_type == 'markdown':
                    markdown_cells.append(source)
            
            output = "### 📓 Jupyter Notebook\n"
            if code_cells:
                output += "**كود (Code Cells):**\n```python\n" + "\n\n".join(code_cells) + "\n```\n"
            if markdown_cells:
                output += "**نص (Markdown Cells):**\n```markdown\n" + "\n\n".join(markdown_cells) + "\n```\n"
            if not code_cells and not markdown_cells:
                output += "```json\n" + json.dumps(data, indent=2, ensure_ascii=False) + "\n```\n"
            
            return output
        
        except Exception as e:
            return f"📓 Jupyter Notebook (حدث خطأ في القراءة): {str(e)}\n```\n" + open(file_path, 'r', encoding='utf-8', errors='ignore').read() + "\n```\n"
    
    # ------ معالجة الملفات النصية العادية (py, md, txt, json, etc.) ------
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # محاولة بترميز آخر
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
        except:
            # ملف ثنائي (صور، PDF، إلخ)
            size = os.path.getsize(file_path)
            return f"⚠️ **ملف ثنائي (Binary)** - حجمه: {size} بايت (لا يمكن عرض المحتوى النصي)."
    
    # تحديد لغة التظليل (Syntax Highlighting) حسب الامتداد
    lang_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.html': 'html',
        '.css': 'css',
        '.json': 'json',
        '.xml': 'xml',
        '.yml': 'yaml',
        '.yaml': 'yaml',
        '.sh': 'bash',
        '.sql': 'sql',
        '.md': 'markdown',
        '.txt': 'text',
    }
    
    lang = lang_map.get(ext, '')
    return f"```{lang}\n{content}\n```\n"

def generate_report(root_dir, output_file):
    """تجول في المجلدات وتكتب كل الملفات في ملف Markdown واحد (مع تخطي Git)"""
    root_dir = os.path.abspath(root_dir)
    output_file = os.path.abspath(output_file)
    
    with open(output_file, 'w', encoding='utf-8') as out_f:
        # رأس الملف
        out_f.write(f"# 📁 تقرير تجميع الملفات\n")
        out_f.write(f"> تم إنشاؤه في: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        out_f.write(f"> المجلد الجذري: `{root_dir}`\n\n")
        out_f.write("---\n\n")
        
        count = 0
        # المشي عبر المجلدات
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # 🔥 أهم تعديل: نزيل أي مجلد خاص بـ Git من قائمة التجوال
            # بنستخدم dirnames[:] عشان نعدل القائمة الأصلية ونمنع os.walk من الدخول فيها
            dirnames[:] = [d for d in dirnames if not is_git_related(os.path.join(dirpath, d))]
            
            # فلترة الملفات: نستبعد أي ملف يبدأ بـ .git (زي .gitignore, .gitattributes)
            # كمان بنستبعد ملف الإخراج نفسه لو صادفنا اسمه
            filenames_filtered = [
                f for f in filenames 
                if not is_git_related(os.path.join(dirpath, f)) 
                and os.path.join(dirpath, f) != output_file
            ]
            
            for filename in filenames_filtered:
                file_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(file_path, root_dir)
                
                count += 1
                ext = os.path.splitext(filename)[1].lower()
                
                # كتابة رأس الملف في التقرير
                out_f.write(f"## 📄 الملف: `{rel_path}`\n")
                out_f.write(f"- **الامتداد**: `{ext if ext else '(بدون امتداد)'}`\n")
                out_f.write(f"- **المسار الكامل**: `{file_path}`\n\n")
                
                # قراءة المحتوى وكتابته
                content_block = read_file_content(file_path)
                out_f.write(content_block)
                out_f.write("\n---\n\n")  # فاصل بين الملفات
        
        out_f.write(f"\n✅ **الإجمالي**: تم تجميع {count} ملف بنجاح (تم تخطي مجلدات وملفات Git).\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='تجميع كل ملفات المجلد في ملف Markdown واحد (مع تخطي Git)')
    parser.add_argument('--root', default='.', help='المجلد الجذري للبحث (افتراضي: المجلد الحالي)')
    parser.add_argument('--output', default='combined_report.md', help='اسم ملف الإخراج (افتراضي: combined_report.md)')
    
    args = parser.parse_args()
    
    generate_report(args.root, args.output)
    print(f"✅ تم الإنشاء بنجاح! افحص الملف: {args.output}")