from models.bbcode.bbcode_tag import BBCodeTag


class BBCodeColorTag(BBCodeTag):

    def __init__(self, color):
        super().__init__('color', color)


class BBCodeItalicTag(BBCodeTag):

    def __init__(self):
        super().__init__('i')


class BBCodeBoldTag(BBCodeTag):

    def __init__(self):
        super().__init__('b')
