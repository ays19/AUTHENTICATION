# 🔐 Django Custom Authentication System

A full-featured, production-ready authentication system built with **Django 5** and **Bootstrap 5**. This project implements a complete user authentication flow using a **custom User model**, class-based views, and Django's built-in security framework — demonstrating clean architecture, reusable components, and industry best practices.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Custom User Model** | Extends `AbstractBaseUser` + `PermissionsMixin` with a dedicated `UserManager` for full control over user creation |
| **User Registration** | Sign-up with username, email, and password — includes duplicate-checking validation |
| **Login / Logout** | Session-based authentication using Django's `authenticate()` and `login()` |
| **Change Password** | Authenticated users can update their password with current-password verification |
| **Password Reset via Email** | Forgot-password flow using Django's `PasswordResetView` with SMTP email delivery |
| **Access Control Mixins** | Custom `LogoutRequiredMixin` prevents authenticated users from accessing login/register pages |
| **Responsive UI** | Bootstrap 5 RTL-ready templates with clean, mobile-friendly layouts |
| **Admin Panel** | Custom User model registered in Django Admin for easy management |

---

## 🛠️ Tech Stack

- **Backend:** Python · Django 5.0
- **Frontend:** Django Templates · Bootstrap 5.3 (RTL)
- **Database:** SQLite (default, easily swappable)
- **Authentication:** Django's built-in auth framework with custom extensions
- **Email:** SMTP (Gmail) for password-reset emails

---

## 📁 Project Structure

```
AUTHENTICATION/
└── authentication/              # Django project root
    ├── manage.py
    ├── db.sqlite3
    ├── authentication/          # Project configuration
    │   ├── settings.py          # Django settings, AUTH_USER_MODEL config
    │   ├── urls.py              # Root URL routing
    │   ├── wsgi.py
    │   └── asgi.py
    └── account/                 # Core authentication app
        ├── models.py            # Custom User model (AbstractBaseUser)
        ├── managers.py          # Custom UserManager (create_user / create_superuser)
        ├── views.py             # CBVs: Login, Logout, Registration, ChangePassword, Home
        ├── forms.py             # LoginForm, UserRegistrationForm, ChangePasswordForm
        ├── urls.py              # App-level URL patterns + password reset routes
        ├── mixins.py            # LogoutRequiredMixin
        ├── admin.py             # User model admin registration
        ├── templates/
        │   ├── base.html        # Base layout (Bootstrap 5)
        │   └── account/
        │       ├── home.html
        │       ├── login.html
        │       ├── registration.html
        │       └── change_password.html
        └── static/
            └── css/
                └── main.css
```

---

## 🏗️ Architecture & Design Decisions

### Custom User Model
Instead of relying on Django's default `User`, this project defines a custom model extending `AbstractBaseUser` and `PermissionsMixin`. This provides:
- Full control over authentication fields (`username` as the login identifier, `email` as required)
- A custom `UserManager` with explicit `create_user()` and `create_superuser()` methods
- Proper email normalization and field validation

### Class-Based Views (CBVs)
All views are implemented as class-based views for better code organization and reusability:
- `generic.View` for login (custom GET/POST handling)
- `generic.CreateView` for registration
- `generic.FormView` for password change
- `generic.TemplateView` for the home page

### Access Control
- **`LoginRequiredMixin`** — Protects authenticated-only pages (Home, Change Password)
- **`LogoutRequiredMixin`** (custom) — Redirects already-logged-in users away from Login and Registration pages

### Form Validation
All forms include server-side validation:
- Duplicate username/email detection (case-insensitive)
- Password confirmation matching
- Current password verification for password changes
- Automatic Bootstrap `form-control` class injection

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/ays19/AUTHENTICATION.git
cd AUTHENTICATION/authentication

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# Install dependencies
pip install django

# Apply migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

### Access the Application

| Page | URL |
|---|---|
| Home (protected) | `http://127.0.0.1:8000/` |
| Login | `http://127.0.0.1:8000/login/` |
| Registration | `http://127.0.0.1:8000/registration/` |
| Change Password | `http://127.0.0.1:8000/change_password/` |
| Password Reset | `http://127.0.0.1:8000/password_reset/` |
| Admin Panel | `http://127.0.0.1:8000/admin/` |

---

## 🔑 API / URL Endpoints

```
GET  /                  → Home (requires login)
GET  /login/            → Login page
POST /login/            → Authenticate user
GET  /logout/           → Logout and redirect to login
GET  /registration/     → Registration form
POST /registration/     → Create new user
GET  /change_password/  → Change password form (requires login)
POST /change_password/  → Update password
GET  /password_reset/   → Password reset request (email)
GET  /reset/<uid>/<token>/  → Password reset confirmation
```

---

## 🧩 Key Code Highlights

<details>
<summary><b>Custom User Model</b> — <code>account/models.py</code></summary>

```python
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, validators=[UnicodeUsernameValidator])
    email    = models.EmailField(max_length=150, unique=True)
    # ...
    objects  = UserManager()
    USERNAME_FIELD  = "username"
    REQUIRED_FIELDS = ["email"]
```
</details>

<details>
<summary><b>Custom UserManager</b> — <code>account/managers.py</code></summary>

```python
class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
```
</details>

<details>
<summary><b>LogoutRequiredMixin</b> — <code>account/mixins.py</code></summary>

```python
class LogoutRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(*args, **kwargs)
```
</details>

---

## 🗺️ Roadmap / Potential Enhancements

- [ ] Add JWT / Token-based authentication (Django REST Framework)
- [ ] Social login integration (Google, GitHub via `django-allauth`)
- [ ] User profile page with avatar upload
- [ ] Email verification on registration
- [ ] Rate limiting on login attempts
- [ ] Docker containerization
- [ ] Unit & integration test coverage

---

## 📄 License

This project is open source and available for learning and reference purposes.

---

<p align="center">
  Built with ❤️ using Django 5 &middot; Python 3
</p>
