# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', os.getenv('SESSION_SECRET', 'dev-secret-key-change-in-production'))
    
    # Database - Use PostgreSQL on Render, SQLite locally
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
    
    # Fix for Render's PostgreSQL URL format
    if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
        DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'pool_recycle': 300,
        'pool_pre_ping': True,
    }
    
    # File uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Ensure upload folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # API Keys
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