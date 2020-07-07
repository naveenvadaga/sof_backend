from typing import List

from questions.storages.storage import Storage


class InvalidQuestionTitleException(Exception):
    pass


class InvalidQuestionBodyException(Exception):
    pass


class QuestionTagsExceededLimitException(Exception):
    pass


class UserReputationIsLessThan1500Exception(Exception):
    pass


class CreateQuestion:

    def __init__(self, storage: Storage):
        self.storage = storage

    def create_question(
            self, user_id: str, question_details: dict):
        """

        :param user_id:str
        :param question_details:{
            "title": str
            "body": str
            "tags": List[str]

        }
        :return:
        """

        self._validate(question_details)
        self._create_tags_if_any(
            user_id, question_details['tags'])
        self._post_question(user_id, question_details)

    def _post_question(self, user_id, question_details):
        self.storage.create_question(
            user_id, question_details)

    def _create_tags_if_any(
            self, user_id, tags: List[str]):
        non_existing_tags = self.storage.get_non_existing_tags(
            tags)

        if len(non_existing_tags) > 0:
            user_reputation = self.storage.get_user_reputation(
                user_id)
            if user_reputation > 1500:
                self.storage.create_tags(
                    non_existing_tags)
            else:
                raise UserReputationIsLessThan1500Exception()

    @staticmethod
    def _validate(question_details: dict):
        if not isinstance(question_details['title'], str) and \
                question_details['title']:
            raise InvalidQuestionTitleException()
        if not isinstance(question_details['body'], str) and \
                question_details['body']:
            raise InvalidQuestionBodyException()

        if len(question_details['tags']) > 5:
            raise QuestionTagsExceededLimitException()
