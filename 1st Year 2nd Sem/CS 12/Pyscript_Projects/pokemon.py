import random
import asyncio

from pyscript import document, web

import httpx

API_ENDPOINT = f'https://pokeapi.co/api/v2/pokemon/'

def create_pokemon_entry(pokemon_data):
    td = document.createElement("td")
    td.style = "border: 1px solid black; border-radius: 3px;"
    p = document.createElement("p")
    p.innerText = (pokemon_data['name'] or '').capitalize()
    image = document.createElement("img")
    image.src = pokemon_data['sprites']['front_default']
    image.alt = pokemon_data['name']
    td.appendChild(image)
    td.appendChild(p)
    return td


async def fetch_pokemon(ev):
    row_one = document.getElementById("row-1")
    row_two = document.getElementById("row-2")
    loader = document.getElementById("pokemon-loader")
    row_one.innerHTML = ""
    row_two.innerHTML = ""
    loader.style = "display: inline;"

    params = {}
    random_ids = random.sample(range(1, 1025 + 1), 10)
    results = []
    for poke_id in random_ids:
        async with httpx.AsyncClient() as client:
            res = await client.get(f'{API_ENDPOINT}/{poke_id}/', params=params)
            results.append(res.json())

    loader.style = "display: none;"

    for pokemon_data in results[:5]:
        poke = create_pokemon_entry(pokemon_data)
        row_one.appendChild(poke)
    for pokemon_data in results[5:]:
        poke = create_pokemon_entry(pokemon_data)
        row_two.appendChild(poke)
    

poke_btn = document.getElementById("pokemon-btn")
poke_btn.addEventListener("click", web.create_proxy(fetch_pokemon))
