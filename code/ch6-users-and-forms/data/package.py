class Package:
    def __init__(
        self,
        package_name: str,
        summary: str,
        description: str,
        home_page: str,
        lic: str,
        author_name: str,
        maintainers: list = None,
    ):
        if maintainers is None:
            maintainers = []
        self.maintainers = maintainers
        self.author_name = author_name
        self.license = lic
        self.home_page = home_page
        self.description = description
        self.summary = summary
        self.package_name = package_name
        self.id = package_name
