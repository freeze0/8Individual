import csv
import datetime
import locale
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)

date = '5 Апрель 2017 14:00'
z_date = datetime.datetime.strptime(date, '%d %B %Y %H:%M')
with open("7 - 1.csv", encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")

    header = next(file_reader)
    end_index = header.index('Завершено')
    B1_index = header.index('В. 1 /1,00')
    B2_index = header.index('В. 2 /1,00')
    B3_index = header.index('В. 3 /1,00')
    B12_count = 0
    B3_count = 0

    for row in file_reader:
        end = " ".join(str(row[end_index]).split())
        if end == '-' or end == '':
            print('')
        else:
            end_date = datetime.datetime.strptime(end, '%d %B %Y %H:%M')
            print(end_date)
            if z_date < end_date:
                if str(row[B1_index]) == '0,00':
                    B12_count += 1
                if str(row[B2_index]) == '0,00':
                    B12_count += 1
                if str(row[B3_index]) == '0,00':
                    B3_count += 1

print('Неверные ответы Основы законодательства РФ в области образования', B12_count)
print('Неверные ответы Экономико-правовое регулирование педагогической деятельности', B3_count)







