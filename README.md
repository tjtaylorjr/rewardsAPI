# Rewards API

## __Setup and Installation__

This project uses the Python programming language, specifically version 3.10, and pipenv for package management.  You will need to make sure that you have these installed before you can proceed.

### Python
---
Python works on all major operating systems.  I could write an entire readme on how to install Python but instead I will just link you to a very good breakdown of installing this programming language on Windows, Linux and macOS:

https://realpython.com/installing-python/

Or straight from the horse's mouth, if you are so inclined.  Though it is not spelled out in as much detail, IMO:

https://wiki.python.org/moin/BeginnersGuide/Download


For Windows, I highly recommend using the Windows installer for python from the official website because it will automatically install the next thing on our list.

Once Python is installed, verify by entering the following in your Linux/macOS terminal or Windows Powershell:

```console
Python --version
```

### Pip
---
Newer versions of Python come with pip preinstalled which you should verify in your terminal with the same command above, only with pip instead of python.

```console
pip --version
```

If you get a version number with a path, it means pip is already installed.

The instructions for how to install pip, should you need to do so, can be found directly in the documentation here:

https://pip.pypa.io/en/stable/installation/

If you do need to install pip, you will also want to follow the instructions to update the PATH environment variable as well.

### Pipenv
---
Finally, this project uses pipenv as both the package and virtual testing environment manager. (more on this below)

For now you can install pipenv with the following command via Windows Powershell or the Linux/macOS terminal:

```console
pip install --user pipenv
```

More information can be found found here:

https://pipenv.pypa.io/en/latest/

You should also update the PATH environment variable for your operating system so that pipenv commands get forwarded to the right place.  Instructions:

https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv

Once again you can verify installation with
```console
pipenv --version
```
### Git
---
You will also need git, if you don't already have it installed.  (check with the --version tag, if you need to)

Installation instructions:

https://github.com/git-guides/install-git

## __Run the API on your local machine__

### Clone the project
---
All installed?  Great!

Create a directory at the location of your choice that will house the project package.  Windows requires an additional install and tweaking for the next part in order to do it in Powershell.  Not really worth it for this project's purpose, so instead just use the search on the task bar for Git Bash and open that.  Git Bash will allow you to clone the git repository to the directory you specified.

 To clone this repository via your Windows Git Bash or macOS/Linux terminal, make sure to navigate to that directory via the prompt and then enter the following command:

```console
git clone https://github.com/tjtaylorjr/rewardsAPI.git
```

### Virtual Environment and dependencies
---
Fortunately this part is relatively easy. While still inside the main directory via your Powershell/terminal run the following command:

```console
Pipenv sync --dev
```

This will create the virtual environment and install all necessary dependencies.  The venv (virtual environment) should now be active in your terminal.  Indicated by (< your directory name here >) at the beginning of your prompt line.  If it is not, use the following command to enter:

```console
pipenv shell
```

Now we are ready to run the development server.

### Unit tests
---
If you would like to run the test file to make sure everything passes, you can do so with:

```console
pipenv run python3 test_rewards_service.py
```

### Start the server
---
Otherwise skip right to running the web service in development mode with

```console
pipenv run python3 rewards_service.py
```

### Testing the endpoints
---

You can use whatever tool you want to want to send HTTP requests to the API.  (I like [Postman](https://www.postman.com/downloads/))

There are three endpoints to interact with.  All accept and return JSON.

<br>

#### Get Balance
http://localhost:7000/api/v1/account

This endpoint will return a dictionary with keys for all companies that have provided points to the consumer along with a value representing the number of points.

<br>

#### Post Transaction
http://localhost:7000/api/v1/account

The endpoint expects a JSON formatted object like so:
<br>
{
    "payer": "TYSON",
    "points": 1000,
    "timestamp": "2022-01-13T17:00:00Z"
}

<br>

#### Post Redemption
http://localhost:7000/api/v1/account/rewards

This endpoint takes a json formatted object representing points the consumer wishes to redeem.

{"points": 5000}

### Shut the server down
---
To exit the virtual environment simply type exit into the terminal hit the return/enter key.
