# Основной модуль библиотеки pillow - Image
from PIL import Image


# Метод Image.open возвращает экземпляр класса ImageFile
im = Image.open("image.jpg")
# Атрибуты format, size, mode позволяют узнать данные о файле
print(im.format, im.size, im.mode)
# Метод crop возвращает фрагмент изображения, определенный с помощью кортежа из координат верхнего левого и нижнего правого углов
region = im.crop((0, 0, 250, 250))
print(region.size)
# Метод show выводит изображение на экран
region.show()
