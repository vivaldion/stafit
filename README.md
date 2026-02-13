1. клонировать репозиторий
   git@github.com:vivaldion/stafit.git
3. в папке проекта создать виртуальное окружение
   python -m venv env
5. активировать виртуальное окружение
   env\Scripts\activate.bat
6. в папке проекта с помощью пип загрузить необходимые зависимости из файла requirements.txt
   pip install -r requirements.txt
7. запускать файл с помощью команды, где economic1.csv economic2.csv имена файлов, которые необходимо прочесть, report.txt имя файла, куда будет сохраняться отчет
   python main.py --files economic1.csv economic2.csv --report report.txt

   Если хоть один файл существует, то срипт выполнится и будет создан файл отчета и будет произведен его вывод. Так же консоль укажет, каких файлов не существует

![Снимок](https://github.com/user-attachments/assets/67bdf4cf-4be4-42ab-ae34-e55bad4c8ed6)
Если файлов не существует, то будет такой вывод
 ![Снимок](https://github.com/user-attachments/assets/3a7d2e41-010f-4f4c-baac-50a6f7e20ca2)

Для запуска тестов применить команду   
pytest -v
