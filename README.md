# Carakan.AI 
carakan.ai is an application for implementing Deep Learning with CNN
algorithm in order to classify Javanese Script called _hanacaraka._
This model only include the main script, so-called _aksara nglegena_,
which is consist of 20 single letters. Pre-trained model are avaiable
to try.

---

This web server is written in Python using Flask framework. The application
has been tested on Debian Buster only.

## Installation
There are a few methods to install this Flask server

### Using Docker
For your convenience, this repos is available on dockerhub. Just run
```bash
$ docker pull ariqfadlan:carakanai
```

If you want to build it yourself, clone this repo and run
```bash
$ docker build -f Dockerfile -t carakanai:latest .
```

To run the application, simply run
```bash
$ docker run -p 8080:8080 --rm carakanai:latest
```

It will expose the port 8080 on your localhost.

### Using pip
Clone this repo and run
```bash
$ pip install -r requirements.txt
```

Run the application by typing
```bash
$ python app.py
```

## Testing
There is a test image included to test the repo. Using `cUrl`, you could
run
```bash
$ curl -F file=@test.jpg 127.0.0.1:8080/upload
```
It should be returning a json response with key `prediction` and value `dha`.
