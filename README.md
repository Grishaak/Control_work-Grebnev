# Control_work-Grebnev
>1. В терминале ubuntu:22.04 в собственной папке прописал
cat > "имя файла", для создания файла, первый Домашние животные - заполнив данный
файл животными: хомяки, собаки, кошки, второй Вьючные животные -
лошади, ослы, верблюды. Далее при помощи команды cat Domestic_pet.txt PetHorse_pet.txt >> All_animals.txt
создадим новый файл где будут все животные. 
>2. При помощи команды
mkdir control_work_db создадим директорию для файла и переместим ее туда
при помощи команды mv 'имя файла' ./control_work_db
>3. Для подключения репозитория mysql необходимо скачать файл дял последующей
дозагрузки от dpkg. Вот список команд для подключения
- 1678  apt-get install mysql-server
- 1679  apt-get remove mysql-server
- 1680  apt-get autoremove
- 1699  cp mysql-apt-config_0.8.29-1_all.deb ../mysql-apt-config_0.8.29-1_all.deb
- 1704  dpkg -i mysql-apt-config_0.8.29-1_all.deb
- 1705  mysql
- 1706  sudo apt-get update
- 1707  systemctl status mysql
- 1708  sudo mysql
- 1709  mysql -p
- 1710  sudo apt-get upgrade
- 1712  dpkg -i mysql-apt-config_0.8.29-1_all.deb
- 1713  sudo apt-get upgrade
- 1714  sudo apt-get update
- 1715  systemctl status mysql
- 1718  sudo apt-get install mysql-server
- 1719  systemctl status mysql
- 1720  apt-get update
- 1721  mysql -p root
- 1722  mysql -p -u root
> 4. Здесь mysql-apt-config - сам файл загрузки необходимой версии
mysql. Для начала удаляем все предыдущие версии, а после обновляемся
до последней версии и чистим ненужные репозитории.
Проверяем сетевой статус через systemctl 
> 5. История команды в папке screens.
> 6. Диаграмма в папке misc.
> 7. : 10 Пункты выполненые в виде скринов, так как некоторые из них некорректно составлены.
Вот пример одной таблицы котороая была создана:
- CREATE TABLE `friends_of_human`.`Horse_table` (
	`id_animal` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `name` VARCHAR(20) NOT NULL,
    `birth_date` DATE NOT NULL);

- INSERT INTO `friends_of_human`.`Horse_table` (`name`, `birth_date`)
- VALUES ('Боря', 20140310),
- ('Вася', 20130421),
- ('Миша', 20200107),
- ('Алёша', 20181014),
- ('Ваня', 20101103),
- ('Мирослав', 20200724),
- ('Мурка', 20220313),
- ('Ярик', 20090909);
> 11. Для создания таблицы была использована такая команда:
- CREATE TABLE all_young_animals as (
- SELECT *,  MONTH(current_date() - birth_date) as month, YEAR(current_date() - birth_date) - 2000 as age FROM (
- SELECT * FROM Donkey_table
- Union SELECT * from Horse_table
- Union SELECT * from Dog_table
- Union SELECT * from Cat_table
- Union SELECT * from Hamster_table) new_table
- where YEAR(current_date() - birth_date) - 2000  < 3 and YEAR(current_date() - birth_date) - 2000  > 1);
> 11. Все скрины с примером в папке screens.mysql
> 12. Такой же как пункт 11 только без дополнительных условий.
Также во время создания таблиц использовались одинаковые id для
разных таблиц, из-за чего может показаться что индесы повторяются.
По хорошему индексы прописывать с условиям какие уже есть, для
создания новых, ибо с join могут возникнуть проблемы.
> 13. Был создан абстрактный класс Animal как в диаграмме.
> 14. Весь код с консольной программой можно увидеть в view controller module.
- Был реализован Класс конструктора через который можно создавать разных животных, удалять
их, добавлять и удалять команды, а также сохранять данные. Не удалось релизовать связь с
базой данных, но на деле это возможно если связаться с локалхостом через рута и пароль до базы данных.
