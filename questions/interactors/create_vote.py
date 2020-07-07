from questions.storages.storage import Storage


class InvalidVoteException(Exception):
    pass


class ReputationLowException(Exception):
    pass


class CreateVote:

    def __int__(self, storage: Storage):
        self.storage = Storage

    def create_vote(
            self, user_id, question_id, answer_id, comment_id, vote):
        """
        :param user_id: str
        :param question_id: str
        :param answer_id: str
        :param comment_id: str
        :param vote: str
        :return:
        """
        self.validate(vote, user_id)
        self.post_vote(user_id, question_id, answer_id, comment_id, vote)

    def validate(self, vote, user_id):
        if not isinstance(vote, str) and vote not in ("UPVOTE", "DOWNVOTE"):
            raise InvalidVoteException
        if self.storage.get_user_reputation(user_id) < 50:
            raise ReputationLowException

    def post_vote(
            self, user_id, question_id, answer_id, comment_id, vote):
        self.storage.create_vote(
            user_id, question_id, answer_id, comment_id, vote)

