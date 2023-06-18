from datetime import date
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Booking
from users.models import CustomUser
from rooms.models import Room


class TestViews(TestCase):
    """Tests for booking app views"""
    def setUp(self):
        # create test user
        email = "testuser@test.ie"
        password = "test123456"
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            email=email, password=password
        )
        logged_in = self.client.login(email=email, password=password)
        self.assertTrue(logged_in)
    
        # create test room
        self.room = Room.objects.create(
            name='Test Room',
            room_no='0',
            view_type='ocean',
            capacity='3',
            description='Test room for testing',
            image='https://res.cloudinary.com/dml1pgzdn/image/upload/v1/media/rooms/istockphoto-1368436973-170667a_oyfhyv',
            image_alt='test room img'
        )