class DreamManagerDataMissing(BaseException):
    def __init__(self):
        super().__init__(f"Can not load Dream Manager JSON file")