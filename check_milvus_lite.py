try:
    from pymilvus import MilvusClient
    client = MilvusClient("./milvus_demo.db")
    print("Milvus Lite is working!")
    client.create_collection(
        collection_name="demo_collection",
        dimension=768
    )
    res = client.get_collection_stats("demo_collection")
    print(res)
except Exception as e:
    print(f"Error: {e}")
