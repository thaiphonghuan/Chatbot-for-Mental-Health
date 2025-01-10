# Sample of start ngrok
import threading
from pyngrok import ngrok

ngrok.set_auth_token('set your token here')

def run_streamlit():
    !streamlit run app.py --server.port 8514

def start_ngrok():
    public_url = ngrok.connect(8514)
    print(f"Public URL: {public_url}")

threading.Thread(target=run_streamlit).start()
start_ngrok()
