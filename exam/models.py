from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Level(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name


class Exam (models.Model):
    name = models.CharField(max_length=225)
    date = models.DateField()
    from_section = models.PositiveIntegerField()
    to_section = models.PositiveIntegerField()
    start_time = models.TimeField()
    level = models.ForeignKey(Level, related_name='exam_level', on_delete=models.CASCADE)
    is_start = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Section (models.Model) :
    exam = models.ForeignKey(Exam, related_name='exam_section', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name='section_level', on_delete=models.CASCADE)
    number = models.PositiveIntegerField()

    class SectionState:
        done = 'done'
        pending = 'pending'
        not_enter = 'not_enter'
    
    state = models.CharField(
        choices=(
            (SectionState.done, SectionState.done),
            (SectionState.pending, SectionState.pending),
            (SectionState.not_enter, SectionState.not_enter),
        ),
        default=SectionState.not_enter,
        max_length=20
    )

    def __str__(self) -> str:
        return f'{self.exam.name} | section : {self.number}'
    


@receiver(post_save, sender=Exam)
def create_sections (created, instance:Exam, **other):
    if not created:
        return
    
    for i in range(instance.from_section, instance.to_section+1):
        section = Section(
            number=i,
            exam=instance,
            level=instance.level
        )
        section.save()