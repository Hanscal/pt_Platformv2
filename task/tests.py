import time
from datetime import datetime

from django.test import TestCase, Client
from user.models import UserProfile
# Create your tests here.

from user.models import UserProfile
from .models import Task, LabelClass, LabelSubClass, DataItem
from .views import DistributeTaskView, NextView, CloseTaskView, LabelView

class DataItemTestCase(TestCase):
    def setUp(self):
        user = UserProfile.objects.create(
            id=2,
            password='test1',
            last_login='2020-05-31 10:00:00',
            is_superuser=0,
            username='test1',
            first_name='1',
            last_name='test',
            email='email1',
            is_active=1,
            is_staff=1,
            date_joined='2020-06-01 11:00:00'
        )

        self.task = Task.objects.create(
            name='n_medical',
            has_finished=False,
            max_label_nums=3,
            has_distributed=False,
            creator=user
        )

    def test_dataitem(self):
        # 建立外键task
        print("任务名称为",self.task)
        dataitem = DataItem.objects.create(
            mid=2,
            img_name='bbb.jpg',
            txt='图片bbb',
            image='bbb.jpg',
            task_id=1,
            task=self.task,
            time='2020-06-01 12:00:00'
        )
        self.assertEqual(dataitem.img_name, 'bbb.jpg', 'create dataitem fail!')
        mid = 2
        data = DataItem.objects.filter(mid=mid)
        print("dataitem image name",dataitem)
        self.assertEqual(data.count(), 1, '应该只存在一个mid为{}的记录'.format(mid))

    def test_get_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200')

    def test_data_view(self):
        client = Client()
        data = dict(
            mid=2,
            img_name='bbb.jpg',
            txt='图片bbb',
            image='bbb.jpg',
            task_id=1,
            task=self.task,
            time='2020-06-01 12:00:00'
        )
        response = client.post('/admin/task/dataitem/add', data)
        self.assertEqual(response.status_code, 302)

