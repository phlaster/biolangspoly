# `rec.py`: Обратная комплементарная последовательность
## Входные данные
Строка ДНК $dna$ длиной не менее одного символа и не более 1000.

## Выходные данные
Обратная комплементарная последовательность $dna^c$.

## Пример
**Входные данные:**
```txt
CAGT
```
**Выходные данные:**
```txt
ACTG
```

# `trn.py`: Трансляция РНК
## Входные данные
Строка РНК $rna$ состоящая из целового числа кодонов (2-3000), оканчивающаяся стоп-кодоном.

## Выходные данные
Последовательность белков, полученная кодированием кодонов в соответствии с таблицей

## Пример
**Входные данные:**
```txt
CGUAUCGGUCACACCGCUAACAGCUGGGAAAGAUAG
```
**Выходные данные:**
```txt
RIGHTANSWER
```

# `rtt.py`: Соотношение транзиций к трансверсиям
## Входные данные
Две строки ДНК $s1$ и $s2$ одинаковой длины не более 1000 символов. В исходных данных присутствует хотя бы одна трансверсия.

## Выходные данные
Соотношение транзиций к трансверсиям $R(s1, s2)$.

## Пример
**Входные данные:**
```txt
ACGATCGCATGTCATCAACGTTTACGGCATGCAGCTAGCGATCGATTTCGCTATGCTTAGCATGACTCGGACTACGACTACGACT
GCTAGTCACCACAGTCGCGATCGACGATCGGATCTCGACTTCGACTACTAGCGCGATTCGAAATCAGCTCGACTATTCGGGTATC
```
**Выходные данные:**
```txt
0.7368421052631579
```

# `fis.py`: Поиск подстрок
## Входные данные
Две строки $s$ и $t$, каждая длиной не более 1000 символов.

## Выходные данные
Все индексы начала подстрок $t$ в строке $s$. Индексы выводятся через пробел.

## Пример
**Входные данные:**
```txt
AGCGCGCATATGCGCGAAT
GCGC
```
**Выходные данные:**
```txt
1 3 11
```

**Входные данные:**
```txt
AGCGCGCATATGCGCGAAT
ACGT
```
**Выходные данные:**
```txt
none
```


# `mss.py`: Поиск наибольшей подстроки
Нужно найти наибольшую общую подстроку (не подпоследовательность) строк в FASTA-формате, записанных в файле.

Если общей подпоследовательности нет, надо вывести `none`.

Использовать стандартные потоки ввода и вывода.

Можно использовать только стандартные библиотеки python.
## Входные данные
Название файла, содержащего данные, записанные в FASTA-формате. Например "test1.txt":

## Выходные данные
Наибольшая общая подстрока строк, указанных в файле
## Пример
**Входные данные:**
```txt
>string_1
ACGTACGT
>string_2
GTACGTCA
>string_3
ACG
```
**Выходные данные:**
>ACG


# `pwe.py`: Вычисление белковых весов
## Входные данные
Белковая строка $P$ длиной не более 1000 символов.

## Выходные данные
Суммарный вес строки $P$ ([моноизотопная масса белка](http://www2.riken.jp/BiomolChar/Aminoacidmolecularmasses.htm)).

## Пример
**Входные данные:**
>PRQTEINSTRING

**Выходные данные:**
>1466.7589799999998


# `dat.py`: Работа с данными
В каталоге содержится директория data, в которой хранятся данные по исследованиям. Нужно пройтись рекурсивно по директориям и считать все файлы, которые оканчиваются на .txt. Все файлы, в которых больше 50 записей - пропустить. В оставшихся файлах, если последовательность состоит из повторяющегося символа - пропустить такое исследование. По считанным исследованиям нужно посчитать и вывести:

1. Время максимальной загрузки каждой из машин.
2. Имя самого "трудолюбимого" сотрудника с указанием потраченного времени.

Пример каталога можно посмотреть тут: https://drive.google.com/file/d/1Vm2NgqIJWlvrXAOPL03s034HjdLUtOhv/view?usp=share_link

Пример исследования можно посмотреть тут: https://drive.google.com/file/d/16NHDzE4FxxIs2raIlFWUIRLM7rFVKMsJ/view?usp=share_link

Использовать стандартные потоки ввода и вывода. Можно использовать только стандартные библиотеки python.
## Входные данные
Название папки, содержащей данные по исследованиям.

## Выходные данные
Под временем максимальной загрузки машины подразумевается час, в который чаще всего запускается валидное исследование.

Самым трудолюбивым сотрудником считается тот, который залогировал больше всего исследований. Потраченным временем считается суммарное кол-во валидных исследований.

## Пример
**Входные данные:**
```txt
/usr/local/share/ejudge-problems-files/data-analisys/1var
```

**Выходные данные:**
```txt
IDSSA1:10
IDSSA2:10
IDSSA3:17
IDSSA4:10
IDSSA5:13
Petr Levdanskiy:29
```


# `ivp.py`: Решение задачи Коши (Вариант 1)
$$
...
$$


# `fco.py`: Сервис кодирования-декодирования файла (Вариант 4)
$$
...
$$