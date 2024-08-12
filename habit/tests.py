from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestcase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='user_1@text.com',
                                        password='12345')
        self.habit = Habit.objects.create(author=self.user,
                                          location='Улица',
                                          time='18:00:00',
                                          action='Выйти на прогулку',
                                          nice_habit=False,
                                          associated_habit=None,
                                          prize='Скушать десерт',
                                          public_habit=True
                                          )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse('habit:detail', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('location'), self.habit.location
        )

    def test_habit_create(self):
        url = reverse('habit:create')
        data = {
            'author': self.user.pk,
            'location': 'Работа',
            'time': '07:00:00',
            'action': 'Придти на работу вовремя',
            'nice_habit': False,
            'prize': 'Выпить чашку кофе',
            'public_habit': True
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(), 2
        )

    def test_habit_update(self):
        url = reverse('habit:update', args=(self.habit.pk,))
        data = {
            'time': '22:00:00'
        }
        response = self.client.patch(url, data)
        result = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            result.get('location'), self.habit.location
        )

    def test_habit_list(self):
        url = reverse('habit:list')
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                'id': self.habit.pk,
                'location': self.habit.location,
                'time': self.habit.time,
                'action': self.habit.action,
                'nice_habit': self.habit.nice_habit,
                'periodicity': self.habit.periodicity,
                'prize': self.habit.prize,
                'lead_time': self.habit.lead_time,
                'public_habit': self.habit.public_habit,
                'author': self.habit.author.pk,
                'associated_habit': self.habit.associated_habit
            }
        ]
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('results'), result
        )

    def test_habit_destroy(self):
        url = reverse('habit:delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 0
        )
