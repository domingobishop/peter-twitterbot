# Twitter bot hosted on Heroku

## Getting Started

1. Download this repository. 
2. Register on [Heroku](https://www.heroku.com/).
3. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
4. Download and install [git](https://git-scm.com/downloads).
5. You may select your python version and runtime with "runtime.txt". Read how on [official heroku page](https://devcenter.heroku.com/articles/python-runtimes#selecting-a-runtime).
6. If you are using non-standart modules, you must add them to requirements.txt
   
   To check which version of module you have on your computer, run pip freeze | grep MODULE_NAME in the terminal. 
   
   You will get line MODULE_NAME==MODULE_VERSION. Add this line to "requirements.txt".
   
   You should remove any unused modules from "requirements.txt".
   
   Repeat this process for all the modules you are planning to use.
   
7. Now open terminal(or do it other way, but i will explain how to do it in terminal on Ubuntu) and create git repository.
   
   ```
   git init
   ```
   
   Create heroku app.
   
   ```
   heroku create
   ```
   
   And push your code into heroku app.
   
   ```
   git add .
   git commit -m "initial commit"
   git push heroku master
   ```

8. Run you worker with following command.
   ```
   heroku ps:scale worker=1
   ```
   
9. Now everything should be working. You can check your logs with.

   ```
   heroku logs --tail
   ```
   
10. From now on you can use usual git commands(push, add, commit etc.) to update your app.

   Everytime you push heroku master your app gets redeployed.

### Prerequisites

* [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
* [git](https://git-scm.com/downloads)

## License

This project is licensed under GNU General Public License v3.0 - see the [LICENCE.md](LICENCE.md) file for details

## Acknowledgments

* @michaelkrukov - http://michaelkrukov.ru/
* [Official guide to deploy app](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [Official guide about worker](https://devcenter.heroku.com/articles/background-jobs-queueing)
* [Guided "Simple twitter-bot with Python, Tweepy and Heroku"](http://briancaffey.github.io/2016/04/05/twitter-bot-tutorial.html)
