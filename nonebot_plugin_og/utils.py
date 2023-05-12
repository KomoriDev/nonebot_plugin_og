import re
import httpx
from typing import Any, Dict, Optional
from pyquery import PyQuery as pq

async def get_og_info(msg: Any) -> Optional[Dict[str, Any]]:
    url = re.search(r'(https?://\S+)', str(msg))
    if not url:
        return None

    async with httpx.AsyncClient() as client:
        res = await client.get(url.group())
        doc = pq(res.content)

    meta_tags = doc('meta')
    og_keys = ['type', 'url', 'title', 'description', 'image']

    info = {}
    for tag in meta_tags.items():
        property_name = tag.attr('property')
        if property_name and property_name.startswith('og:'):
            key = property_name[3:]
            value = tag.attr('content')
            if key in og_keys:
                info[key] = value
    return info