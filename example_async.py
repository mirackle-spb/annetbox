import asyncio
import os

from annetbox.base.client_async import NetboxStatusClient
from annetbox.v37.client_async import NetboxV37


async def main():
    url = os.getenv("NETBOX_URI")

    # check the status of netbox installation
    # ClientError with `.status_code == 404` for 2.x versions
    status_client = NetboxStatusClient(url=url)
    status = await status_client.status()
    print(status)
    await status_client.close()

    # basic netbox methods
    netbox = NetboxV37(url=url)
    res = await netbox.devices(limit=1)
    print(res)
    print()

    res = await netbox.interfaces(limit=1)
    print(res)
    print()

    res = await netbox.ip_addresses(limit=1)
    print(res)
    print()

    await netbox.close()


if __name__ == '__main__':
    asyncio.run(main())
