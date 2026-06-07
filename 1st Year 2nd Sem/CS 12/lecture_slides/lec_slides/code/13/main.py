from pyscript import document, web

# MENTION: camelcase Javascript convention used for Pyscript
# MENTION: pyscript lacks checkable type annotations

root = document.getElementById("app")

count = 0

def handle_incr(ev):
    global count
    print("+ was clicked")
    count += 1
    ctr.innerText = str(count)

def handle_decr(ev):
    global count
    print("- was clicked")
    count -= 1
    ctr.innerText = str(count)

incr_btn = document.createElement("button")
incr_btn.innerText = "+"
incr_btn.addEventListener("click", web.create_proxy(handle_incr))

ctr = document.createElement("p")
ctr.innerText = "0"

decr_btn = document.createElement("button")
decr_btn.innerText = "-"
decr_btn.addEventListener("click", web.create_proxy(handle_decr))

root.appendChild(incr_btn)
root.appendChild(ctr)
root.appendChild(decr_btn)