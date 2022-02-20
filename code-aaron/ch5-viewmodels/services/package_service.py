from typing import List, Optional
from data.package import Package
from data.release import Release
import datetime


def release_count() -> int:
    return 1


def package_count() -> int:
    return 2


def user_count() -> int:
    return 3


def latest_packages(limit: int = 5) -> List:
    return [
        {"id": "fastapi", "summary": "A great web framework"},
        {"id": "uvicorn", "summary": "Your favourite ASGI server"},
        {"id": "httpx", "summary": "Requests fro an async world"},
    ][:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        "fake_news",
        "I am not Donald Trump",
        "Long Live America",
        "www.wikipedia.com",
        "MIT license",
        "Aaron Teo",
        [],
    )
    return package


def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    return Release(version="1.0.0", created_date=datetime.datetime.now())
