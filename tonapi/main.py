from enum import Enum
from typing import Any, Literal

from aiohttp import ClientSession


class Diff(Enum):
    """Diff class."""

    ONE_DAY = "1d"
    SEVEN_DAYS = "7d"
    THIRTY_DAYS = "30d"

class TonAPI:
    """API class."""

    base_url = "https://tonapi.io/v2/rates?tokens={tokens}&currencies={currencies}"

    async def get_rate(
            self: Any,
            tokens: str,
            currencies: str,
            ) -> float:

        url = self.base_url.format(
            tokens=tokens,
            currencies=currencies,
            )
        async with ClientSession() as session:
            response = await session.get(url=url)
            response_data = await response.json()
            return response_data["rates"][tokens]["prices"][currencies]

    async def get_diff(
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
