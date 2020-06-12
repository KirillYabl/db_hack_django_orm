from datacenter.models import Schoolkid, Subject, Lesson, Mark, Chastisement, Commendation
from django.http import Http404

import random

COMMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
]


def find_schoolkid(schoolkid_name):
    """Find a schoolkid by the full name."""
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        raise Http404(f'More than one schoolkid found with name {schoolkid_name}')
    except Schoolkid.DoesNotExist:
        raise Http404(f'No schoolkids found with the name {schoolkid_name}')


def fix_marks(schoolkid):
    """Correct the grade for a particular schoolkid."""
    schoolkid_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])

    for mark in schoolkid_bad_marks:
        mark.points = random.choice([4, 5])
        mark.save()


def remove_chastisements(schoolkid):
    """Remove all chastisements from teachers."""
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisements.delete()


def create_commendation(schoolkid_name, subject_name):
    """Create a record with commendation for a specific subject to the schoolkid.

    This function uses ".order_by('?').first()" to get a random record.
    In this case, this is normal, because schoolkids haven few lessons.
    Using ".values_list('pk)" and ".get(pk=pk)" showed a decrease in performance.
    """
    schoolkid = find_schoolkid(schoolkid_name=schoolkid_name)
    try:
        subject = Subject.objects.get(title=subject_name, year_of_study=schoolkid.year_of_study)
    except Subject.DoesNotExist:
        raise Http404(f'No subjects found with the name {subject_name}')
    good_lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                        group_letter=schoolkid.group_letter,
                                        subject=subject) \
        .order_by('?').first()
    commendation = random.choice(COMMENDATIONS)
    Commendation.objects.create(text=commendation,
                                created=good_lesson.date,
                                schoolkid=schoolkid,
                                subject=subject,
                                teacher=good_lesson.teacher)
