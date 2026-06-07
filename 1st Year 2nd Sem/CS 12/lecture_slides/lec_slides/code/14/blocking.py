import httpx

ranges = [1, 150, 512]

for r in ranges:
    url = f'http://httpbin.org/range/{r}?duration=2'
    print(f'Fetching {url}...')
    res = httpx.get(f'http://httpbin.org/range/{r}?duration=2')
    print(res.text)

print('Done')
