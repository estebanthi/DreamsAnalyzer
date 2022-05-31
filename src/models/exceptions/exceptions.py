class DreamManagerDataMissing(BaseException):
    def __init__(self):
        super().__init__(f"Can not load Dream Manager JSON file")


class DreamManagerWrongCredentials(BaseException):
    def __init__(self):
        super().__init__("Vos identifiants Dream Manager sont incorrects")


class DreamManagerDataError(BaseException):
    def __init__(self):
        super().__init__("Erreur lors de la réception des données")


class EmptyDreamJournal(BaseException):
    def __init__(self):
        super().__init__("Votre journal de rêves est vide")
