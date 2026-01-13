from uuid import UUID
from db import support_table, database
from core.domain.support_message import SupportMessage
from core.repositories.isupport import ISupportRepository

class SupportRepository(ISupportRepository):

    async def add(self, user_id: UUID, message: str) -> SupportMessage:
        query = support_table.insert().values(
            user_id=user_id,
            message=message,
        )
        new_id = await database.execute(query)

        record = await database.fetch_one(
            support_table.select().where(support_table.c.message_id == new_id)
        )

        return SupportMessage.model_validate(record)
