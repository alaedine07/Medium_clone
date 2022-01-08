# from usermanagment.models import Users
# from django.conf import settings

# requires to define two functions authenticate and get_user

# class MyCustomAuth:

#     def authenticate(self, username=None, password=None):
#         try:
#             user = Users.objects.get(username=username, password=password)
#             return user
#         except Users.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return Users.objects.get(pk=user_id)
#         except Users.DoesNotExist:
#             return None