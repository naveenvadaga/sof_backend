from typing import List

from questions.storages.storage import Storage


class InvalidOffsetOrLimitException(Exception):
    pass


class GetQuestions:

    def __init__(self, storage: Storage):
        self.storage = storage

    def get_questions(self, offset, limit):
        """
        :param offset:
        :param limit:
        :return:
        """
        self.validate(offset, limit)
        question_objs = self.retrieve_questions(
            offset, limit)
        question_ids = [
            str(each_obj.id)
            for each_obj in question_objs
        ]
        question_id_wise_tags = self.\
            get_question_id_wise_tags(
                question_ids)
        question_ids_wise_votes = self.\
            get_question_id_wise_votes(question_ids)
        question_id_wise_answer_count = self.\
            get_question_id_wise_answer_count(
                question_ids)
        user_ids = [
            str(each_obj.user_id)
            for each_obj in question_objs
        ]
        user_id_wise_user_details = self.\
            get_user_id_wise_user_details(user_ids)
        question_details = []
        for each_question_obj in question_objs:
            question_id = str(
                each_question_obj.id)
            question_details.append({
                "question_id": str(
                    each_question_obj.id),
                "question_title":
                    each_question_obj.title,
                "question_body": each_question_obj.body,
                "tags": question_id_wise_tags[
                    question_id],
                "votes": question_ids_wise_votes[
                    question_id],
                "no_of_answers": question_id_wise_answer_count[
                    question_id],
                "question_posted_at": each_question_obj.posted_at,
                "question_posted_user_name": user_id_wise_user_details[
                    each_question_obj.user_id]['user_name'],
                "question_posted_user_reputation": user_id_wise_user_details[
                    each_question_obj.user_id]['reputation']

            })

        return question_details

    def get_question_id_wise_answer_count(
            self, question_ids: List[str]):
        question_id_wise_answer_count = {}
        question_answer_objs = self.storage.\
            get_question_answer(question_ids)
        for each_obj in question_answer_objs:
            if str(each_obj['question_id']) not in \
                    question_id_wise_answer_count:
                question_id_wise_answer_count[str(
                    each_obj['question_id'])] = 1
            else:
                question_id_wise_answer_count[
                    str(each_obj['question_id'])] += 1

        return question_id_wise_answer_count



    def get_user_id_wise_user_details(self, user_ids):
        user_objs = self.storage.get_users_details(
            user_ids)
        user_id_wise_user_details = {}
        for user in user_objs:
            user_id_wise_user_details[str(user.id)] = {
                "user_name": user.first_name,
                "reputation": user.reputation
            }

        return user_id_wise_user_details

    def get_question_id_wise_votes(
            self, question_ids: List[str]):
        question_vote_objs = self.storage.\
            get_question_votes(question_ids)
        question_id_wise_votes = {}
        for question_vote_obj in question_vote_objs:
            question_id = str(question_vote_obj.id)
            vote = question_vote_obj.vote_type
            if question_id not in question_id_wise_votes:
                question_id_wise_votes[question_id] = 1 \
                    if vote == "UPVOTE" else -1
            else:
                question_id_wise_votes[question_id] += 1 \
                    if vote == "UPVOTE" else -1

        return question_id_wise_votes

    def get_question_id_wise_tags(
            self, question_ids: List[str]):
        question_tags = self.storage.get_question_tags(
            question_ids)
        question_id_wise_tags = {}
        for each_question_tag in question_tags:
            question_id = str(each_question_tag.question_id)
            tag = each_question_tag.tag

            if question_id not in question_id_wise_tags:
                question_id_wise_tags[question_id] = [
                    tag]
            else:
                question_id_wise_tags[question_id].append(
                    tag)

        return question_id_wise_tags

    @staticmethod
    def validate(offset, limit):
        if not isinstance(offset, int) or not isinstance(limit, int):
            raise InvalidOffsetOrLimitException

    def retrieve_questions(self, offset, limit):
        question_objs = self.storage.get_questions(
            offset, limit)
        return question_objs


