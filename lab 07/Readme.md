## Декоратори
## Лабораторна №07
### Ціль: Ознайомитись з роботою декораторів, написату функцію для рахування часу роботи програми.


####Умови виконання:
 1. Передбачити, що декоратори можуть приймати аргументи.
 2. Продемонструвати виклики декораторів за допомогою звичайних викликів та нотації @. 
 3. Передбачити, що функції, які будуть декоровані приймають аргументи.
 4. Зробити описи Doc strings.
 5. Перевірити, що після декорування метадані початкової функції збережені.

####Алгоритм виконання першого завдання:

 - Введення початкового значення прогресії.
 - Введення кроку прогресії.
 - Введення елементу який потрібно знайти.
 - Реалізуємо функцію знаходження елементу ариф. прогресії.
 - Створення декоратору для відстежування часу початку та завершення виконання програми.
 - Створення декоратору для декількох запусків функції у разі її неуспішного виконання.
 - Створення декоратору, що буде додавати у змінну Registered усі продекоровані функції програми.
 - Прив'язка декораторів до потрібних функцій.

### Приклад роботи програми
```
Введіть початкове значення: 4949576
Введіть крок прогресії: 69484648
Введіть номер елементу прогресії який хочете знайти: 34568902
-----Арифметична прогресія-----
Значеня 34568902 елементу =  2402007922681424
Час виконання: 0:00:02.389900
Функція виконана правильно
Registered: ['arithmetic_progression', 'my_func']


   ```