# Weather Application

A full-featured weather application built with Django that integrates with OpenWeatherMap API to provide real-time weather information.

## Features

- Real-time weather data from OpenWeatherMap API
- User authentication and personalized weather preferences
- Responsive and modern user interface
- Search weather by city name
- Save favorite locations
- View detailed weather information including temperature, humidity, wind speed, and more

## Prerequisites

- Python 3.8 or higher
- Django 4.2.7
- OpenWeatherMap API key

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root and add your configuration:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   OPENWEATHER_API_KEY=your-api-key-here
   DATABASE_URL=sqlite:///db.sqlite3
   ```
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## Project Structure

```
├── manage.py
├── requirements.txt
├── .env
├── README.md
├── weather_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── weather/
│   ├── migrations/
│   ├── templates/weather/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── api.py
│   └── tests.py
└── accounts/
    ├── migrations/
    ├── templates/accounts/
    ├── __init__.py
    ├── models.py
    ├── views.py
    └── urls.py
```

## Development

- The project follows Django's MVT architecture
- Frontend is built with vanilla JavaScript and modern CSS
- API calls are handled through a custom wrapper around the OpenWeatherMap API
- User authentication is managed through Django's built-in authentication system

## Testing

Run the test suite:
```
python manage.py test
```

## Deployment

The application is configured for deployment to Heroku:

1. Create a new Heroku app
2. Set environment variables in Heroku dashboard
3. Deploy using Git

## License

MIT License