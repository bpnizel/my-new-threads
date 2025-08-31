import threading
import time
import requests


def downloader(url: str, thread_index: int, returns: list):
    start = time.time()
    requests.get(url).json()
    end = time.time()
    result_time = end - start
    print(str(thread_index) + ". thread: " + url + " took, " + str(result_time) + " seconds")
    returns.append(result_time)



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
    main()
    

