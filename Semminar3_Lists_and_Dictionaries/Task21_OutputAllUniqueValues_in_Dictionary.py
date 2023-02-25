# Напишите программу для печати всех уникальных значений в словаре.
# Input:[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#       {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
listNew = []
for a in list:
  for item in a: # for (k,v) in dictionary.items():
      listNew.append(a[item])
print(set(listNew))
