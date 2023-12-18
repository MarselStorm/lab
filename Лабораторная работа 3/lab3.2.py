def find_common_participants(group1, group2, delimiter=','):
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    set_participants1 = set(participants1)
    set_participants2 = set(participants2)

    common_participants = set_participants1.intersection(set_participants2)

    return sorted(list(common_participants))


group1 = "Иван,Петр,Виктор,Евгений,Дмитрий"
group2 = "Петр,Виктор,Александр,Дмитрий,Михаил"

result = find_common_participants(group1, group2)
print(result)
