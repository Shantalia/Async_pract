import asyncio
from faker import Faker
from timing import async_timed

fake = Faker('uk-UA')

# Avaitable -> Coroutine
# Avaitable -> Future -> Task

async def async_get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)
    return {'id': uuid, 'username': fake.user_name(), 'email': fake.email()}

@async_timed('Перевірка future')
async def main():
    users = []
    for i in range(1, 6):
        task = asyncio.create_task(async_get_user_from_db(i))
        users.append(task)
    print(users)
    result = await asyncio.gather(*users)
    return result

if __name__ == '__main__':
    users = asyncio.run(main())
    print(users)
