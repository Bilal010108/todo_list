from .models import Task
from modeltranslation.translator import TranslationOptions,register



@register(Task)
class TaskTranslationOptions(TranslationOptions):
    fields = ('task', 'description')