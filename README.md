HEAD
# MyExcelCompareApp
برنامه پایتون برای مقایسه داده‌های جدید با داده‌های موجود در فایل اکسل.

# MyExcelCompareApp
edcbcbb7f07347045595b970f2ae2c16526aca89
## نمونه کد پایتون برای مقایسه دو فایل اکسل

```python
import pandas as pd

# فرض: دو فایل اکسل با نام‌های data1.xlsx و data2.xlsx در پوشه data قرار دارند
df1 = pd.read_excel('data/data1.xlsx')
df2 = pd.read_excel('data/data2.xlsx')
diff = df1.compare(df2)
print(diff)
