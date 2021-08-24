def age_assignment(*names,**ages):
    dict = {name:0 for name in names}

    for first_letter, age in ages.items():
        for name in dict:
            if name.startswith(first_letter):
                dict[name] = age

    return dict

print(age_assignment("Peter","George",P = 18,G = 20))