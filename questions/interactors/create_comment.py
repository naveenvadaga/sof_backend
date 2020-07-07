from questions.storages.storage import Storage


class InvalidCommentException:
    pass


class CreateComment:

    def __init__(self, storage: Storage):
        self.storage = Storage

    def create_comment(
            self, user_id, question_id, answer_id, comment):
        """
        :param user_id:str
        :param question_id:str
        :param answer_id:str
        :param comment:str
        :return:
        """
        self.validate(comment)
        self.post_comment(user_id, question_id, answer_id, comment)

    def post_comment(
            self, user_id, question_id, answer_id, comment):
        self.storage.create_comment(
            user_id, question_id, answer_id, comment
        )

    @staticmethod
    def validate(comment):
        if not isinstance(comment, str):
            raise InvalidCommentException
