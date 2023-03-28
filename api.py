from aiohttp import ClientSession
from data import config

url = config.MYURL
# head = {'Authorization': f'token {config.MYTOKEN}'}

async def user_post( username: str, telegram_id: str):
    async with ClientSession() as session:
        http = f"{url}/user/"
  
        async with session.post(url=http, data = {'username': username, 'telegram_id': telegram_id}) as response: #, headers=head
            if response.status == 201:
                 return True
            else:
                 return False            
            
async def product_get():
    async with ClientSession() as session:
        http = f"{url}/product/"
  
        async with session.get(url=http) as response:
            if response.status == 200:
                 result = await response.json()
                 return result
            else:
                 return False
            
async def info_get():
    async with ClientSession() as session:
        http = f"{url}/info/"
  
        async with session.get(url=http) as response:
            if response.status == 200:
                 result = await response.json()
                 return result
            else:
                 return False
            
async def get_lang(id):
    async with ClientSession() as session:
        http = f"{url}/user/{id}/"
  
        async with session.get(url=http) as response:
            if response.status == 200:
                 result = await response.json()
                 return result
            else:
                 return False
            
async def put_lang(id, lang):
    async with ClientSession() as session:
        http = f"{url}/user/{id}/"
  
        async with session.put(url=http, data = {'lang': lang}) as response:
            if response.status == 200:
                 return True
            else:
                 return False 