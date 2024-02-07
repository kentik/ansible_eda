"""kentik_webhook.py.

Description:
This is an event source plugin for receiving events via a webhook
from the webhook notifications action of Kentik's Alerting engine.
The message must be a valid JSON object.

Arguments:
---------
    host:     The hostname to listen to. Defaults to 0.0.0.0 (all interfaces)
    port:     The TCP port to listen to.  Defaults to 5000

"""
import asyncio
import json
import logging
from collections.abc import Callable
from typing import Any

from aiohttp import web

logger = logging.getLogger(__name__)
routes = web.RouteTableDef()

# Initialize the loggger configuration
def _initialize_logger_config() -> None:
    logging.basicConfig(
        format="[%(asctime)s] - %(pathname)s: %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %I:%M:%S",
    )

# Process incoming webhook alert notifications from Kentik
@routes.post("/alert")
async def webhook(request: web.Request) -> web.Response:
    """Process incoming webhook alert notifications from Kentik
    
    Parameters
    ----------
    request : web.Request
        Received request

    Returns
    -------
    Response with empty JSON object

    Raises
    ------
    HTTPBadRequest
        If the payload can't be parsed as JSON
        
    """
    logger.info("Received alert")
    try:
        payload = await request.json()
    except json.JSONDecodeError as exc:
        logger.warning("Wrong body request: failed to decode JSON payload: %s", exc)
        raise web.HTTPBadRequest(text="Invalid JSON payload") from None
    headers = dict(request.headers)
    headers.pop("Authorization", None)
    data = {
        "payload": payload,
        "meta": {"headers": headers},
    }
    logger.info("Put alert on queue")
    await request.app["queue"].put(data)
    return web.json_response({})

# Set app_attr settings in a dictionary
def set_app_attr(args: dict[str, Any]) -> dict[str, Any]:
    """Set app_attr settings in a dictionary

    Parameters
    ----------
    args : Dict[str,Any]
        Empty dictionary of arguments
    
    Returns
    -------
    args : Dict[str,Any]
        Args containing the host and port
    
    """
    if "host" not in args:
        host="0.0.0.0"
    if "port" not in args:
        port=5000
    app_attrs = {}
    app_attrs["host"] = args.get("host")
    app_attrs["port"] = args.get("port")

    return app_attrs

# Entrypoint from ansible-rulebook
async def main(queue: asyncio.Queue, args: dict[str, Any]) -> None:
    """Receive events via webhook.
    
    Parameters
    ----------
    queue : asyncio.Queue
        Problem queue
    args : Dict[str,Any])
        Args containing the host and port

    """
    _initialize_logger_config()
    logging.info("Starting kentik_webhook...")
    
    app_attrs = set_app_attr(args)
    app = web.Application()
    app.add_routes(routes)

    # Store queue to access it in the event handler function
    app["queue"] = queue

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(
        runner,
        app_attrs["host"],
        app_attrs["port"],
    )
    await site.start()
    logger.info("kentik_webhook is running and waiting for alerts")

    try:
        await asyncio.Future()
    except asyncio.CancelledError:
        logger.info("Webhook Plugin Task Cancelled")
    finally:
        await runner.cleanup()

if __name__ == "__main__":
    """MockQueue if running directly."""

    class MockQueue:
        """A fake queue."""

        async def put(self: "MockQueue", event: dict) -> None:
            """Print the event."""
            print(event)
    
    asyncio.run(
        main(
            MockQueue(),
            {
                "host": "localhost",
                "port": 80,
            },
        ),
    )
