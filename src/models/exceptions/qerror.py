from models.ui.popups.qerror_popup import QErrorPopup


class QError(BaseException):

    def __init__(self, text):
        qerror_popup = QErrorPopup(text)
        super().__init__(text)
