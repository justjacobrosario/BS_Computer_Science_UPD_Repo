from pyscript import document, web

# MENTION: camelcase Javascript convention used for Pyscript
# MENTION: pyscript lacks checkable type annotations

# run ``python3 -m http.server 3000 in the same directory
# as index.html and your pyscript file


def add_counter(ev):
    number = document.getElementById("num")
    div = document.getElementById("counters")
    btn = document.createElement("button")
    value = int(number.value or '0')
    btn.innerText = str(value)

    def _event_listener(ev):
        nonlocal value
        value -= 1
        btn.innerText = str(value)

    btn.addEventListener("click", web.create_proxy(_event_listener))
    div.appendChild(btn)


root = document.getElementById("app")

number_input = document.createElement("input")
number_input.id = "num"
number_input.type = "number"
create_btn = document.createElement("button")
create_btn.innerText = 'Create button'
br = document.createElement("br")

div = document.createElement("div")
div.id = "counters"

create_btn.addEventListener("click", web.create_proxy(add_counter))

root.appendChild(number_input)
root.appendChild(create_btn)
root.appendChild(br)
root.append(div)
