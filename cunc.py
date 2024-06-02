# Об'єднати кодувальну і декодувальну частину із decoder_project  в один проєкт
# (бажано отримати exe файл через pyinstaller - окремо скину в це завдання exe

import os
import pickle

#список файлів та розміру
file_info = []                           

#формування списку  файлів за злиття
def get_data_info(filename): 
    with open(filename,"rb") as file:
        return {"files":filename,
                "size":len(file.read())}


#запис файлів зі списку file_info в єдиний файл res
def write_data_info(filename, res): 
    #print (str(filename)+ " : " +str(res))
    with open (filename, "rb") as files:
        res.write (files.read())


#перевірка на наявність файлу, підключили import os. повертаємо True/False
def find_files(filename): 
    if os.path.exists(filename):
        return True
    else:
        return False


#частина збору даних для запису файлів та запис файлу для відновлення
def file_coding(): 
    while True:
        choice= input("[1] Додати файл, [2] Виконати кодування, [0] Вихід : ")
        if choice=="1":
            files_data = input("Ім'я файлу для захисту :")
            if find_files (files_data):
                file_info.append(get_data_info(files_data))
                for list_info in file_info:
                    print(list_info)
            else:
                print(f"Помилка, файл {files_data} відсутній !!!")
        elif choice=="2":
            feles_du = input("Ім'я файлу результату :")
            with open(feles_du,"wb") as resault:
                for data in file_info:
                    write_data_info(data["files"],resault)
                    
            with open("info.txt","wb") as file:
                file.write(pickle.dumps(file_info))
            print(f"Операція по створенню фалу {feles_du} завершена")
        else:
            break


def file_uncoding(): #частина для розкодування файлів

    feles_du = input("Файли із даними/результатом : ")
    info_file = input("Інформаційний файл : ")

    if find_files(feles_du) and find_files(info_file):
        
        with open(info_file,"rb") as file:
            data_info = pickle.loads(file.read())

        with open(feles_du,"rb") as result_file:
            for data in data_info:
                with open(data["files"],"wb") as file:
                    file.write(result_file.read(data["size"]))

        print(f"Операція по відновленню завершена")
    else:
        if find_files(feles_du)==False:
            print(f"Помилка, файл {feles_du} відсутній !!!")
        else:
            print(f"Помилка, файл {info_file} відсутній !!!")


        
#Меню
while True:
    choice = input("""
======================
Захист інформації
======================
[1] Кодування інформації
[2] Розкодування інформації
[0] Вихід
======================
""")
    if choice=="1":
        file_coding()
    elif choice=="2":
        file_uncoding()
    else:
        break

