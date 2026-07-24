'''import asyncio


async def letter():
    for letter in ['A', 'E', 'I', 'O', 'U']:
        print(letter)
        await asyncio.sleep(0) # literally like yield
        
async def number():
    for number in [1, 2, 3, 4, 5]:
        print(number)
        await asyncio.sleep(0)

async def color():
    for color in ['🔴', '🟠', '🟡','🟢','🔵']:
        print(color)
        await asyncio.sleep(0)

async def main():
    await asyncio.gather(*[letter(), number(), color()])
    print('Done')

asyncio.run(main())'''


def letter():
    for letter in ['A', 'E', 'I', 'O', 'U']:
        print(letter)
        
def number():
    for number in [1, 2, 3, 4, 5]:
        print(number)


def color():
    for color in ['🔴', '🟠', '🟡','🟢','🔵']:
        print(color)

def main():
    letter()
    number()
    color()
    print("Done")

main()




'''import asyncio
import httpx
from pyscript import document, web
from random import randint
import json


root = document.getElementById("lagayan")
API_ENDPOINT = "https://v2.jokeapi.dev/joke/Pun?type=single"

def request_joke(ev):
    joke_idx = randint(0, 1367)

    joke_container = document.getElementById("joke-container")

    joke_json = httpx.get(API_ENDPOINT)
    joke_json_str = joke_json.text
    joke_container.innerText = json.loads(joke_json_str)["joke"]

btn = document.getElementById("joke-btn")
btn.innerText = "fetch joke"
btn.addEventListener("click", web.create_proxy(request_joke))'''