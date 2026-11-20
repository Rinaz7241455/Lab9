# Лабораторная работа № 9. Вариант 8: «Сериализация»
# JSON/XML сериализация и десериализация объекта Employee (из ЛР № 7)
import json
import xml.etree.ElementTree as ET

class Employee:
    def __init__(self, full_name: str, position: str, salary: float, experience: int) -> None:
        self.full_name, self.position = full_name, position
        self.salary, self.experience = salary, experience

    def to_dict(self) -> dict:
        return {"full_name": self.full_name, "position": self.position,
                "salary": self.salary, "experience": self.experience}

    @classmethod
    def from_dict(cls, data: dict) -> "Employee":
        return cls(data["full_name"], data["position"], float(data["salary"]), int(data["experience"]))

def save_and_load_json(emp: Employee, path: str = "employee.json") -> Employee | None:
    """Сериализация и десериализация в JSON с обработкой >=3 исключений и finally."""
    f = None
    try:
        with open(path, "w", encoding="utf-8") as out_f:
            json.dump(emp.to_dict(), out_f, ensure_ascii=False, indent=2)
        f = open(path, "r", encoding="utf-8")
        return Employee.from_dict(json.load(f))
    except FileNotFoundError:
        print(f"Ошибка: файл '{path}' не найден.")
    except (json.JSONDecodeError, KeyError, ValueError) as err:
        print(f"Ошибка формата данных JSON: {err}")
    except PermissionError:
        print(f"Ошибка доступа к файлу '{path}'.")
    finally:
        if f and not f.closed:
            f.close()
    return None

def save_xml(emp: Employee, path: str = "employee.xml") -> None:
    """Экспорт объекта Employee в формат XML с безопасным закрытием потока."""
    root = ET.Element("Employee")
    for key, val in emp.to_dict().items():
        child = ET.SubElement(root, key)
        child.text = str(val)
    with open(path, "wb") as xml_f:
        ET.ElementTree(root).write(xml_f, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    emp = Employee("Иванов Алексей Андреевич", "Разработчик", 80000.0, 6)
    restored = save_and_load_json(emp)
    save_xml(emp)
    if restored:
        print(f"JSON восстановлен: {restored.full_name}, {restored.position}, {restored.salary:.2f} руб.")
        print("XML успешно сохранён в файл employee.xml")
