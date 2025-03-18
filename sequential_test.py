import http.client

def test_sequential_requests():
    conn = http.client.HTTPConnection("localhost", 8000)

    # Sequentially hit the server 10,000 times
    for i in range(10000):
        conn.request("GET", "/")
        response = conn.getresponse()
        print(f"Request {i + 1}: {response.read().decode()}")

    # After hitting all 10,000 requests, hit one more and print the output
    conn.request("GET", "/")
    response = conn.getresponse()
    print("Final Request Response:", response.read().decode())

    conn.close()

if __name__ == "__main__":
    test_sequential_requests()
