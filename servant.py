class Servant:
    def __init__(self, name, short_desc, long_desc):
        self._name = name
        self._long_desc = long_desc
        self._short_desc = short_desc
        self._opposed = None

    def __str__(self):
        return self._name

    @property
    def name(self) -> str:
        return self._name

    @property
    def short_desc(self) -> str:
        return self._short_desc

    @property
    def long_desc(self) -> str:
        return self._long_desc

    @property
    def opposed(self) -> "Servant":
        return self._opposed
