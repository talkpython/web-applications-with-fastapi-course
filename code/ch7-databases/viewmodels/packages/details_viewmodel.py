import datetime
from typing import List, Optional

from starlette.requests import Request

from data.release import Release
from services import package_service, user_service
from viewmodels.shared.viewmodel import ViewModelBase


class DetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str, request: Request):
        super().__init__(request)

        self.package_name = package_name
        self.package = package_service.get_package_by_id(package_name)
        self.latest_release = package_service.get_latest_release_for_package(package_name)
        self.latest_version = "0.0.0"
        self.is_latest = True
        self.maintainers = []

        if not self.package or not self.latest_release:
            return

        r = self.latest_release
        self.latest_version = f'{r.major_ver}.{r.minor_ver}.{r.build_ver}'
        self.maintainers = []

