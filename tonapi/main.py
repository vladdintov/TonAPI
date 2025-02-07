from typing import Any, Literal

from aiohttp import ClientSession


class API:
    """API class."""

    base_tonapi_url = "https://tonapi.io/v2/rates?tokens={tokens}&currencies={currencies}"
    stonfi = "https://api.ston.fi/v1/assets/"


    async def get_rate_by_tonapi(
            self: Any,
            tokens: str,
            currencies: str,
            ) -> float:

        url = self.api.format(
            tokens=tokens,
            currencies=currencies,
            )
        async with ClientSession() as session:
            response = await session.get(url=url)
            response_data = await response.json()
            return response_data["rates"][tokens]["prices"][currencies]

    async def get_diff_by_tonapi(
            self: Any,
            tokens: str,
            currencies: str,
            diff: Literal["24h", "7d", "30d"],
        ) -> float:

        url = self.base_url.format(
            tokens=tokens,
            currencies=currencies,
            diff=diff,
        )
        async with ClientSession() as session:
            response = await session.get(url=url)
            response_data = await response.json()
            return response_data["rates"][tokens][f"diff_{diff}"][currencies]

    async def get_rate_by_stonfi(
            self: Any,
            token: str,
            ) -> float:

        url = f"{self.stonfi}{token}"
        async with ClientSession() as session:
            response = await session.get(
                url=url,
                headers={
                "Accept": "application/json",
                })
            data = await response.json()
            return data["asset"]["dex_usd_price"]
