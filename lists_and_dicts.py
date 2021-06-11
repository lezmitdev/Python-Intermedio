def run():
    my_list=[1,"hello",True,4.5]
    my_dict={"firtsname","lezmit","lastname","Garcia"}

# Lista de diccionarios
    super_lits=[
        {"firtsname","lezmit","lastname","Garcia"},
        {"firtsname","Carmelo","lastname","Putin"},
        {"firtsname","lucia","lastname","Arias"},
        {"firtsname","Fernanda","lastname","Garzon"},
        {"firtsname","Camila","lastname","Paz"},
    ]
#diccionario de listas
    super_dict={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,2.2,3.3,4.4]
    }

    for key,value in super_dict.items():
        print(key,"-",value)


if __name__=='__main__':
    run()