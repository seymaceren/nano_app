import python_weather
import asyncio


# We maken hier gebruik van python_weater API om de temperatuur van een bepaalde stad
# in de wereld op te vragen
async def geef_temparatuur() -> None:
    stad = input("Welke stad: ")
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # Vraag van een stad het weer
        weather = await client.get(stad)

        # geeft de temperatuur terug in graden celcius
        print(f"{int(round((weather.temperature - 32) * 5/9, 0))}°C")

def run():
    asyncio.run(geef_temparatuur())
if __name__ == '__main__':
    run()
