import subprocess
import sys

def install_cvv_api():
    try:
        import cvv_api  # Sostituisci "cvv_api" con il nome del pacchetto se è diverso
        print("CVV-API è già installato.")
    except ImportError:
        print("CVV-API non è installato. Procedo con l'installazione...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "CVV-API"])

install_cvv_api()
