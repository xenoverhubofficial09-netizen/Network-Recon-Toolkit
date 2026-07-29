import aiohttp
import asyncio

HEADERS = {
    "User-Agent": "NetworkReconToolkit/2.0"
}


async def fetch(session, host):

    for protocol in ("https", "http"):

        try:

            async with session.get(

                f"{protocol}://{host}",

                headers=HEADERS,

                ssl=False,

                timeout=3,

                allow_redirects=True

            ) as response:

                return {

                    "host": host,

                    "status": response.status,

                    "server": response.headers.get("Server", "-")

                }

        except Exception:

            pass

    return None


async def async_verify(hosts):

    connector = aiohttp.TCPConnector(limit=500)

    timeout = aiohttp.ClientTimeout(total=3)

    async with aiohttp.ClientSession(

        connector=connector,

        timeout=timeout

    ) as session:

        tasks = [

            fetch(session, host)

            for host in hosts

        ]

        return await asyncio.gather(*tasks)