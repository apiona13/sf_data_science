# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных
....
  
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  

random_predict: Первая версия алгоритма угадывает число используя random, не принимая во внимание дополнительных условий

game_core_v2: Вторая версия алгоритма угадывает число и использует условия больше или меньше, для сокращения диапозона препологаемых чисел

game_core_v3: Третья версия алгоритма угадывает число и использует услвоия больше или меньше, однако в отличие от второй версии, сужает диапозон сильнее

Функции принимают загаданное число и возвращают затраченное количество попыток

В дополнение добавлена функция, которая вычисляет среднее количество затраченных попыток на 1000 угадываний для сравнения результатов

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  

random_predict: Этот алгоритм угадывает число в среднем за 99 попыток. Это означает, что он неэффективен и требует большого количества попыток для угадывания числа. Этот алгоритм просто выбирает случайные числа и проверяет, совпадает ли выбранное число с искомым.

game_core_v2: Этот алгоритм угадывает число в среднем за 33 попытки. В сравнении с random_predict, это уже лучше, но все еще довольно медленно. Этот алгоритм использует допольнительные условия в подходе, чем простое случайное угадывание.

game_core_v3: Этот алгоритм является наиболее эффективным из представленных. Он угадывает число в среднем за 11 попыток, что значительно быстрее, чем предыдущие два. Этот алгоритм использует более сложные условия, чтобы более точно и быстро угадывать число.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  

 game_core_v3 является предпочтительным вариантом из представленных, так как он достигает цели с наименьшим количеством попыток, что повышает эффективность и скорость выполнения задачи.

:arrow_up:[к оглавлению](.README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами