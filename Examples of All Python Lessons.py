#==========================================================================
# هذه امثلة على جميع دروس بايثون الموجودة في الموقع الرسمي لبايثون
#==========================================================================

#يمكن استخدام بايثون للحسابات البسيطة
print(2+5)
print(2*3)
print(2/5)
print(8-5)
#النصوص
#يمكن معالجة السلاسل النصية بسهولة.
print('Hello' + ' ' + 'World')
# القوائم
#القوائم متعددة الاستخدامات ويمكنها تخزين عناصر متعددة
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')
print(fruits)

#عبارات if
x = 10
if x > 5:
    print("x أكبر من 5")

#عبارات for
for i in range(5):
    print(i)

#دالة range()
list(range(5))
# الناتج: [0, 1, 2, 3, 4]

#عبارات break و continue، وجمل else في الحلقات
for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#عبارات pass
#تستخدم كموضع لنقاط مستقبلية في الكود.
def func():
    pass

#عبارات match
#تم تقديم match في بايثون 3.10، وهي مشابهة لعبارات switch-case في لغات أخرى.
def http_error(status):
    match status:
        case 400:
            return "طلب سيء"
        case 404:
            return "غير موجود"
        case 418:
            return " إبريق شاي"
        case _:
            return "شيء آخر"

#تعريف الدوال
def greet(name):
    return f"مرحبا، {name}"

#قيم الوسائط الافتراضية
def greet(name, greeting="مرحبا"):
    return f"{greeting}، {name}"

#الوسائط الأساسية
def greet(name, greeting="مرحبا"):
    return f"{greeting}، {name}"
greet(greeting="أهلا", name="mohammed")

#الوسائط الموقفية أو الأساسية
def func(a, /, b, *, c):
    pass

#الوسائط الموقفيه فقط
def func(a, /, b):
    pass

#الوسائط الأساسية فقط
def func(*, c):
    pass

#قوائم الوسائط العشوائية
def greet(*names):
    for name in names:
        print(f"مرحبا، {name}")

#فك قوائم الوسائط
def add(a, b):
    return a + b
args = (5, 3)
add(*args)

#التعبيرات اللامبدية
add = lambda x, y: x + y
add(2, 3)

#سلاسل التوثيق
def func():
    """هذه سلسلة توثيق."""
    pass

#توضيحات الدوال
def greet(name: str) -> str:
    return f"مرحبا، {name}"

#الهياكل البيانية
#المزيد حول القوائم
# استخدام القوائم كأكوام
stack = []
stack.append(1)
stack.append(2)
stack.pop()
#استخدام القوائم كطوابير
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
#فهم القوائم المتداخلة
matrix = [[j for j in range(5)] for i in range(5)]

#عبارة del
a = [1, 2, 3]
del a[0]

#القوائم المرتبة (Tuples) والتسلسلات
t = (1, 2, 3)

#المجموعات
a_set = {1, 2, 3}

#القواميس
a_dict = {"one": 1, "two": 2}

#تقنيات التكرار
for k, v in a_dict.items():
    print(k, v)

#مقارنة التسلسلات والأنواع الأخرى
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # صحيح

#تنفيذ الوحدات كبرامج (Executing Modules as Scripts)
# افترض أن لديك وحدة باسم mymodule.py
# يحتوي الملف على الكود التالي:
def greet():
    print("Hello from mymodule!")

if __name__ == "__main__":
    greet()
# يمكنك تشغيله باستخدام:
#python -m mymodule

#دالة dir() (The dir() Function)
import math
print(dir(math))  # سيعرض جميع الأسماء المتاحة في وحدة math

#الحزم (Packages)
#استيراد * من الحزمة (Importing * From a Package)
from package_name import * # type: ignore

#الإدخال والإخراج (Input and Output)
# طلب إدخال اسم المستخدم
name = input("Please enter your name: ")
# طلب إدخال عمر المستخدم
age = input("Please enter your age: ")

# طباعة المعلومات المدخلة
print("Your name is:", name)
print("Your age is:", age)

#دالة format() (The String format() Method)
print("Hello, {}!".format(name))

#التنسيق القديم للسلاسل النصية (Old string formatting)
print("Hello, %s!" % name)

#دوال كائنات الملف (Methods of File Objects)
with open('example.txt', 'w') as f:
    f.write("Hello, file!")

#حفظ البيانات المهيكلة باستخدام json (Saving structured data with json)
import json
data = {"name": "John", "age": 30}
with open('data.json', 'w') as f:
    json.dump(data, f)

#الأخطاء والاستثناءات (Errors and Exceptions)
# معالجة الاستثناءات (Handling Exceptions)
# استخدام عبارات try وexcept لمعالجة الاستثناءات.
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# #رفع الاستثناءات (Raising Exceptions)
# استخدام العبارة raise لرفع استثناء مخصص.
raise ValueError("Invalid value")

#الاستثناءات المعرفة من قبل المستخدم (User-defined Exceptions)
class MyException(Exception):
    pass

#الفئات (Classes)
#بناء جملة تعريف الفئة (Class Definition Syntax)
class MyClass:
    def __init__(self, value):
        self.value = value

#كائنات الفئة (Class Objects)
instance = MyClass(10)

#كائنات الطريقة (Method Objects)
instance.value

# #الوراثة (Inheritance)
# نفترض أننا نريد إنشاء فئة تمثل الحيوانات (Animal) وفئة أخرى تمثل الكلاب (Dog) التي ترث من فئة الحيوانات. هنا كيف يمكنك القيام بذلك:
# تعريف فئة أساسية تمثل الحيوانات
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} makes a sound.")

# تعريف فئة الكلاب التي ترث من فئة الحيوانات
class Dog(Animal):
    def __init__(self, name, breed):
        # استدعاء الدالة المُنشِئة للفئة الأساسية
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

# إنشاء كائن من فئة الكلاب
my_dog = Dog(name="Buddy", breed="Golden Retriever")

# استخدام الكائن الجديد
print(f"My dog's name is {my_dog.name}, and it is a {my_dog.breed}.")
my_dog.speak()





# تعريف متغيرات
age = 25  # متغير لتخزين العمر
name = "mohammed"  # متغير لتخزين الاسم
height = 1.75  # متغير لتخزين الطول بالمتر

# طباعة المتغيرات
print("name:", name)
print("age:", age)
print("height:", height, "metr")

# تغيير قيمة المتغير
age = 26
print("the age after year:", age)



# تعريف ثوابت
PI = 3.14159  # ثابت لقيمة باي
GRAVITY = 9.81  # ثابت لتسارع الجاذبية بالأمتار لكل ثانية مربعة

# استخدام الثوابت
radius = 5
area = PI * (radius ** 2)  # حساب مساحة دائرة
print("circuit space:", area)

# محاولة تغيير قيمة ثابت (هذا غير مستحسن)
# PI = 3.14  # لا يُنصح بتغيير قيمة الثوابت

