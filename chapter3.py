cars = ["jeep", "jetta", "altima", "escape"]
# print(cars)
# print(cars[1].title())
# print(cars[-2].upper()) # -1 grabs last element in a list same for -2 etc....
print(f"I hope I can get that {cars[0].title()}.")

motorcycles = ["honda", "kawasaki", "suzuki"]
motorcycles[0] = "ducati"
motorcycles.append('honda')
motorcycles.insert(1, 'moto guzzi')
del motorcycles[-1] # honda
print(motorcycles)

books = []
books.append('On the Road')
books.append('The Great Gatsby')
del books[1]
print(books)

pets = ["luna", "beatrice", "sully"]
cat = pets.pop()
print(pets)
print(f"The last pet we got was {cat.title()}.")
print(f"The oldest pet we have is {pets.pop(0).title()}.")

relatives = ['katie', 'ron', 'noelle', 'rob']
pain_in_the_ass = 'katie'
relatives.remove(pain_in_the_ass)
print(f'Sometimes {pain_in_the_ass.title()} can be a real pain in the ass.')