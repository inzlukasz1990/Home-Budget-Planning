# Home Budget Planning

A Django-based web application to manage and track personal finances.

## Features

- User registration and authentication
- Record receipts and expenses
- Categorize receipts and expenses
- Recurring expenses
- Monthly balance summary
- Category-wise expense charts
- Administrator management of categories

## Installation

1. Clone the repository:


```
git clone git@github.com:inzlukasz1990/Home-Budget-Planning.git
```

2. Create a virtual environment and activate it:


```
python -m venv env
source env/bin/activate # For Windows, use env\Scripts\activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the project's root directory and add the following settings:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=.localhost, 127.0.0.1
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=your-email-host
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email-address
EMAIL_HOST_PASSWORD=your-email-password
```

Replace `your-secret-key`, `your-email-host`, `your-email-address`, and `your-email-password` with the appropriate values.

5. Run the following commands to apply migrations and create a superuser:

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6. Start the development server:

```
python manage.py runserver
```

7. Access the application in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This README.md provides an overview of the Home Budget Planning application, its features, and instructions for installation and usage. Make sure to replace yourusername in the repository URL with your actual GitHub username.

