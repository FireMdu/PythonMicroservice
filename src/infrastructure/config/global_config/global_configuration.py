import json
import traceback
from pathlib import Path
from typing import Union

from src.app_definitions import PACKAGE_SOURCE_DIR, ROOT_DIR
from src.infrastructure.config.global_config.schemas import GlobalConfiguration

__all__ = [
    "GlobalConfigurationManager"
]


class GlobalConfigurationManager:
    _global_configuration_filename = "global_configuration.json"

    def __init__(
            self,
            *,
            config_sub_directory_name: Union[str, Path] = ROOT_DIR
    ) -> None:
        self.config_sub_directory: Union[str, Path] = Path(config_sub_directory_name)
        self.configuration: GlobalConfiguration = self.get_configuration()

    @property
    def global_config_directory(self) -> Path:
        return PACKAGE_SOURCE_DIR.joinpath(Path(self.config_sub_directory))

    @property
    def global_config_path(self) -> Path:
        config_filename = self.__class__._global_configuration_filename
        return self.global_config_directory.joinpath(config_filename)

    @staticmethod
    def read_config_file(path: Path) -> dict:
        try:
            with open(path, 'r') as file:
                data: dict = json.load(file)
            return data
        except Exception:
            print(
                f"""
                Failed to read configurations settings for [{path}]. 
                See the stack trace bellow for details. >>>>>>>>>>>>
                >> {traceback.format_exc()}
                """
            )
            raise

    def get_configuration(self) -> GlobalConfiguration:
        data = self.read_config_file(Path(self.global_config_path))
        return GlobalConfiguration.parse_obj(data)
