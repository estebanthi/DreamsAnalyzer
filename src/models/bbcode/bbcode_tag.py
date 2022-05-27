from abc import ABC


class BBCodeTag(ABC):

    def __init__(self, type_, arg=None, **kwargs):
        self.type = type_
        self.arg = arg
        self.kwargs = kwargs

        self.opening = self._get_opening()
        self.closing = self._get_closing()

    def _get_opening(self):
        opening = f"[{self.type}"

        if self.arg:
            opening += f"={self.arg}"

        for k, v in self.kwargs.items():
            opening += f" {k}={v}"

        opening += ']'
        return opening

    def _get_closing(self):
        return f"[/{self.type}]"

    def __repr__(self):
        return self.opening + self.closing
