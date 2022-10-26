from src.infrastructure.config.global_config.schemas import DatabaseDetails

__all__ = [
    "GlobalConfigurationManager"
]


class GlobalConfigurationManager:

    def __init__(self) -> None:
        self.configuration: DatabaseDetails = self.get_configuration()

    @staticmethod
    def get_configuration() -> DatabaseDetails:
        return DatabaseDetails()
