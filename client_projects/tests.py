from django.test import TestCase
from client_projects.models import ClientProject, Requirements, ProjectFiles

# Create your tests here.

class TestModels(TestCase):

    def Setup(self):
        self.project1 = ClientProject.objects.create(
            client=User.objects.create_user(username='test_user1', password='test_password1'),
            name='project 1',
            Summary='test_summary1',
            due_date='2020-01-01',
        )
    
    def test_project_is_assigned_slug_on_creation(self):
        self.assertEqual(self.project1.slug, 'project-1')
