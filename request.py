from pyodide.http import pyfetch, FetchResponse
from typing import Optional, Any

async def request(url: str, method: str = "GET", body: Optional[str] = None,
                  headers: Optional[dict[str, str]] = None, **fetch_kwargs: Any) -> FetchResponse:
                  
                  
                  kwargs = {"method": method, "mode": "cors"} 
                  if body and method not in ["GET", "HEAD"]:
                      kwargs["body"] = body
                      if headers:
                          
                          kwargs["headers"] = headers
                          kwargs.update(fetch_kwargs)

                          response = await pyfetch(url, **kwargs)
                          return response
asyncio.ensure_future(request())
