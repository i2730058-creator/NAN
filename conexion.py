import os
from dotenv import load_dotenv
from supabase import create_client 

class conexionDB:
    def __init__(self):
        load_dotenv()

    def conexionsupabase(self):
        url = os.getenv("SUPABASE_URL")
        api_key = os.getenv("SUPABASE_API_KEY")

        if not url or not api_key:
            raise Exception(
                "Faltan credenciales de Supabase. "
                "Revisa el archivo .env"
            )

        return create_client(url, api_key)
