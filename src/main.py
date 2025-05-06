import openpyxl

def load_excel_data(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = [cell.value for cell in sheet['A'] if cell.value is not None]
    return data

def compare_data(existing_data, new_data):
    if new_data in existing_data:
        return False, len(existing_data)
    else:
        return True, len(existing_data)

def main():
    excel_path = '/data/data/com.termux/files/home/MyExcelCompareApp/data/data.xlsx'  # مسیر فایل اکسل
    existing_data = load_excel_data(excel_path)
    new_data = input("داده جدید را وارد کنید: ")
    is_new, count = compare_data(existing_data, new_data)
    if is_new:
        print(f"داده جدید است. تعداد داده‌های موجود: {count}")
    else:
        print("داده تکراری است.")

if __name__ == "__main__":
    main()
