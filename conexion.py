import os
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

if not SUPABASE_URL or not SUPABASE_API_KEY:
    raise Exception("Faltan credenciales de Supabase en .env")


supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)
