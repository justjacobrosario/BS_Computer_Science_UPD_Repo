import httpx

from pyscript import document, web

counter = 0

def increment(ev):
    global counter
    p = document.getElementById("ctr-text")
    counter += 1
    p.innerText = str(counter)

async def fetch_joke(ev):
    joke_p = document.getElementById("joke-text")
    params = {
        'blacklistFlags': "nsfw,racist,sexist,explicit",
        'format': 'txt',
        'rq_delayed': 'true'
    }
    async with httpx.AsyncClient() as client:
        res = await client.get("https://app.requestly.io/delay/2000/v2.jokeapi.dev/joke/Programming", params=params)
    joke_p.innerText = res.text


incr_btn = document.getElementById("incr-btn")
joke_btn = document.getElementById("joke-btn")

incr_btn.addEventListener("click", web.create_proxy(increment))
joke_btn.addEventListener("click", web.create_proxy(fetch_joke))
