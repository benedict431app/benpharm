# config.py
import os
from datetime import timedelta

class Config:
    # Secret Key
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
<<<<<<< HEAD
    # Database - Use PostgreSQL on Render, SQLite locally
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
    
    # Fix for Render's PostgreSQL URL format
    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
=======
    # Database Configuration
    # Get DATABASE_URL from environment
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    # Handle both SQLite (for development) and PostgreSQL (for production)
    if DATABASE_URL:
        # Fix for Render's PostgreSQL URL format
        if DATABASE_URL.startswith('postgres://'):
            DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # Fallback to SQLite for development
        SQLALCHEMY_DATABASE_URI = 'sqlite:///benpharm.db'
>>>>>>> 7241f060ad963e0b034f5b796e6a780a12f6dafe
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'pool_recycle': 300,
        'pool_pre_ping': True,
    }
    
    # Upload settings
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    
    # API Keys
<<<<<<< HEAD
    COHERE_API_KEY = os.getenv('COHERE_API_KEY', '')
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', '')
    
    # Flask configuration
    PREFERRED_URL_SCHEME = 'https' if os.environ.get('RENDER') else 'http'
    
    # Additional settings
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

# For development
class DevelopmentConfig(Config):
    DEBUG = True

# For production
class ProductionConfig(Config):
    DEBUG = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
=======
    COHERE_API_KEY = os.environ.get('COHERE_API_KEY', '')
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY', '')
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', '')
    
    # Flask-Login
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    SESSION_PROTECTION = 'strong'
    
    # Server settings
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
>>>>>>> 7241f060ad963e0b034f5b796e6a780a12f6dafe
