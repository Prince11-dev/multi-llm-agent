class ProviderException(Exception):

    def __init__(
        self,
        message: str
    ):
        self.message = message
        super().__init__(
            self.message
        )


class MemoryException(Exception):

    def __init__(
        self,
        message: str
    ):
        self.message = message
        super().__init__(
            self.message
        )


class ToolException(Exception):

    def __init__(
        self,
        message: str
    ):
        self.message = message
        super().__init__(
            self.message
        )