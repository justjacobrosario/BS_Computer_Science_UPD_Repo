from pyscript import display, HTML, fetch
import asyncio
from js import document
import json


search_bar_html = """
    <div style="display: flex; gap: 10px;">
        <input type="text" id="search_bar" placeholder="Enter name..." style="font-family: Verdana, sans-serif;">
        <label style="font-family: Verdana, sans-serif;"><input type="checkbox" id="gen1" checked>Gen 1</label>
        <label style="font-family: Verdana, sans-serif;"><input type="checkbox" id="gen2">Gen 2</label>
        <label style="font-family: Verdana, sans-serif;"><input type="checkbox" id="gen3">Gen 3</label>
        <label style="font-family: Verdana, sans-serif;"><input type="checkbox" id="gen4">Gen 4</label>
        <label style="font-family: Verdana, sans-serif;"><input type="checkbox" id="gen5">Gen 5</label>
        <label style="font-family: Verdana, sans-serif;"><input type="checkbox" id="gen6">Gen 6</label>
        <label style="font-family: Verdana, sans-serif;"><input type="checkbox" id="gen7">Gen 7</label>
        <label style="font-family: Verdana, sans-serif;"><input type="checkbox" id="gen8">Gen 8</label>
        <label style="font-family: Verdana, sans-serif;"><input type="checkbox" id="gen9">Gen 9</label>
    </div>
    <div id="results_div" style="display: grid; grid-template-columns: auto auto auto auto; gap: 15px;"></div>
"""

display(HTML(search_bar_html), target="app")

generation_checkboxes = {
    "1": True,
    "2": False,
    "3": False,
    "4": False,
    "5": False,
    "6": False,
    "7": False,
    "8": False,
    "9": False
}

# ACCEPTS A LIST OF "POKEMON" AND DISPLAYS POKEMON IN COLUMNS OF 4
def display_pokemon(matches):
    results_div = document.getElementById("results_div")
    results_div.innerHTML = ''
    
    if not matches:
        results_div.innerHTML = "No matches found."
        return

    for p in matches:
        box = f"""
        <div style="padding: 15px; margin: 10px 0; border-radius: 10px; display: flex; align-items: center; gap: 20px;">
            <img src="{p['sprite']}" style="width: 80px;">
            <div>
                <h1 style="margin-bottom: 10px; text-transform: capitalize; font-family: Verdana, sans-serif;">{p['name']}</h1>
                <code>{" | ".join(pokemon_type['type']['name'][:1].upper() + pokemon_type['type']['name'][1:] for pokemon_type in p['type'])}</code>
                <p style="margin: 10px 0; font-family: Verdana, sans-serif;">Height: {p['height']} m</p>
                <p style="margin: 10px 0; font-family: Verdana, sans-serif;">Weight: {p['weight']} kg</p>
            </div>
        </div>
        """

        results_div.innerHTML += box

async def fetch_single(pokemon):
                pokemon_id = pokemon["url"].strip("/").split("/")[-1]
                pokemon_response = await fetch(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
                pokemon_data = await pokemon_response.json()
                return {
                    "id": pokemon_data["id"],
                    "name": pokemon_data["name"],
                    "height": pokemon_data["height"] / 10,
                    "weight": pokemon_data["weight"] / 10,
                    "type": pokemon_data["types"],
                    "sprite": pokemon_data["sprites"]["front_default"]
                }


# FETCHES FROM POKEAPI AND CALLS DISPLAY_POKEMON WITH LIST OF POKEMON THAT MATCH THE SEARCH INPUT AND GENERATIONS CHECKED
async def fetch_pokemon(event):

    detailed_results = []

    search_input = document.getElementById("search_bar")
    search_string = search_input.value.lower().strip()
    search_string_length = len(search_string)

    for gen_num, is_checked in generation_checkboxes.items():
        if is_checked:
            response = await fetch(f"https://pokeapi.co/api/v2/generation/{gen_num}")
            data = await response.json()

            pokemon_list = data["pokemon_species"]

            matches = []
            for p in pokemon_list:
                if p["name"].lower()[:search_string_length] == search_string:
                    matches.append(p)
                    if len(matches) >= 50:
                        break
            
            results = await asyncio.gather(*[fetch_single(p) for p in matches])
            detailed_results = detailed_results + results

    detailed_results.sort(key=lambda x: x["id"])
        
    display_pokemon(detailed_results)

# CHANGES BOOLEAN STATE OF GENERATION IN GENERATION_CHECKBOXES
def update_generation_requirements(generation, event):
    is_checked = event.target.checked
    generation_checkboxes[generation] = is_checked

# EXECUTES BOTH UPDATE_GENERATION_REQUIREMENTS AND FETCH_POKEMON 
def create_handler(gen_num):

    async def handler(event):
        update_generation_requirements(gen_num, event)
        await fetch_pokemon(event)

    return handler

document.getElementById("search_bar").oninput = fetch_pokemon
document.getElementById("gen1").onclick = create_handler("1")
document.getElementById("gen2").onclick = create_handler("2")
document.getElementById("gen3").onclick = create_handler("3")
document.getElementById("gen4").onclick = create_handler("4")
document.getElementById("gen5").onclick = create_handler("5")
document.getElementById("gen6").onclick = create_handler("6")
document.getElementById("gen7").onclick = create_handler("7")
document.getElementById("gen8").onclick = create_handler("8")
document.getElementById("gen9").onclick = create_handler("9")