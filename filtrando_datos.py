DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
# 1. list comprehensions  , nombres de todos que trabajan en python
    all_python_devs=[dev["name"] for dev in DATA if dev["language"]=="python"]
# Usando filter y map
    all_devs =list(filter(lambda dev: dev["language"]=="python",DATA))
    devs = list(map(lambda dev: dev["name"],all_devs))

# 2. Usando List comprenhensions , devs que trabajan en platzi 
    all_platzi_workers=[worker["name"] for worker in DATA if worker["organization"]=="Platzi"]

# Usando filter and map

    all_workers= list(filter(lambda worker:worker["organization"]=="Platzi", DATA))
    workers=list(map(lambda worker: worker["name"],all_workers))
# 3. A.  List conprehension para personas mayores de edad
#     all_people_old=[people["name"] for people in DATA if people["age"]>=18]
#  B. Opcion 2 te trae disccionarios 
    all_people_old = list(filter(lambda people: people["age"]>=18,DATA)) 
    adults=list(map(lambda people: people["name"], all_people_old))
    
# agregar caracteristica al diccionario 
#1.A 
    old_people= [x|{ "old": x["age"]>70} for x in DATA ]


# 1.B  old_people = list( map(lambda worker: worker|{ "old": worker["age"]>70},DATA ))

    for people in old_people:
        print(people)
if __name__=='__main__':
    run()    