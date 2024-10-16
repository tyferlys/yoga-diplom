import asyncpg
from asyncpg import Connection

from src.website.utils.database_manager import DataBaseManager
from src.admin.api.poses.schemas import PoseIn, OtherTitleIn, OtherTitleInUpdate


class PosesRepository(DataBaseManager):
    async def get_count_poses(self):
        connection: Connection = await asyncpg.connect(**self.db_config)
        count = await connection.fetchval("""
                    SELECT COUNT(*) FROM poses 
                """)
        return count

    async def get_poses(self, count: int, page: int):
        connection: Connection = await asyncpg.connect(**self.db_config)
        rows = await connection.fetch("""
                    SELECT * FROM poses ORDER BY id OFFSET $1 LIMIT $2
                """, page * count, count)
        return rows

    async def get_pose_by_id(self, id_pose: int):
        connection: Connection = await asyncpg.connect(**self.db_config)
        row = await connection.fetchrow("""
            SELECT * FROM poses WHERE id = $1
        """, id_pose)
        return row

    async def get_poses_titles(self, id_pose: int):
        connection: Connection = await asyncpg.connect(**self.db_config)
        rows = await connection.fetch("""
            SELECT * FROM poses_titles WHERE id_pose = $1 ORDER BY id
        """, id_pose)
        return rows

    async def update_pose_by_id(self, id_pose: int, pose_data: PoseIn):
        connection: Connection = await asyncpg.connect(**self.db_config)
        await connection.execute("""
            UPDATE poses SET source_title = $1, description = $2, short_description = $3 WHERE id = $4
        """, pose_data.source_title, pose_data.description, pose_data.short_description, id_pose)

    async def get_other_title_by_id(self, id_other_title: int):
        connection: Connection = await asyncpg.connect(**self.db_config)
        row = await connection.fetchrow("""
            SELECT * FROM poses_titles WHERE id = $1
        """, id_other_title)
        return row

    async def create_other_title(self, id_pose: int, other_title_data: OtherTitleIn):
        connection: Connection = await asyncpg.connect(**self.db_config)
        await connection.execute("""
            INSERT INTO poses_titles(id_pose, title) VALUES($1, $2)
        """, id_pose, other_title_data.title)

    async def update_other_title(self, id_other_title: int, other_title_data: OtherTitleInUpdate):
        connection: Connection = await asyncpg.connect(**self.db_config)
        await connection.execute("""
            UPDATE poses_titles SET title = $1 WHERE id = $2
        """, other_title_data.title, id_other_title)

    async def delete_other_title(self, id_other_title: int):
        connection: Connection = await asyncpg.connect(**self.db_config)
        await connection.execute("""
            DELETE FROM poses_titles WHERE id = $1
        """, id_other_title)

    async def update_image(self, id_pose: int, image_path: str):
        connection: Connection = await asyncpg.connect(**self.db_config)
        await connection.execute("""
                UPDATE poses SET image = $1 WHERE id = $2
        """, image_path, id_pose)