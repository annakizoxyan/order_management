from functools import lru_cache
from pydantic_settings import BaseSettings


class EnvSecrets(BaseSettings):
    MONGO_DB: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_URI: str | None = None

    class Config:
        env_file = ".env"

    def build_mongo_uri(self, test: bool = False):
        db_name = self.MONGO_DB + "_test" if test else self.MONGO_DB
        return (
            f"mongodb://{self.MONGO_USER}:{self.MONGO_PASSWORD}"
            f"@{self.MONGO_HOST}:{self.MONGO_PORT}/{db_name}?authSource=admin"
        )


@lru_cache
def get_env_secrets() -> EnvSecrets:
    return EnvSecrets()
