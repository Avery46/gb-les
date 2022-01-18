def thesaurus(*names):
  
    new_names = {}
    for name in names:
        
        key = name[0].capitalize()
        if key not in new_names:
            new_names[key] = []
        new_names[key].append(name)
       
    return new_names

print(thesaurus("Егор", "Дмитрий","Демьян", "Себастьян"))
