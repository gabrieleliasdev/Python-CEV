print(f"{'- = '*16}\n{'Dictionaries':^64}\n{'- = '*16}")

movies = {
            "Title": "Star Wars",
            "Year": 1977,
            "Director": "George Lucas"    
        }

print(f"This is the 'movies' Dictionary:\n » {movies}")

print(f"\n{'Exemple 01':=^64}\n")

movies["Note"] = 10
print(f"Add element (key and value) » movies['Note'] = 10\n » {movies}")

print(f"\n{'Exemple 02':=^64}\n")

del movies["Note"]
print(f"Remove Dictionary element » del movies['Note']\n » {movies}")

print(f"\n{'Exemple 03':=^64}\n{'Print only: Values | Keys | Items':^64}\n")

print(f"Print only values » movies.values()\n » {movies.values()}\n")
print(f"Print only keys » movies.keys()\n » {movies.keys()}\n")
print(f"Print only items » movies.items()\n » {movies.items()}")

print(f"\n{'Exemple 04':=^64}\n{'In Repetition Structure (loop)':^64}\n")

print("In repetition structure (loop) » for k, v in movies.items()")
for k, v in movies.items():
    print(f" » The {k} is {v}")

print(f"\n{'Exemple 05':=^64}\n{'List structure with built-in Dicionaries':^64}\n")

lst = []
lst.append(movies)
print(f"List structure with built-in Dicionaries » lst.append(movies)\n » {lst}")
print(f"\nPrint lst[0]['Title'] or lst[0]['Year']\n » {lst[0]['Title']} or {lst[0]['Year']}")

print(f"\n{'Exemple 06':=^64}\n{'Replacing values':^64}\n")

movies["Year"] = 1977.1
print(f"Replacing values » movies['Year'] = 1977.1\n » {movies}")

print(f"\n{'Exemple 07':=^64}\n{'Copy in Dicionary and List':^64}\n")

states = {}
brazil = []

for c in range(3):
    states["UF"] = str(input("Federative Unit » "))
    states["Initials"] = str(input("State Abbreviation » "))
    brazil.append(states.copy())
print(f"\n{brazil}\n")

for s in brazil:
    print(s)

print()
for s in brazil:
    for k, v in s.items():
        print(f"{k} in {v}")

print()
for s in brazil:
    for v in s.values():
        print(v, end=" ")
    print()
        