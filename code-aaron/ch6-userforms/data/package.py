from typing import List


class Package:
    def __init__(
        self,
        package_name: str,
        summary: str,
        description: str,
        home_page: str,
        license: str,
        author_name: str,
        maintainers: List,
    ):
        self.package_name = package_name
        self.id = package_name
        self.summary = summary
        self.description = description
        self.home_page = home_page
        self.license = license
        self.author_name = author_name
        self.maintainers = maintainers
