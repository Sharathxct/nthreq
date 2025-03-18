import http.client
import multiprocessing
import time

# Function to send a single HTTP request and print the response
def send_request(request_id):
    try:
        conn = http.client.HTTPConnection("localhost", 8000)
        conn.request("GET", "/")
        response = conn.getresponse()
        print(f"Request {request_id}: {response.read().decode()}")
        conn.close()
    except Exception as e:
        print(f"Request {request_id} failed: {e}")

# Function to continuously send requests until a limit is reached
def continuous_requests(thread_id, request_limit):
    request_id = 0
    while request_id < request_limit:
        request_id += 1
        try:
            conn = http.client.HTTPConnection("localhost", 8000)
            conn.request("GET", "/")
            response = conn.getresponse()
            response_data = response.read().decode()
            print(f"Request {request_id}: {response_data}")
            conn.close()
        except Exception as e:
            print(f"Request {request_id} failed: {e}")
        time.sleep(0.1)  # Add a small delay to prevent overwhelming the server

# Function to test parallel requests
def test_parallel_requests():
    request_limit = 10000
    
    # Using multiprocessing Pool to run processes in parallel
    with multiprocessing.Pool(processes=8) as pool:
        # Submit continuous request tasks
        pool.starmap(continuous_requests, [(i + 1, request_limit // 8) for i in range(8)])
    
    # Send a final request to get the last response
    send_request("Final")

if __name__ == "__main__":
    test_parallel_requests()

