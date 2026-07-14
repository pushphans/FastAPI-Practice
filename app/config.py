from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SUPABASE_ANON_KEY: str
    SUPABASE_SERVICE_ROLE_KEY: str
    SUPABASE_JWT_SECRET: str
    # Optional: for any other secrets
    SECRET_KEY: str = "CHANGE_ME_TO_A_RANDOM_SECRET"  # For any internal use, e.g., session if needed

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()