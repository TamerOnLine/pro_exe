import subprocess
import sys
import os
import shutil
from tkinter import Tk, filedialog

def ask_for_file():
    Tk().withdraw()  # إخفاء نافذة Tk
    return filedialog.askopenfilename(
        title="Select Python file to convert",
        filetypes=[("Python files", "*.py")]
    )

def clean_up():
    print("🧹 Cleaning up temporary files...")
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("__pycache__", ignore_errors=True)
    for ext in [".spec", ".log"]:
        for f in os.listdir():
            if f.endswith(ext):
                try:
                    os.remove(f)
                except Exception as e:
                    print(f"Couldn't delete {f}: {e}")

def main():
    # 1️⃣ تحديد الملف: من السطر - أو نافذة اختيار
    if len(sys.argv) >= 2:
        full_path = os.path.abspath(sys.argv[1])
    else:
        full_path = ask_for_file()

    if not full_path or not os.path.isfile(full_path):
        print("❌ No valid file selected.")
        return

    filename = os.path.splitext(os.path.basename(full_path))[0]
    print(f"🔄 Converting '{filename}.py' to .exe...")

    # 2️⃣ تشغيل PyInstaller مع اسم ديناميكي
    result = subprocess.run([
        "pyinstaller",
        "--onefile",
        f"--name={filename}",
        full_path
    ])

    if result.returncode != 0:
        print("❌ Conversion failed.")
        return

    # 3️⃣ تنظيف
    clean_up()

    print(f"✅ Done! Created: dist\\{filename}.exe")

if __name__ == "__main__":
    main()
