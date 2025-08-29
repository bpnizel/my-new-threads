import threading
import time
import requests
import random

def downloader(url: str, thread_index: int, returns: list):
    sleep_second = random.randint(0, 8)
    time.sleep(sleep_second)
    requests.get(url).json()
    print(str(thread_index) + ". thread: " + url + ", slept " + str(sleep_second) + " seconds")
    returns.append(sleep_second)



def main():
    urls = [ 'https://jsonplaceholder.typicode.com/posts',        
    'https://jsonplaceholder.typicode.com/comments',     
    'https://jsonplaceholder.typicode.com/albums',       
    'https://jsonplaceholder.typicode.com/photos',       
    'https://jsonplaceholder.typicode.com/todos',        
    'https://jsonplaceholder.typicode.com/users'      
 ]

    threads_returns = []
    thread_list = []
    for i, url in enumerate(urls):
       thread = threading.Thread(target=downloader,args=(url, i, threads_returns, ))
       thread.start()
       thread_list.append(thread)
    
    for thread in thread_list:
        thread.join()
    print(threads_returns) 

    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time() 
    print("Total time:" + str(end - start))
