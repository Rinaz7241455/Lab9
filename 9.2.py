# Контрольный пример (Фотография 2)
# Быстрая проверка JSON/XML сериализации объекта Employee
import json
import xml.etree.ElementTree as ET

emp_data = {
    "full_name": "Иванов Алексей Андреевич",
    "position": "Разработчик",
    "salary": 80000.0,
    "experience": 6,
}

with open("employee.json", "w", encoding="utf-8") as f:
    json.dump(emp_data, f, ensure_ascii=False, indent=2)

with open("employee.json", "r", encoding="utf-8") as f:
    restored = json.load(f)

root = ET.Element("Employee")
for k, v in emp_data.items():
    ET.SubElement(root, k).text = str(v)
ET.ElementTree(root).write("employee.xml", encoding="utf-8", xml_declaration=True)

print(f"JSON восстановлен: {restored['full_name']}, {restored['position']}, {restored['salary']:.2f} руб.")
print("XML успешно сохранён в файл employee.xml")
print(json.dumps(restored, ensure_ascii=False, indent=2))
