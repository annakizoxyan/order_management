import uuid
from beanie import Document
from pydantic import Field


class UUIDDocument(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    class Settings:
        use_state_management = True
        validate_on_save = True
