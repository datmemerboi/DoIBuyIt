class FailedBuildFetchError(Exception):
    message: str = "Failed to fetch build ID"

    def __init__(self, message: str | None = None):
        if message:
            self.message = message
        super().__init__(self.message)


class UnableToInitSpiderError(Exception):
    message: str = "Unable to initialize spider"

    def __init__(self, message: str | None = None, vendor: str | None = None):
        if vendor:
            self.message = f"Unable to initialize spider for vendor: {vendor} vendor"
        if message:
            self.message = message
        super().__init__(self.message)


class FailedCategoryFetchError(Exception):
    message: str = "Failed to fetch category data"

    def __init__(self, message: str | None = None, vendor: str | None = None, category: str | None = None):
        if vendor and category:
            self.message = f"Failed to fetch category data for category: {category}, vendor: {vendor}"
        if message:
            self.message = message
        super().__init__(self.message)


class EmptyCategoryDataError(Exception):
    message: str = "No data found for category"

    def __init__(self, message: str | None = None, vendor: str | None = None, category: str | None = None):
        if vendor and category:
            self.message = f"No data found for category: {category}, vendor: {vendor}"
        if message:
            self.message = message
        super().__init__(self.message)
