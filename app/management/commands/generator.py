from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile, Question, Answer, Tag, LikeQuestion, LikeAnswer
from random import choice, sample, randint
from faker import Faker

f = Faker()


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('--auto', nargs='+', type=int)
        parser.add_argument('--users', nargs='+', type=int)
        parser.add_argument('--questions', nargs='+', type=int)
        parser.add_argument('--answers', nargs='+', type=int)
        parser.add_argument('--tags', nargs='+', type=int)
        parser.add_argument('--likes', nargs='+', type=int)

        parser.add_argument('--db_size', nargs='+', type=str)

    def handle(self, *args, **options):
        if options['auto']:
            self.fill_db(options['auto'][0])

        if options['users']:
            self.fill_profile(options['users'][0])

        if options['tags']:
            self.fill_tag(options['tags'][0])

        if options['questions']:
            self.fill_questions(options['questions'][0])

        if options['answers']:
            self.fill_answers(options['answers'][0])

        if options['likes']:
            self.fill_likes_questions(options['likes'][0])
            self.fill_likes_answers(5 * options['likes'][0])

        self.stdout.write(self.style.SUCCESS('Data creation was successful'))

    @staticmethod
    def fill_profile(cnt):
        for i in range(cnt):
            Profile.objects.create(
                user_id=User.objects.create_user(
                    username=f.user_name(),
                    email=f.email(),
                    password="1"
                ),
                avatar="static/img/avatar_" + str(i % 7) + ".jpg",
            )

    @staticmethod
    def fill_tag(cnt):
        for i in range(cnt):
            tag = f.word()
            while Tag.objects.filter(tag=tag).exists():
                tag = f.word()
            Tag.objects.create(tag=tag)

    @staticmethod
    def fill_questions(cnt):
        for profile in Profile.objects.all():
            q = Question.objects.create(
                profile_id=profile,
                title=f.sentence(),
                text=f.text(),
            )

            tag_ids = list(
                Tag.objects.values_list(
                    'tag', flat=True
                )
            )
            tags_list = sample(tag_ids, k=randint(1, 3))
            q.tags.set(Tag.objects.create_question(tags_list))

    @staticmethod
    def fill_answers(cnt):
        profile_ids = list(
            Profile.objects.values_list(
                'id', flat=True
            )
        )
        question_ids = list(
            Question.objects.values_list(
                'id', flat=True
            )
        )
        for i in range(cnt):
            Answer.objects.create(
                profile_id=Profile.objects.get(pk=choice(profile_ids)),
                question_id=Question.objects.get(pk=choice(question_ids)),
                text=f.text(),
                is_correct=f.random_int(min=0, max=1),
            )

    @staticmethod
    def fill_likes_questions(cnt):
        count = 0
        for question in Question.objects.all():
            for profile in Profile.objects.sample_profile(f.random_int(min=0, max=10)):
                LikeQuestion.objects.create(
                    question_id=question,
                    profile_id=profile,
                    is_like=f.random_int(min=0, max=1),
                )
                count += 1
                if count == cnt:
                    break
            if count == cnt:
                break

    @staticmethod
    def fill_likes_answers(cnt):
        count = 0
        for answer in Answer.objects.all():
            for profile in Profile.objects.sample_profile(f.random_int(min=0, max=15)):
                LikeAnswer.objects.create(
                    answer_id=answer,
                    profile_id=profile,
                    is_like=f.random_int(min=0, max=1),
                )
                count += 1
                if count == cnt:
                    break
            if count == cnt:
                break

    def fill_db(self, cnt):
        self.fill_profile(cnt)
        self.fill_tag(cnt // 2)
        self.fill_questions(3 * cnt)
        self.fill_answers(10 * cnt)
        self.fill_likes_questions(5 * cnt)
        self.fill_likes_answers(20 * cnt)
