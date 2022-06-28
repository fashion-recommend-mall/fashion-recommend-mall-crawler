# **Fashion Recommend Mall Crawler**

![twitter_header_photo_2](https://user-images.githubusercontent.com/66009926/176111438-92f1352f-c063-4e5e-a715-f8ef3cbe0757.png)

## Project Description

This program crawls fashion items from the four sites.

First, get the items introduction page.

Second, go to each item page and crawl the title, image, reviews, and price using celery

Third, categorize image style using fashion recommend mall deep learning server

After all, save all data in the Mongo DB atlas

| 키작녀 | 키작남 | 소녀나라 | 고고싱 |
| --- | --- | --- | --- |
| <img src= "https://user-images.githubusercontent.com/66009926/176109884-399077e1-59e4-49de-9ceb-48e8f11c2cec.png" width = "70%"> |  <img src= "https://user-images.githubusercontent.com/66009926/176110089-75ed3a5c-e411-462d-a263-0088ae8e4532.png" width = "100%"> |  <img src= "https://user-images.githubusercontent.com/66009926/176109979-5bdda760-1d41-4294-b593-aee48938b020.png" width = "100%">|  <img src= "https://user-images.githubusercontent.com/66009926/176110179-392f0aef-6907-403d-8861-140c014481a0.png" width = "100%"> |

## Final data form

```json
{
  "site" : crawling site,
  "category" : item category(top, pants ...),
  "title" : item title,
  "image_link" : item image link,
  "price" : item price,
  "reviews" : item review kewords(list[str]),
  "style" : item stytle(first, second)
}
```

---
## System Structure


![Slide1_3](https://user-images.githubusercontent.com/66009926/176109459-888fb886-e5b7-4046-b608-9270d4a24822.jpg)

---
## Folder Structure

![Untitled](https://user-images.githubusercontent.com/66009926/176109515-8451c6c7-7d82-4829-91ff-58c2706aad6f.png)

---
## How to run


### Requirement

```
Docker : 20.10.16
```

### Project Setting

```python
# First, Set like below in project_setting.py

url_setting = {
    "mongo_db_url" : "mongo db atlas url",
    "selenium_url" : "driver path",
    "deep_learning_server_url" : "deep learning server url"
}

tool_setting = {
    "database_driver" : MongodbContextManager,
    "web_driver" : SeleniumContextManager
}

celery_broker_url = {
    "celery_broker_url" : "celery broker url"
}

```

### Build Setup

```
// setting celery worker
$ sudo git clone {this repo}
$ sudo docker build -t crawler .
$ sudo docker run -d crawler

// run app.py
python3 app.py
```

---
## What I learn


### Celery

![image](http://user-images.githubusercontent.com/66009926/176109791-6ebb5922-cb05-43ad-b6bb-36b66b5d9528.png)

Celery is an asynchronous task queue and multi-task processing method of queuing a series of tasks. Celery is often used when converting and storing files on a synchronously performed web or performing heavy tasks such as file uploads.

### F**eatures**

1. Asynchronous task queue, capable of scheduling but focused on real-time processing.
2. Synchronous/Asynchronous processing is possible.
3. The unit of work is called Task, and the worker is called Worker.
4. Use a message broker like RabbitMQ, or Redis.

### How to install

```bash
pip3 install celery
```

### How to run

```bash
celery -A tasks worker -l INFO
```

### First step

```python
"""
This code is default using of celery
"""
import time
import random

import celery

# Set celery like blew
app = celery.Celery{
	'tasks',
	broker='pyamqp://broker-url',
	backend='pyamqp://backend-url'
}

# Add anotation app.task
@app.task
def build_server():
		print('wait 10 sec')
		time.sleep(10)
		server_id = random.randit(1,10)
		return server_id
```

### Group

```python
"""
Group handles celery tasks by grouping
"""
@app.task
def build_servers():
		# call celery group and set tasks parameter
		g = celery.group(
				build_server.s() for _ in range(10))
		return g()
```

### Chord

```python
"""
Chord runs a callback task after all group tasks done
"""
@app.task
def callback(result):
		for server_id in result:
				print(server_id)
		print("done")
		return "done"

@app.task
def build_server_with_callback():
		c = celery.chord(
				# run group task
				build_server.s() for _ in range(10),
				# After group task, run callbak
				callback.s()
		)
		return c()
```

### Chain

```python
"""
Chain connects each task.
"""
@app.task
def setup_dns(server_id):
		print(server_id)
		return "done"

@app.task
def deploy_costomer_server():
		chain = build.server.s() | setup_dns.s()
		return chain()
```


### Chord vs Chain

**Chord is connecting Goup and Callback. However Chain is connecting each tasks!**

**Chord performs a synchronization to connect Group and Callback. this process uses a lot of resource.**

**So use chains instead of chords as possible**
