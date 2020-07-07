from questions.storages.storage import Storage


class DeleteQuestion:

    def __init__(self, storage: Storage):
        self.storage = storage

    def _delete_question(
            self, user_id: str, question_id: str):
        """

        :param user_id:str
        :param question_id:str
        :return:
        """
        self._delete_question_if_valid(user_id, question_id)

    def _delete_question_if_valid(self, user_id, question_id):
        if self.storage.is_question_valid(user_id, question_id):
            self.storage.delete_question(question_id)



