from questions.storages.storage import Storage


class InvalidAnswerException(Exception):
    pass


class CreateAnswer:

    def __init__(self, storage: Storage):
        self.storage = storage

    def create_answer(
            self, user_id: str, question_id: str, answer: str):
        """
        :param user_id:str
        :param question_id:str
        :param answer:str
        :return:
        """
        self._validate(answer)
        self._post_answer(user_id, question_id, answer)

    def _post_answer(self, user_id, question_id, answer):
        self.storage.create_answer(
            user_id, question_id, answer)

    @staticmethod
    def _validate(answer: str):
        if not isinstance(answer, str):
            raise InvalidAnswerException
