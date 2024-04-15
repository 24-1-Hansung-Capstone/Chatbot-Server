#!/usr/bin/env bash

PROJECTNAME=chatbot-server
VENVNAME=capstone
REPOSITORY=/home/ubuntu/$PROJECTNAME
FLASK_APP_DIR=/home/ubuntu/$PROJECTNAME
ENV_PATH=$FLASK_APP_DIR/.env
cd $REPOSITORY

# Flask 앱 인스턴스 종료
FLASK_PID=$(pgrep -f gunicorn)
if [ -z $FLASK_PID ]
then
  echo "> 종료할 Flask 애플리케이션이 없습니다."
else
  echo "> kill Flask app with PID: $FLASK_PID"
  kill -9 $FLASK_PID
  sleep 5
fi

echo "> Removing existing venv directory"
rm -rf $FLASK_APP_DIR/$VENVNAME

echo "> Setting up new virtual environment"
pip install virtualenv
virtualenv $VENVNAME --python=python3.11.5
source $FLASK_APP_DIR/$VENVNAME/bin/activate

echo "> Installing dependencies"
pip install -r $FLASK_APP_DIR/requirements.txt

# Flask 앱 시작
echo "> Starting Flask app"
cd $FLASK_APP_DIR
source $FLASK_APP_DIR/venv/bin/activate
nohup python -m flask run > $FLASK_APP_DIR/app.log 2>&1 < /dev/null &