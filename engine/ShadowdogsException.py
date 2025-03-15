class ShadowdogsException(Exception):
    def __init__(self, key: str, args: tuple[str] = None):
        super().__init__()
