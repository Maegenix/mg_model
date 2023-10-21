from mongoengine import Document, StringField, DateTimeField, BooleanField
from django.utils import timezone
from django.contrib.auth.hashers import check_password, make_password
import time
import uuid
from mg_model.Exceptions import (
    ExistingUser,
    UserNotFound,
    InvalidPassword,
    InvalidUsername,
)
from mg_model.Validators import ValidateNewUser, UsernameValidator


class User(Document):
    email = StringField(max_length=99)
    password = StringField(max_length=99)
    username = StringField(max_length=99)
    reference = StringField(default=f"User/{uuid.uuid4()}")
    is_authenticated = BooleanField(default=True)
    last_login = DateTimeField(default=time.time(), verbose_name="last login")
    date_joined = DateTimeField(default=time.time(), verbose_name="date joined")

    def set_password(self, raw_password):
        """
        Sets the user's password - always use this rather than directly
        assigning to :attr:`~mongoengine.django.auth.User.password` as the
        password is hashed before storage.
        """
        self.password = make_password(raw_password)
        self.save()
        return self

    def check_password(self, raw_password):
        """
        Checks the user's password against a provided password - always use
        this rather than directly comparing to
        :attr:`~mongoengine.django.auth.User.password` as the password is
        hashed before storage.
        """
        return check_password(raw_password, self.password)

    def create(self, **creds):
        email = self.email
        password = self.password
        now = time.time()
        try:
            ValidateNewUser(email, password)
            # Check for existing user with provided email
            User.objects.get(email=email)

            raise ExistingUser("Email exists")
        except InvalidPassword as e:
            raise InvalidPassword(e) from e
        except InvalidUsername as e:
            raise InvalidPassword(e) from e
        except User.DoesNotExist:
            # Normalize the address by lowercasing the domain part of the email
            # address.
            email_name, domain_part = email.strip().split("@", 1)
            email = "@".join([email_name.lower(), domain_part.lower()])

            user = User(email=email, date_joined=now)
            user.set_password(password)
            user.save()
            return user

    def set_name(self, username):
        UsernameValidator().validate(username)
        self.username = username
        self.save()
        # entity = Entity(name=username)
        # entity.save()

    def login(**creds):
        username = creds["username"]
        password = creds["password"]
        # Find attempting user
        try:
            user = User.objects.get(username=username)

            # Authenticate password
            if user.check_password(password):
                # Update last login date to now
                user.update(last_login=time.time())
                return user
            else:
                raise InvalidPassword("Incorrect username/password.")

        # Incorrect Username
        except User.DoesNotExist as e:
            raise UserNotFound("User not found") from e
