import asyncpg
from asyncpg import Connection

from src.admin.utils.database_manager import DataBaseManager

from src.admin.api.poses.schemas import PoseIn


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
                    SELECT * FROM poses OFFSET $1 LIMIT $2
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
            SELECT * FROM poses_titles WHERE id_pose = $1
        """, id_pose)
        return rows

    async def update_pose_by_id(self, id_pose: int, pose_data: PoseIn):
        connection: Connection = await asyncpg.connect(**self.db_config)
        await connection.execute("""
            UPDATE poses SET source_title = $1, description = $2 WHERE id = $3
        """, pose_data.source_title, pose_data.description, id_pose)