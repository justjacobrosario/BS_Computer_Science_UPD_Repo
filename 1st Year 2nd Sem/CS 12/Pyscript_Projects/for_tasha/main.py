from pyscript import web, document
import json
import random

root = document.getElementById("wrapper")
root.style.display = "flex"
root.style.flexDirection = "column"
root.style.alignItems = "center"
root.style.justifyContent = "center"
root.style.height = "100vh"
root.style.gap = "20px"    



def get_response(ev):
	with open("data.json", "r") as f:
		data = json.load(f)
	rand_id = random.randint(0, 74)
	text.innerHTML = data[rand_id]

text = document.createElement("div")
text.innerText = "Click the button hehe :))"
text.style.fontSize = "1.5rem"


btn = document.createElement("button")
btn.innerText = "😘😘😘"
btn.style.padding = "10px 20px"
btn.style.fontSize = "2rem"
btn.style.cursor = "pointer"
btn.style.backgroundColor = "#343830"
btn.style.borderRadius = "20%"
btn.addEventListener("click", web.create_proxy(get_response))


root.appendChild(text)
root.appendChild(btn)