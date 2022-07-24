from datetime import datetime
from django.test import TestCase
from client_projects.models import ClientProject, Requirements, ProjectFiles
from django.contrib.auth.models import User

# Create your tests here.


class TestModels(TestCase):

    def setUp(self):
        self.client = User.objects.create_user(
            username='test_user1', password='test_password1')
        self.client_project = ClientProject.objects.create(
            client=self.client,
            name='project 1',
            Summary='test_summary1',
            due_date='2023-01-01'
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEqual(self.client_project.slug, 'project-1')

    def test_project_is_assigned_random_id_on_creation(self):
        self.assertEqual(len(self.client_project.project_id), 32)

    def test_time_of_creation_is_saved(self):
        self.assertTrue(self.client_project.created_at)
