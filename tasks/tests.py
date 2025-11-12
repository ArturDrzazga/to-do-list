from django.test import TestCase

from .models import Task, Tag


# Create your tests here.
class ModelTests(TestCase):
    def test_task_str(self):
        task = Task.objects.create(
            content="test"
        )
        self.assertEqual(str(task), task.content)

    def test_tag_str(self):
        tag = Tag.objects.create(name="test")
        self.assertEqual(str(tag), tag.name)