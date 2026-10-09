class Singleton:

    _instance = None
    _v = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def getValue(self) -> str:
        return self._v

    def setValue(self, value: str):
        self._v = value