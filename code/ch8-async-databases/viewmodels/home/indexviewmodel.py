from typing import List

from starlette.requests import Request

from data.package import Package
from services import package_service, user_service
from viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.release_count: int = 0
        self.user_count: int = 0
        self.package_count: int = 0
        self.packages: List[Package] = []

    async def load(self):
        self.release_count: int = await package_service.release_count()
        self.user_count: int = await user_service.user_count()
        self.package_count: int = await package_service.package_count()
        self.packages = await package_service.latest_packages(limit=7)
