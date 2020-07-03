from user_auth.models import UserProfile
from questions.models import QuestionTag, Tag, Question


class Storage:

    @staticmethod
    def get_non_existing_tags(tags):
        existing_question_tags = Tag.\
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

    def create_question(
            self, user_id, question_detaiis: dict):
        """
        :param user_id: str
        :param question_detaiis: {
            "title": str
            "body": str
            "tags": List[str]

        }
        :return:
        """
        question = Question.object.create(
            user_id=user_id,
            title=question_detaiis['title'],
            body=question_detaiis['body']
        )
        question_tag_objs = []
        for tag in question_detaiis['tags']:
            question_tag_objs.append(
                QuestionTag(
                    question=question,
                    tag_id=tag))

        QuestionTag.objects.bulk_create(
            question_tag_objs)
