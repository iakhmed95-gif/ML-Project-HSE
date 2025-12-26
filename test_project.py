#!/usr/bin/env python
import os
import json

print("🧪 БЫСТРЫЙ ТЕСТ ПРОЕКТА")
print("=" * 30)

# 1. Проверка файлов
files_ok = all(os.path.exists(f) for f in ["ml_project_hse_improved.ipynb", "README.md"])
check_mark = "✅" if files_ok else "❌"
print(f"📁 Файлы: {check_mark}")

# 2. Проверка датасета
dataset_ok = os.path.exists("Telco-Customer-Churn.csv")
check_mark = "✅" if dataset_ok else "❌"
print(f"📊 Датасет: {check_mark}")

# 3. Проверка структуры ноутбука
if os.path.exists("ml_project_hse_improved.ipynb"):
    with open("ml_project_hse_improved.ipynb", "r") as f:
        data = json.load(f)
    cells_ok = len(data["cells"]) >= 25
    check_mark = "✅" if cells_ok else "❌"
    print(f"📋 Ячейки: {check_mark} ({len(data['cells'])})")
else:
    print("📋 Ячейки: ❌")

all_ok = files_ok and dataset_ok and cells_ok
status = "ГОТОВ К ЗАПУСКУ" if all_ok else "НУЖНЫ ИСПРАВЛЕНИЯ"
print(f"\n🎯 СТАТУС: {status}")

if all_ok:
    print("\n🚀 Для запуска:")
    print("jupyter notebook ml_project_hse_improved.ipynb")
else:
    print("\n🔧 Исправьте проблемы выше")
