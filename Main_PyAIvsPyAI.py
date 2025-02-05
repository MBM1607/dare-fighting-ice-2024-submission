import asyncio

import typer
from pyftg.utils.gateway import get_async_gateway
from pyftg.utils.logging import DEBUG, set_logging
from typing_extensions import Annotated, Optional

from AudioAvenger import AudioAvenger
from KickAI import KickAI

app = typer.Typer(pretty_exceptions_enable=False)


async def start_process(
    host: str, port: int, use_grpc: bool, character: str = "ZEN", game_num: int = 1
):
    gateway = get_async_gateway(host, port, use_grpc)
    agent1 = AudioAvenger()
    agent2 = KickAI()
    gateway.register_ai("AudioAvenger", agent1)
    gateway.register_ai("KickAI", agent2)
    await gateway.run_game([character, character], ["AudioAvenger", "KickAI"], game_num)
    await gateway.close()


@app.command()
def main(
    host: Annotated[
        Optional[str], typer.Option(help="Host used by DareFightingICE")
    ] = "127.0.0.1",
    port: Annotated[
        Optional[int], typer.Option(help="Port used by DareFightingICE")
    ] = 50051,
    use_grpc: Annotated[
        Optional[bool], typer.Option(help="Use gRPC instead of socket")
    ] = True,
):
    asyncio.run(start_process(host, port, use_grpc))


if __name__ == "__main__":
    set_logging(log_level=DEBUG)
    app()
