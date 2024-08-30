\c - показывает к какой бд мы подключены и через какого юзера
\c <name_of_db> - подключается к указанной бд
\l - список всех бд
\du - показывает список всех юзеров с их правами
\dt - показывает список таблиц в текущей бд
\d+ - показывает более подробную информацию о таблицах
\d+ <name_of_table> - показывает более подробную информацию о указанной таблице

psql - команда для входа в оболочку postgresql
\q - выход из СУБД (из оболочки psql)

СОЗДАНИЕ ТАБЛИЦ И БД:
CREATE DATABASE name_of_db;
DROP DATABASE name_of_db;

ТИПЫ ДАННЫХ POSTGRESQL

Числовые типы данных:
1) smallint - хранит маленькие числа в диапозоне от -32767 до +32767, в памяти занимает 2 байта
2) integer - хранит числа в более широком диапозоне, занимает 4 байта
3) bigint - хранит числа в самом большом диапозоне -9223372036854775808 до +9223372036854775808 занимает 8 байт
4) serial - числовой тип данных у которого есть автоинкремент

Строковые типы данных:
1) char(character(n)) - используется для строк, имеет фиксированную длину, обязательно нужно ограничение по символам
2) character varying(n) (VARCHAR) - такой же тип данных для строк, но имеет переменную длину
3) text - предоставляет текст произвольной длины

Типы данных для работы со временем и датой
1) date - предоставляет дату от 4713г. до н. э. до 5874897 г н. э. занимает 4 байта в памяти
2) time - хранит время с точностью до 1 микросекунды без указания часового пояса. Принимает значения от 00.00.00 до 24.00.00, занимает 8 байт

Булевые значения:
boolean - хранит одно из двух значений: true или false
Вместо true можно записать следующие значения: TRUE, 't', 'true', 'y', 'yes', 'on', '1'
Вместо false можно записать следующие значения: FALSE, 'f', '0', 'false', 'no', 'off'

json - хранит данные json в текстовом виде

КОМАНДА ДЛЯ СОЗДАНИЯ ТАБЛИЦЫ:
CREATE TABLE name_of_table (
    column1 data_type1,
    column2 data_type2
    ...
);-- создает таблицу с полями

DROP TABLE name_of_table; -- команда для удаления таблицы

КОМАНДА ДЛЯ ВЫВОДА ДАННЫХ С ТАБЛИЦЫ:
SELECT * FROM name_of_table; -- выводит все поля и данные с таблицы
SELECT id, name FROM name_of_table; --выведет только поля id, first_name из таблицы

КОМАНДА ДЛЯ ЗАПОЛНЕНИЯ ТАБЛИЦ:
INSERT INTO name_of_table
(first_name, last_name, phone_number, username) 
VALUES
('nikita', 'grebnev', '+996707531295', 'nick');


КОМАНДА ДЛЯ УДАЛЕНИЯ ЗАПИСЕЙ ИЗ ТАБЛИЦЫ:
DELETE FROM name_of_table; -- удаляет все записи из таблицы

ОБНОВЛЕНИЕ ЗАПИСЕЙ В ТАБЛИЦЕ:
UPDATE name_of_table SET column = new_val; -- Обновляет все записи в таблице

UPDATE name_of_table SET column = new_val WHERE id < 10; -- Обновление нескольких записей, id которых меньше 10

УСЛОВИЯ:
DELETE FROM name_of_table WHERE id=4;
DELETE FROM name_of_table WHERE name='nikita';

SELECT * FROM name_of_table WHERE last_name like '%grebnev%'; -- Выбирает все записи у которых в поле last_name есть название содержащее 'grebnev'
-- like - чувствительный к регистру (Grebnev - не пройдет)


SELECT * FROM name_of_table WHERE last_name ilike '%grebnev%'; -- ilike не чувствителен к регистру


SELECT * FROM name_of_table ORDER BY column1; -- сортировка по определенному полю (по возврастанию ASC)

SELECT * FROM name_of_table ORDER BY column1 DESC; -- сортировка по опеределенному полю, по убыванию (DESC)

ASC - ascending - возврастание
DESC - descending - убывание

SELECT * FROM name_of_table LIMIT 10; -- выводит первые 10 записей

SELECT * FROM name_of_table OFFSET 5; -- пропускает первые 5 записей в таблице, и выводит все остальные

SELECT * FROM name_of_table LIMIT 5 OFFSET 5; -- пропускает 5 записей, выводит следующие 5 записей


СВЯЗИ:
1) PRIMARY KEY (pk) - первичный ключ, ограничение которое накладывается на поле, которое будет использовано в связях
2) FOREIGN KEY (fk) - внешний ключ, ограничение, которое накладывается на поле, которое ссылается на pk в другой таблице

CREATE TABLE author(
id SERIAL PRIMARY KEY,
name VARCHAR(50),
last_name VARCHAR(50)
);


CREATE TABLE book(
id SERIAL PRIMARY KEY,
title VARCHAR(100),
published DATE,
author_id INT,

CONSTRAINT fk_book_author FOREIGN KEY (author_id) 
REFERENCES author (id));


ONE-TO-ONE -- Один к одному
1) один человек - один ID
2) один автор - одна автобиография

ПРИМЕР КОДА:
CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

CREATE TABLE autobiography (
    id SERIAL PRIMARY KEY,
    body TEXT,
    created_at DATE,
    author_id INT UNIQUE,

    CONSTRAINT fk_author_bio
    FOREIGN KEY (author_id) REFERENCES author (id)
);


ONE-TO-MANY -- Один ко многим

CREATE TABLE curator (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    language VARCHAR(2),
    curator_id INT,

    CONSTRAINT fk_student_curator
    FOREIGN KEY (curator_id) REFERENCES curator (id)
);

MANY-TO-MANY -- многие ко многим

CREATE TABLE developer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    experience INT
);

CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    tz TEXT,
    start DATE,
    finish DATE
);

CREATE TABLE dev_proj (
    dev_id INT,
    proj_id INT,

    CONSTRAINT fk_dev FOREIGN KEY (dev_id) REFERENCES developer (id),
    CONSTRAINT fk_proj FOREIGN KEY (proj_id) REFERENCES project (id)
);


--JOINS--

JOIN - инструкция, которая позволяет в запросах SELECT брать данные из нескольких таблиц

INNER JOIN (JOIN) - достаются только те записи, у которых есть связь

FULL JOIN - достаются все записи с обеих таблиц

LEFT JOIN - достает все записи с левой таблицы, и с правой таблицы у которых есть связь с левой таблицей

RIGHT JOIN - достает все записи с правой таблицы, и с левой таблицы у которых есть связь с правой таблицей

'левая' таблица - та, которая написана до join'a a 'правая' таблица - та, которая написана после join'a 


----ПРАКТИКА----
-BLOGG
CREATE TABLE bloger(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE post(
    id SERIAL PRIMARY KEY,
    bloger_id INT,
    body TEXT,
    created_at DATE,

    CONSTRAINT fk_post_blogger FOREIGN KEY (blogger_id) REFENRECES bloger (id)
);
--- заполнение таблиц
INSERT INTO bloger (name) VALUES
('nikita'),
('Isa'),
('Emir'),
('Torokul');

INSERT INTO post (blogger_id, body, created_at) VALUES 
(1, 'some body', '2024-08-12'),
(1, 'some body', '2021-09-23'),
(1, 'some body', '2001-01-01');

INSERT INTO post (blogger_id, body, created_at) VALUES 
(2, 'some body', '2002-08-17'),
(2, 'some body', '2025-12-12'),
(2, 'some body', '2024-10-12');

INSERT INTO post (blogger_id,body,created_at) VALUES 
(3, 'some body', '2006-11-27'),
(3, 'some body', '2012-09-10'),
(3, 'some body', '2015-01-06');

INSERT INTO post (blogger_id,body,created_at) VALUES 
(4, 'some body', '2023-09-09'),
(4, 'some body', '2022-05-23'),
(4, 'some body', '2019-04-12');


---SHOP---

1) команда psql -- зайдет в оболочку postgres
2) CREATE DATABASE shop; -- создание бд
3) \c shop --подключение к бд 

CREATE TABLE customer(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE product(
    id SERIAL PRIMARY KEY,
    tittle VARCHAR(50),
    price DECIMAL
);

CREATE TABLE cart(
    id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,

    CONSTRAINT cart_customer FOREIGN KEY (customer_id) REFERENCES customer (id),
    CONSTRAINT cart_product FOREIGN KEY (product_id) REFERENCES product (id)
);

--заполнение таблиц--

INSERT INTO customer (name) VALUES
('customer1'),
('customer2'),
('customer3');


INSERT INTO product (tittle, price) VALUES 
('milk', 2.24),
('bread', 3),
('eggs', 3.33),
('sugar', 5),
('salt', '1');


INSERT INTO cart(customer_id,product_id) VALUES
(1, 3), (2, 1), (3, 5), 
(1, 3), (2, 1), (3, 5);


--АГРЕГАТНЫЕ ФУНКЦИИ--
SUM - функция, считает сумму всех записей в сгруппированном поле

SELECT customer.name, SUM(product.price) AS total_price
FROM product JOIN cart ON product.id = cart.product_id
JOIN customer ON customer.id = cart.customer_id
GROUP BY (customer.name);

  name    | total_price 
-----------+-------------
 customer2 |        4.48
 customer1 |        6.66
 customer3 |           2
(3 rows)



ARRAY_AGG - обьединяет записи с группировоного поля массив
--- пример из blog

SELECT blogger.name, ARRAY_AGG(post.body) AS posts
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);

  name   |                 posts                 
---------+---------------------------------------
 Torokul | {"some body","some body","some body"}
 nikita  | {"some body","some body","some body"}
 Isa     | {"some body","some body","some body"}
 Emir    | {"some body","some body","some body"}

MIN, MAX - высчитывают минимальное и максимальное значение среди записей с группировонном поле

SELECT blogger.name, MIN(post.created_at) AS first, MAX(post.created_at) AS last FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);
  name   |   first    |    last    
---------+------------+------------
 Torokul | 2019-04-12 | 2023-09-09
 nikita  | 2001-01-01 | 2024-08-12
 Isa     | 2002-08-17 | 2025-12-12
 Emir    | 2006-11-27 | 2015-01-06



COUNT - считает количество записей в сгруппированном поле

SELECT blogger.name, COUNT(post.id) AS posts_count
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);
 name   | posts_count 
---------+-------------
 Torokul |           3
 nikita  |           3
 Isa     |           3
 Emir    |           3

---ИЗМЕНЕНИЕ ТАБЛИЦ---

ALTER TABLE name_of_table ADD COLUMN col_name type constrint; -- добавляет новую колонну в таблицу 
--ПРИМЕР--
ALTER TABLE blogger ADD CLOUMN age INT;

ALTER TABLE name_of_table DROP COLUMN col_name;
--Удаляет колонну из таблицы
--ПРИМЕР--
ALTER TABLE blogger DROP COLUMN age;


ALTER TABLE name_of_table ADD CONSTRAINT constr_name constraint;
-- добавление ограничение на поле