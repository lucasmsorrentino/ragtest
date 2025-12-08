import requests
import os
import time

BASE_URL = "http://127.0.0.1:8000"
API_V1 = f"{BASE_URL}/api/v1"

def create_dummy_pdf(filename="test.pdf"):
    from reportlab.pdfgen import canvas
    c = canvas.Canvas(filename)
    c.drawString(100, 750, "This is a test PDF document about Artificial Intelligence.")
    c.drawString(100, 730, "AI is transforming the world with agents like IAA.")
    c.save()
    return filename

def wait_for_server(max_retries=30, initial_delay=2):
    """
    Wait for the server to be ready with exponential backoff.
    On first run, model downloads can take time.
    """
    print(f"Waiting for server at {BASE_URL}/ ...")
    
    delay = initial_delay
    for attempt in range(max_retries):
        try:
            response = requests.get(f"{BASE_URL}/", timeout=5)
            if response.status_code == 200:
                print(f"✅ Server is ready! (attempt {attempt + 1})")
                return True
        except (requests.ConnectionError, requests.Timeout) as e:
            if attempt < max_retries - 1:
                print(f"⏳ Server not ready yet, waiting {delay}s... (attempt {attempt + 1}/{max_retries})")
                time.sleep(delay)
                delay = min(delay * 1.5, 10)  # Exponential backoff, max 10s
            else:
                print(f"❌ Server failed to start after {max_retries} attempts")
                return False
    
    return False

def test_health():
    print(f"\nTesting Health Check at {BASE_URL}/ ...")
    try:
        response = requests.get(f"{BASE_URL}/")
        assert response.status_code == 200
        print("✅ Health Check Passed:", response.json())
    except Exception as e:
        print("❌ Health Check Failed:", e)
        return False
    return True

def test_upload(filename):
    print(f"\nTesting Document Upload at {API_V1}/upload ...")
    with open(filename, "rb") as f:
        files = {"file": (filename, f, "application/pdf")}
        response = requests.post(f"{API_V1}/upload", files=files)
    
    if response.status_code == 200:
        print("✅ Upload Passed:", response.json())
        return True
    else:
        print("❌ Upload Failed:", response.text)
        return False

def test_chat():
    print(f"\nTesting Chat at {API_V1}/chat ...")
    payload = {
        "message": "What is this document about?",
        "session_id": "default"
    }
    response = requests.post(f"{API_V1}/chat", json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("✅ Chat Passed!")
        print("Answer:", data.get("answer"))
        return True
    else:
        print("❌ Chat Failed:", response.text)
        return False

def main():
    # First, wait for server to be ready
    if not wait_for_server():
        print("\n❌ Server is not available. Please start the server first:")
        print("   python src/main.py")
        return
    
    if not test_health():
        return

    pdf_file = "test_verification.pdf"
    create_dummy_pdf(pdf_file)
    
    try:
        if test_upload(pdf_file):
            # Give Milvus/Index a brief moment if needed (usually synchronous though)
            test_chat()
    finally:
        if os.path.exists(pdf_file):
            os.remove(pdf_file)

if __name__ == "__main__":
    # Ensure reportlab is installed or just write a simple text file if pdf not required
    # Since the engine expects PDF, we need a valid PDF. 
    # Attempting to use reportlab implies it's installed. 
    # If not, we'll try to find an existing PDF or fail gracefully.
    try:
        import reportlab
        main()
    except ImportError:
        print("Installing reportlab for PDF generation...")
        os.system("pip install reportlab")
        main()
