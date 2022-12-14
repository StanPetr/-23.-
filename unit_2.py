''' 23.2. Локатор ID

Первый локатор, который применяется для тестирования, — это указание на элемент по ID.
Определение элемента по id — самый точный и надежный способ идентификации, потому что по спецификации HTML значение
каждого id должно быть уникальным в пределах документа.

В DevTools браузера на вкладке Console существует встроенный метод для обращения к элементу по id с помощью команды
document.getElementById("значение id").

Плюсы и минусы работы с локатором ID

Плюсы обращения по локатору ID:
    Локатор легко прочесть и понять.
    Путь к элементу никогда не зависит от его положения в DOM-дереве.
    Поддерживается в самых древних браузерах.

Недостатки работы с локатором ID:
    Не у каждого элемента страницы есть ID, более того, есть страницы, на которых может вообще не быть элементов с ID.
    Изредка ID не уникален на странице (такого быть не должно, но иногда случается).




'''