import datetime
from typing import Optional

from data.package import Package
from data.release import Release


def release_count() -> int:
    return 2_234_847


def package_count() -> int:
    return 274_000


def latest_packages(limit: int = 5) -> list:
    return [
        {'id': 'fastapi', 'summary': "A great web framework"},
        {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
        {'id': 'httpx', 'summary': "Requests for an async world"},
    ][:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name, "This is summary", "Full details is here",
        "fastapi.com", "MIT", "Ramirez"
    )
    return package


def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    return Release("1.2.3", datetime.datetime.now())