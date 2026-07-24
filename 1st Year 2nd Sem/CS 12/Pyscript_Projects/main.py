from pyscript import document, web, fetch
print("NEW ITOOO")
root = document.getElementById("app")

API_ENDPOINT = 'https://pokeapi.co/api/v2/'

async def get_poke(ev):
    text_input = (document.getElementById("inpt").value).lower().strip()
    response =  await fetch(f"{API_ENDPOINT}pokemon/{text_input}")
    data = await response.json()
    output.innerText = data

text_input = document.getElementById("inpt")

output = document.getElementById("output")


btn = document.getElementById("btn")
btn.addEventListener("click", web.create_proxy(get_poke))



