import requests
from bs4 import BeautifulSoup
from random import choice
list1=[]
r = requests.get("https://www.imdb.com/search/title/?genres=sci-fi&%22")
soup=BeautifulSoup(r.text, "html.parser")
movies = soup.find_all(class_="lister-item-content")
for name in movies:
    name_tags = name.find_all('p')[2]
    name_tags1 = name_tags.find_all('a')
    names= [tag.get_text() for tag in name_tags1]
    elements_with_class = name.find_all(class_="text-muted")
    second_element = elements_with_class[2]
    list1.append({"Name":name.find("a").get_text(),
                  "Year released":name.find("span",class_="lister-item-year text-muted unbold").get_text(),
                  "Description":second_element.get_text(strip=True),
                  "Cast":names
                  })
print("Hello!! Welcome to the game\n")
while True:
    a=int(input("Enter:\n1.Instructions of the game\n2.Play the game\n3.Quit the game\n\n"))
    if a==1:
        print("\nYou will be given some clues about a Sci-Fi movie, Your task is to guess the name of the movie. You will be given three guesses!\nReady?")
    if a==2:
        hello = choice(list1)
        remaining_guesses = 3
        print("\nHere's the descritpion of the movie:")
        print(hello["Description"])
        print()
        guess = ''
        while guess.lower() != hello["Name"].lower() and remaining_guesses>0:
            guess = input(f"What's the movie name? Guesses remaining {remaining_guesses}\n")
            if guess.lower() == hello["Name"].lower():
                print("Hurray!! You go the correct answer\n")
                break
            remaining_guesses -=1
            if remaining_guesses == 2:
                print(f"\nHint 1:The director and cast of the movie\n{', '.join(hello['Cast'])}")
            elif remaining_guesses == 1:
                print(f"\nHint 2: Year released: {hello['Year released']}")
            else:
                print(f"\nOut of guesses! Try again next time\nThe answer is {hello['Name']}\n")
    if a==3:
        break





      