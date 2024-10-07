import asyncio
import os

import asyncpg
from asyncpg import Connection

current_directory = os.path.abspath(__file__)
directory_dataset = os.path.join(current_directory, os.pardir, os.pardir, os.pardir, os.pardir, "resources", "yoga-82-dataset", "test")
db_config = {
    'user': "postgres",
    'password': "1234",
    'database': "yoga",
    'host': "localhost",
    'port': "5432"
}


async def database_creator():
    connection: Connection = await asyncpg.connect(**db_config)
    for item in os.listdir(directory_dataset):
        item = item.replace("_", " ").strip()
        await connection.execute("""
            INSERT INTO poses(source_title) VALUES($1)
        """, item)



if __name__ == "__main__":
    asyncio.run(database_creator())