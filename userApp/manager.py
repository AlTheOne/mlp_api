from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login, email, phone, password, **extra_fields):
        if not email:
            raise ValueError("User must have an email address.")
        if not phone:
            raise ValueError("User must have a phone number.")

        user = self.model(
            login=login,
            email=self.normalize_email(email),
            phone=phone,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, email, phone, password, **extra_fields)

    def create_superuser(self, login, email, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        is_superuser = extra_fields.setdefault('is_superuser', True)

        if is_superuser is not True:
            raise ValueError("Superuser must have 'is_superuser = True'")

        return self._create_user(login, email, phone, password, **extra_fields)
