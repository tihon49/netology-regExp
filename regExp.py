import re
from pprint import pprint
import csv


with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
phone_pattern = re.compile(r'(\+7|8)\s*\(?(\d{3})\)?(\s*|-)(\d{3})(\s*|-*)(\d{2})-?(\d{2})(\s*(\(?(\доб.)?)\s*(\d{4}))?(\))*')
text_pattern = re.compile(r'(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё]\w+[А-яЁё –]*\–*\s*)*\,*(\+*\d\s*\(*\d+\)*\-*\s*\d+\-*\d+\-*\d+\s*\(*\w*\.*\s*\d*\)*)*\,*(\w+\.*\w*\@\w+\.\w+)*')


new_contacts_list = []
for i in range(len(contacts_list)):
    if i == 0:
        new_contacts_list.append(contacts_list[i])
    else:
        line = ','.join(contacts_list[i])
        result = re.search(text_pattern, line)
        new_contacts_list.append(list(result.groups()))
        if new_contacts_list[i][0] in new_contacts_list:
            print(new_contacts_list[i][0:3])
        if new_contacts_list[i][5] != None:
            new_contacts_list[i][5] = phone_pattern.sub(r'+7(\2)\4-\6-\7 \10\11', new_contacts_list[i][5])


final_contacts_list = []
for i in range(len(new_contacts_list)):
    for j in range(len(new_contacts_list)):
        if new_contacts_list[i][0] == new_contacts_list[j][0]:
            new_contacts_list[i] = [x or y for x, y in zip(new_contacts_list[i], new_contacts_list[j])]
    if new_contacts_list[i] not in final_contacts_list:
        final_contacts_list.append(new_contacts_list[i])
        
pprint(final_contacts_list)


# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts_list)