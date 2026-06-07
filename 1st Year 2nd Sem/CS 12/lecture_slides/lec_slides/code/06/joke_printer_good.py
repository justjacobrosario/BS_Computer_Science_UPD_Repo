class JokeFetcher(Protocol):
    def fetch_joke(self) -> str:
        ...
 
class JokePrinter:
    def print_joke(self, joke: str):
        print('Time for a joke:')
        print()
        print(joke)
 
    def run(self, fetcher: JokeFetcher):
        joke = fetcher.fetch_joke()
        self.print_joke(joke)
 
class ProgrammingJokeFetcher:
    def fetch_joke(self):
        url = '...'
        resp = httpx.get(url)
 
        return resp.text
 
class PunJokeFetcher:
    def fetch_joke(self):
        url = 'https://v2.jokeapi.dev/joke/Pun?format=txt'
        resp = httpx.get(url)
 
        return resp.text