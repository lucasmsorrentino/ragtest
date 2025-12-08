from pymilvus import connections, utility

def check_milvus():
    print("Connecting to Milvus...")
    try:
        connections.connect("default", host="localhost", port="19530")
        print("Connected to Milvus!")
        
        # Check health/version if possible or just list collections
        print("Milvus is reachable.")
        return True
    except Exception as e:
        print(f"Failed to connect to Milvus: {e}")
        return False

if __name__ == "__main__":
    check_milvus()
