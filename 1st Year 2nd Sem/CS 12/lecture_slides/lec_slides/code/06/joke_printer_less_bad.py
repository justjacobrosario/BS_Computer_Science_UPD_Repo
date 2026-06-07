import httpx


class JokePrinter:
    def print_joke(self, joke: str):
        print('Time for a joke:')
        print()
        print(joke)
 
    def run(self):
        joke = ProgrammingJokeFetcher().fetch_joke()  # Baked-in dependency
        self.print_joke(joke)

class ProgrammingJokeFetcher:
    def fetch_joke(self):
        url = 'https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,racist,sexist&format=txt'
        resp = httpx.get(url)
 
        return resp.text
