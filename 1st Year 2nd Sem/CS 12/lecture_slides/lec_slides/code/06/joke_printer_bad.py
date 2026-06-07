import httpx
 
class JokePrinter:
    def print_joke(self, joke: str):
        print('Time for a joke:')
        print()
        print(joke)
 
    def fetch_joke(self):
        url = 'https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,racist,sexist&format=txt'
        resp = httpx.get(url)
 
        return resp.text
 
    def run(self):
        joke = self.fetch_joke()
        self.print_joke(joke)
