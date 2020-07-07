from user_auth.models import UserProfile
from questions.models import QuestionTag, Tag, Question, Answer, Comment, Vote


class Storage:

    @staticmethod
    def get_non_existing_tags(tags):
        existing_question_tags = Tag. \
            objects.filter(name__in=tags)

        return list(
            set(tags) -
            set(existing_question_tags))

    @staticmethod
    def get_user_reputation(user_id):
        return UserProfile.objects.get(
            id=user_id).reputation

    @staticmethod
    def create_tags(tags):
        tag_objs = []
        for tag in tags:
            tag_objs.append(
                Tag(name=tag))

        Tag.objects.bulk_create(tag_objs)

    @staticmethod
    def is_question_valid(user_id, question_id):
        try:
            question = Question.objects.get(id=question_id)
            if question.user_id == user_id:
                return 1
            return 0
        except Exception:
            return 0

    def create_question(
            self, user_id, question_details: dict):
        """
        :param user_id: str
        :param question_details: {
            "title": str
            "body": str
            "tags": List[str]

        }
        :return:
        """
        question = Question.objects.create(
            user_id=user_id,
            title=question_details['title'],
            body=question_details['body']
        )
        question_tag_objs = []
        for tag in question_details['tags']:
            question_tag_objs.append(
                QuestionTag(
                    question=question,
                    tag_id=tag))

        QuestionTag.objects.bulk_create(
            question_tag_objs)

    @staticmethod
    def delete_question(question_id):
        question = Question.objects.get(question_id=question_id)
        question.is_question_deleted = True
        question.save()

    @staticmethod
    def create_answer(
            user_id, question_id, answer):
        Answer.objects.create(
            question_id=question_id,
            user_id=user_id,
            body=answer,
        )

    @staticmethod
    def create_comment(
            user_id, question_id, answer_id, comment):
        comment = Comment.objects.create(
            user_id=user_id,
            question_id=question_id,
            answer_id=answer_id,
            body=comment,
        )

    @staticmethod
    def create_vote(
            user_id, question_id, answer_id, comment_id, vote):
        Vote.objects.create(
            user=user_id,
            question=question_id,
            answer=answer_id,
            comment=comment_id,
            vote_type=vote,
        )



