from pprint import pprint
import csv
import re

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код
    my_list = contacts_list[1:]
    fio_list = []
    final_list = []
    for row in my_list:
        fio = " ".join(row[0:3]).split(' ')
        if '' in fio:
            fio.remove('')
        row[0:3] = fio[0:3]
        pattern = r'(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})(\s*)\(?(доб.)?\s*(\d{4})?\)?'
        repl_pattern = r'+7(\2)\3-\4-\5\6\7\8'
        phone = re.sub(pattern, repl_pattern, row[-2])
        row[-2] = phone

        fi = " ".join(row[0:2]).strip()
        if fi not in fio_list:
            fio_list.append(fi)
            final_list.append(row)
        else:
            for ids, column in enumerate(row[3:]):
                if column:
                    final_list[fio_list.index(fi)][3+ids] = column
    final_list.insert(0, contacts_list[0])

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(final_list)
