# JSON_debugging

### Скрипт, позволяющий проверить JSON-данные по JSON-схеме.

## Установка на локальном компьютере
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Запуск проекта (на примере Linux)

Перед тем, как начать: если вы не пользуетесь `Python 3`, вам нужно будет установить инструмент `virtualenv` при помощи `pip install virtualenv`. 
Если вы используете `Python 3`, у вас уже должен быть модуль [venv](https://docs.python.org/3/library/venv.html), установленный в стандартной библиотеке.

- Создайте на своем компютере папку проекта foodgram `mkdir JSON_debugging` и перейдите в нее `cd JSON_debugging`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/SergePogorelov/JSON_debugging .`
- Создайте виртуальное окружение `python3 -m venv venv`
- Активируйте виртуальное окружение `source venv/bin/activate`
- Установите зависимости `pip install -r requirements.txt`
- Запустите скрипт `python jsondebugging.py`

Результы работы скрипта будут сохранены в файл `JSON_debug_<текущие дата и время>`.

**Пример файла:**
```
#1. Checking the file: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json
--------------------
ERROR: The schema for the file was not found.
SOLUTION: Add 'cmarker_calculated.schema' file to folder 'task_folder/schema/'.

********************

#2. Checking the file: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json
--------------------
ERROR: 'unique_id' is a required property.
SOLUTION: Аdd the 'unique_id' property to JSON data.
--------------------
ERROR: 'user' is a required property.
SOLUTION: Аdd the 'user' property to JSON data.
--------------------
ERROR: 'user_id' is a required property.
SOLUTION: Аdd the 'user_id' property to JSON data.

********************

#3. Checking the file: c72d21cf-1152-4d8e-b649-e198149d5bbb.json
--------------------
ERROR: The schema for the file was not found.
SOLUTION: Add 'meditation_created.schema' file to folder 'task_folder/schema/'.

********************

#4. Checking the file: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json
--------------------
ERROR: 'unique_id' is a required property.
SOLUTION: Аdd the 'unique_id' property to JSON data.

********************

#5. Checking the file: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json
--------------------
ERROR: The schema for the file was not found.
SOLUTION: Add 'meditation_created.schema' file to folder 'task_folder/schema/'.

********************

#6. Checking the file: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json
--------------------
ERROR: None is not of type 'integer'.
SOLUTION: Add a value with the correct data type: 'integer'.
--------------------
ERROR: 'suprt marker' is not of type 'array'.
SOLUTION: Add a value with the correct data type: 'suprt marker'.

********************

#7. Checking the file: ba25151c-914f-4f47-909a-7a65a6339f34.json
--------------------
ERROR: The schema for the file was not found.
SOLUTION: Add 'label_       selected.schema' file to folder 'task_folder/schema/'.

********************

#8. Checking the file: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json
OK: No errors found.

********************

#9. Checking the file: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json
--------------------
ERROR: 'type' is a required property.
SOLUTION: Аdd the 'type' property to JSON data.
--------------------
ERROR: 'type' is a required property.
SOLUTION: Аdd the 'type' property to JSON data.
--------------------
ERROR: 'type' is a required property.
SOLUTION: Аdd the 'type' property to JSON data.

********************

#10. Checking the file: 3b4088ef-7521-4114-ac56-57c68632d431.json
OK: No errors found.

********************

#11. Checking the file: 6b1984e5-4092-4279-9dce-bdaa831c7932.json
--------------------
ERROR: The schema for the file was not found.
SOLUTION: Add 'meditation_created.schema' file to folder 'task_folder/schema/'.

********************

#12. Checking the file: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json
--------------------
ERROR: The file is empty.
SOLUTION: Add data to JSON file: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json.

********************

#13. Checking the file: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json
--------------------
ERROR: 'bad user id' is not of type 'integer'.
SOLUTION: Add a value with the correct data type: 'bad user id'.

********************

#14. Checking the file: a95d845c-8d9e-4e07-8948-275167643a40.json
--------------------
ERROR: There is no 'event' in the JSON file.
SOLUTION: Add 'event' property to JSON file.

********************

#15. Checking the file: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json
--------------------
ERROR: 'cmarkers' is a required property.
SOLUTION: Аdd the 'cmarkers' property to JSON data.

********************

#16. Checking the file: cc07e442-7986-4714-8fc2-ac2256690a90.json
--------------------
ERROR: None is not of type 'object'.
SOLUTION: Add a value with the correct data type: 'object'.

********************

```

## В разработке использованы

- [Python](https://www.python.org/)
- [jsonschema](https://github.com/Julian/jsonschema)
