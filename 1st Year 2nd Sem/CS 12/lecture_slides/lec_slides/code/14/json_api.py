import asyncio
import httpx
 
API_ENDPOINT = 'https://pokeapi.co/api/v2/pokemon'
 
async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get(API_ENDPOINT)
        data = response.json()
 
    print(data)
 
asyncio.run(main())
