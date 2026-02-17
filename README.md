# Todo List Application

A modern todo list web app with user authentication, task management, and progress tracking.

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the App

```bash
python main.py
```

### 3. Open Browser

```
http://localhost:5000
```

## Features

- ✅ User registration & secure login
- 📝 Create, complete, and delete tasks
- 📊 Real-time progress bar with percentage
- 🎨 Beautiful gradient UI with Tailwind CSS
- 📱 Fully responsive design
- 🔒 Password hashing & secure sessions

## Project Structure

```
Flask web app/
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
├── README.md               # This file
└── website/
    ├── __init__.py         # App configuration
    ├── models.py           # Database models
    ├── auth.py             # Login/Signup routes
    ├── views.py            # Task routes & logic
    ├── static/index.js     # Task interactions
    └── templates/          # HTML pages
```

## How to Use

1. **Sign Up** - Create account with email & password
2. **Add Tasks** - Type task and click "Add"
3. **Complete Tasks** - Check the checkbox to mark complete
4. **Delete Tasks** - Click trash icon to remove
5. **Track Progress** - See completion % at bottom

## Routes

| Route          | Method   | Purpose                  |
| -------------- | -------- | ------------------------ |
| `/`            | GET/POST | View & create tasks      |
| `/login`       | GET/POST | User login               |
| `/signup`      | GET/POST | Register account         |
| `/logout`      | GET      | Sign out                 |
| `/delete-note` | POST     | Delete task              |
| `/toggle-note` | POST     | Mark complete/incomplete |

## Tech Stack

- **Backend:** Flask, SQLAlchemy, Flask-Login
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Database:** SQLite
- **Security:** Werkzeug password hashing (pbkdf2:sha256)

## Troubleshooting

**Database Error?**

```bash
Remove-Item instance/database.db -Force
python main.py
```

**Port 5000 taken?**
Edit `main.py`:

```python
app.run(debug=True, port=5001)
```

**Module errors?**

```bash
pip install -r requirements.txt
```

## Important for Production

⚠️ Before deploying:

- Change `SECRET_KEY` in `website/__init__.py`
- Set `debug=False` in `main.py`
- Use environment variables for config

---

**Enjoy organizing your tasks!** 🚀
