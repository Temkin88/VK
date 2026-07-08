import pathlib  # noqa: D100

from yaml import safe_load

from utils.config.model import ConfigModel

root = pathlib.Path()
config_file = root.joinpath("config.yaml")


with config_file.open(mode="r") as f:
    configuration = safe_load(f)

ConfigModel.parse_obj(configuration)
