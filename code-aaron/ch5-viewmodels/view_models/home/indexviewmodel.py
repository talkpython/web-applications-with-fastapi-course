from view_models.shared.viewmodel import ViewModelBase
from typing import Optional, List
from fastapi.requests import Request
from services import package_service


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request, user: str = "guest"):
        super().__init__(request)
        self.user = user
        self.package_count = package_service.package_count()
        self.release_count = package_service.release_count()
        self.user_count = package_service.user_count()
        self.packages: List = package_service.latest_packages(limit=5)
