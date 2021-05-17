## Файли. Виключення. Менеджери контексту.
## Лабораторна №08
### Ціль: Ознайомитись з принципом роботи з файлами використовуючи конструкцію try/catch використовуючи менеджери контексту.

Для виконання першого завдання використовується наступний алгоритм:
 - Відкриття файлу з певним текстом для читання
 - Створення нового файлу та відкриття його для запису
 - Считування построково файл 
 - За допомогою методу *split()* виділяємо кожне слово як конкретний елементу
 - Обмін місцями перше та останнє слово в рядку
 - Запис отриманого рядка в файл 
 - Якщо при відкритті або при записі в файл виникають помилки,
   то вони оброблюються в конструкції  try/catch після чтого 
   програма завуршується коректно
   
Для виконання першого завдання використовується наступний алгоритм:
 - Відкриття файлу з певним текстом для читання
 - Створення нового файлу та відкриття його для запису
 - Вміст першого файлу переписується в другий
 - Считування построково другий файл
 - Перевірка кожного зчитаного рядку чи не закінчується він "?"
 - Якщо такий рядок знаходиться то він переписуєтьсяв зворотньому порядку літер
 - Якщо рядка не знайдено то програма завершується

### Приклад виконання роботи першої програми
###### Вміст файлу для роботи з текстом
```
First job offer
Second job offer
Some kind of text to work with
A sentence with? a question mark
Some kind of text to work with
Some kind of text to work with?
Rerrere
```
###### Вміст файлу після закінчення роботи першої програми
```
offer job First
offer job Second
with kind of text to work Some
mark sentence with? a question A
with kind of text to work Some
with? kind of text to work Some
Rerrere
```
###### Вміст файлу після закінчення роботи другої програми
```
First job offer
Second job offer
Some kind of text to work with
A sentence with? a question mark
Some kind of text to work with
?htiw krow ot txet fo dnik emoS
Rerrere
```