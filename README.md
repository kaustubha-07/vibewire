# VibeWire - A Twitter-Like Social Media App

## 🚀 Introduction
VibeWire is a **full-stack Django-based social media application** similar to Twitter, where users can create, edit, and delete tweets containing **text and images**. The platform includes user authentication, admin control, and role-based permissions.

---

## ✨ Features
- 📝 **Tweet Creation**: Users can create tweets with text and images.
- 👥 **User Authentication**: Secure **sign-up, login, and logout** functionality.
- 🔐 **Role-Based Permissions**:
  - **New Users**: Can view tweets but cannot modify them.
  - **Tweet Owners**: Can edit or delete their own tweets.
  - **Admin**: Has full control over all tweets and users.
- 🏛️ **Admin Panel**: The admin can manage users and tweets.
- 🖼️ **Image Upload Support**: Users can attach images to their tweets.
- 📢 **Responsive UI**: A clean and user-friendly interface for easy navigation.

---

## 🛠️ Tech Stack
- **Backend**: Django, Django REST Framework (DRF)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (default)
- **Authentication**: Django Authentication System
- **Deployment**: Hosted on Heroku / Render / AWS (optional)

---

## 🎮 Installation & Setup
### 🔹 Prerequisites
Make sure you have the following installed:
- Python (>=3.8)
- Django (>=4.0)
- Virtualenv
- Git

### 🔹 Clone the Repository
```sh
git clone https://github.com/kaustubha-07/vibewire.git
cd vibewire
```

### 🔹 Create & Activate Virtual Environment
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # On MacOS/Linux
venv\Scripts\activate  # On Windows
```

### 🔹 Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔹 Apply Migrations
```sh
python manage.py migrate
```

### 🔹 Run the Development Server
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔑 User Roles & Permissions
| Role  | Actions |
|-------|---------|
| Guest | View tweets |
| Registered User | Create, Edit, Delete own tweets |
| Admin | Manage all users and tweets |

---

## 📜 License
This project is **open-source** and available under the [MIT License](LICENSE).

---

## 📩 Contact
For queries or contributions, contact:
- **GitHub**: [@kaustubha-07](https://github.com/kaustubha-07)
- **Email**: kskaustubha@gmail.com

---

🚀 **Enjoy using VibeWire!** 🎉
