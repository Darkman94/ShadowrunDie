ShadowrunDie
============

A Bot that allows _Reddit_ Users to toss a pool of dice for the game Shadowrun. This tool is designed to facillitate a fair dice rolling mechanism, allowing users of the social networking system _Reddit_ to play a game of Shadowrun with the knowledge that all results are generated truly randomly (or at least as randomly as can be attained reasonably through a computer system)

TODO
====
- [ ] Prevent the program from crashing when the host server loses internet connection
- [ ] Fix the Debugger
- [ ] Implement a method to support a wider range of dice rolling schemas
- [ ] Create Documentation
- [ ] Get the project to run straight from the root directory

Installation
============
* Download and install [Python 2.7] (http://www.python.org/download/releases/2.7/)

_Windows_
* Download and install [Distribute] (http://python-distribute.org/distribute_setup.py)
* Install pip, by typing the following into the command line:

```
  easy_install pip
```

_Linux_
* Type the following into the terminal

```
apt-get pip
```

* Either way from here on out it should be the same.
* Install praw on your system, this is a handler for _Reddit_

```
pip install praw
```

* Fork the project (Since, you're on _Github_ I assume you know how to do this if not [here is a good resource](http://lifehacker.com/5983680/how-the-heck-do-i-use-github))
* Configure the project (see Configuration below)
* And run the project by running run_boy.py in the Roller folder

Installation Using VirtualEnv
=============================
This is used when one has a version of Python other than 2.7 installed. I assume here that one already has VirtualEnv installed but if not here is the [official guide](https://pypi.python.org/pypi/virtualenv).
* In the command system of your OS (command prompt/terminal) switch to the root directory of the project
* Make the virtual enviroment by typing the following command:

```
virtualenv -p env <path/to/new/python27/>
```

Where path/to/new/python27/ is the path to Python 2.7 that you installed earlier
* Activate the Virtual Enviroment by typing the following into your terminal
_Linux_

```
source virt_env/Scripts/activate
```

_Windows_

```
\env\Scripts\activate
```
* Configure the project  (see Configuration below)
* And run the project by switching to the Roller folder (in Terminal) and typing:

```
python run_bot.py
```

Configuration
=============
There are a few ways to configure the project, all of these configurations can be made with a simple text editor, and must be made to the file run_bot.py in the Roller folder
_Input A User Agent_
Reddit needs to know who's running a bot on their system, so they use a system called user agents. This is identifying info you provide to their API. User agents follow a pattern as so:

```
Bot Name v# by /u/Username
```

Where Bot Name is they name of your bot, # is the version number of the bot, and Username is your Reddit Username (note the login of of the bot)
Place your User Agent:

```
user_agent = 'PUT YOUR USER AGENT HERE'
```

_Give the Bot a Username_
Your bot needs a username and password to be able to post roll results, so build a Reddit Account for it and place it:

```
r.login('PLACE YOUR USERNAME HERE', 'PLACE YOUR PASSWORD HERE')
```

_Select the Subreddit_
Your bot needs to know what Subreddit to scan, by default this is the Test subreddit.

```
subreddit = r.get_subreddit('SELECT YOUR SUBREDDIT HERE')
```

Using the Bot
=============
Finally to use the bot, one simply types a comment in the subreddit being scanned that includes the following command

```
ROLL ##(E)
```

Here ## indicates a two digit number indicating the number of dice to roll (so three dice would be 03, and the Roller can only handle up to 99 dice) and ends with an E if Edge was spent for the roll.
