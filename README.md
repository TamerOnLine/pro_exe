# 🛠️ pro_exe - Python to EXE Converter

**pro_exe** is a simple, lightweight tool that allows you to convert any Python `.py` script into a standalone Windows `.exe` executable using [PyInstaller](https://www.pyinstaller.org/).  
It supports drag & drop, command-line arguments, or interactive file selection via a GUI.

---

## 🚀 Features

- ✅ Converts any `.py` file into a `.exe` with the same name
- 🖱️ Supports drag & drop
- 📂 GUI file selection if no arguments are provided
- 🧹 Auto-cleanup of `build/`, `__pycache__/`, `.spec`, and `.log` files
- 📦 Uses `PyInstaller` under the hood

---

## 🔧 Requirements

- Python 3.x
- `pyinstaller` (installed via `pip`)

Install requirements:

```bash
pip install -r requirements.txt
```

---

## 📦 Usage

### ➤ Method 1: Run from terminal

```bash
python myapp.py your_script.py
```

### ➤ Method 2: Run without arguments (GUI file picker will open)

```bash
python myapp.py
```

### ➤ Method 3: Drag & Drop

Drag any `.py` file onto `myapp.py` to convert it to `.exe`.

---

## 📁 Output

The resulting `.exe` file will be available in the `dist/` directory:

```
dist/
└── your_script.exe
```

---

## ⚖ License

This project is licensed under the **Apache License 2.0** – see the [LICENSE](LICENSE) file for details.
