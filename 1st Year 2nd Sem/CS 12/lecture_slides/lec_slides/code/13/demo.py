from pyscript import document, web


root = document.getElementById('app')

counter_value = 0


incr_btn = document.createElement("button")
incr_btn.innerText = '+'

counter = document.createElement("p")
counter.innerText = str(counter_value)

decr_btn = document.createElement("button")
decr_btn.innerText = '-'


input_text = document.createElement("input")
input_text.type = "text"

post_btn = document.createElement("button")
post_btn.innerText = 'Post!'

posts = document.createElement("div")
posts.id = "posts"


def add_post(ev):
    print("post was added")
    post = document.createElement("p")
    post.innerText = str(input_text.value)
    posts.appendChild(post)

def handle_incr(ev):
    global counter_value
    print("+ was clicked")
    counter_value += 1
    counter.innerText = str(counter_value)

def handle_decr(ev):
    global counter_value
    print("- was clicked")
    counter_value -= 1
    counter.innerText = str(counter_value)

# event listeners
# element, event, function

incr_btn.addEventListener("click", web.create_proxy(handle_incr))
decr_btn.addEventListener("click", web.create_proxy(handle_decr))
post_btn.addEventListener("click", web.create_proxy(add_post))



root.appendChild(incr_btn)
root.appendChild(counter)
root.appendChild(decr_btn)
root.appendChild(posts)
root.appendChild(input_text)
root.appendChild(post_btn)
