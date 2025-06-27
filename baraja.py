import random

MAXIMOPALO=10

#------------------------------------------

palos=["corazon", "diamante", "pica", "trebol"]

baraja=[]
for palo in palos:
    for i in range(MAXIMOPALO):
        carta={
            "palo": palo,
            "valor": i+1,
            "girada": False
        }
        baraja.append(carta)

random.shuffle(baraja)


print(baraja)

matriz_pilas=[
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

for i in range(len(matriz_pilas)):
    match i:
        case 0:
            matriz_pilas[i].append(baraja[0])
        case 1:
            for j in range(1, 3):
                matriz_pilas[i].append(baraja[j])
        case 2:
            pass


for carta in baraja:
    if carta["palo"]=="pica":
        print(carta)