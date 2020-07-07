from questions.storages.storage import Storage


class InvalidOffsetOrLimitException(Exception):
    pass


class GetQuestions:

    def __init__(self, storage: Storage):
        self.storage = Storage

    def get_questions(self, offset, limit):
        """
        :param offset:
        :param limit:
        :return:
        """
        self.validate(offset, limit)
        self.retrieve_questions(offset, limit)

    @staticmethod
    def validate(offset, limit):
        if not isinstance(offset, int) or not isinstance(limit, int):
            raise InvalidOffsetOrLimitException

    def retrieve_questions(self, offset, limit):


