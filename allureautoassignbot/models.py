from utils.model_validator import CustomBaseModel


class StartLaunchProcessingData(CustomBaseModel):
    id: int
    project_id: int
    name: str
    exclude_users: list[str] = []
