from view_models.shared.viewmodel import ViewModelBase
from fastapi import Request
from services import package_service
from data.release import Release
import datetime


class DetailsViewModel(ViewModelBase):
    def __init__(self, request: Request, package_name: str):
        super().__init__(request)
        self.package_name = package_name
        self.package = package_service.get_package_by_id(package_name)
        self.latest_release = package_service.get_latest_release_for_package(
            package_name
        )
        self.is_latest = True
        if not self.package:
            return
        self.x = 9
