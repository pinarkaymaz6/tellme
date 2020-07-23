# TellMe

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![HitCount](http://hits.dwyl.com/pinarkaymaz6/tellme.svg)](http://hits.dwyl.com/pinarkaymaz6/tellme)
[![GitHub last commit](https://img.shields.io/github/last-commit/pinarkaymaz6/tellme.svg?style=flat)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg?style=flat-square)](http://makeapullrequest.com)

TellMe is an anonymous Question-Answer platform where people can ask a question or submit their own answers or advices. 

Home View             |  Detail View
:-------------------------:|:-------------------------:
![](https://pinarkaymaz6.github.io/images/tellme/index.png)  |  ![](https://pinarkaymaz6.github.io/images/tellme/detail.png)

### Run locally

1. Clone the repository
    ```shell
    git clone https://github.com/pinarkaymaz6/tellme.git
    ```
2. Create a virtual environment
    ```shell
    cd tellme/
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```
3. Start the application. The application should be running at [http://127.0.0.1:8000/tellme/](http://127.0.0.1:8000/tellme/)
    ```shell
    cd webapp/
    python manage.py runserver
    ```
4. Access admin tool at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


If you want to learn more about the project, this post provides a step-by-step tutorial: [TellMe - A Simple Web Application with Django](https://pinarkaymaz6.github.io/tellme/)