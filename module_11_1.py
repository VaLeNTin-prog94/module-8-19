import matplotlib.pyplot as plt
import numpy as np
import requests

a = np.array([1, 2, 3, 4, 5, 6], )
print(a.ndim)  # Число измерений массива содержится в ndim атрибуте.
print(a.shape)  # количество неотрицательных элементов в виде кортежа
print(a.size)  # Фиксированное общее количество элементов в массиве

a = np.empty(3)  # создаем случайными элементами
print(a)
a = np.arange(50)  # Вы можете создать массив с диапазоном элементов:
print(a)

print(a[a > 25])  # распечатка элементов больше 25
print(len(a))
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  #
plt.show()
#рисование условно по каоординатам "х" и "у"
r = requests.get('https://api.github.com/events') #получаем веб страницу
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
#Requests позволяет вам предоставлять эти аргументы в виде словаря строк, используя
# params аргумент ключевого слова. Например, если вы хотите передать key1=value1и key2=value2 в
# httpbin.org/get, вы бы использовали следующий код:
print(r.url)#распечатав URL-адрес:

r = requests.get('https://api.github.com/events')
print(r.text)#Cодержимое ответа сервера
