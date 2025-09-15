from typing import Generic, List, Type, TypeVar, Optional
from uuid import UUID
from beanie import Document
from beanie.odm.operators.find.comparison import In

ModelType = TypeVar("ModelType", bound=Document)


class BaseRepo(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, obj: ModelType) -> ModelType:
        await obj.insert()
        return obj

    async def get_by_id(self, obj_id: UUID) -> Optional[ModelType]:
        return await self.model.get(obj_id)

    async def list_all(self) -> List[ModelType]:
        return await self.model.find_all().to_list()

    async def get_by_ids(self, ids: List[UUID]) -> List[ModelType]:
        return await self.model.find(In(self.model.id, ids)).to_list()
