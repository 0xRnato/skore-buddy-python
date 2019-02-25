# Skore Buddy

_Flask + Vue.js + DialogFlow Chatbot_

## Demo

[Live Demo](https://skore-buddy-python.herokuapp.com/)

#### Important Files

| Location             | Content                                          |
| -------------------- | ------------------------------------------------ |
| `/app`               | Flask Application                                |
| `/app/webhook`       | Dialogflow webhook (`/api/webhook`)              |
| `/app/process`       | Dialogflow detect intent API (`/api/process`)    |
| `/app/client.py`     | Flask Client (`/`)                               |
| `/src`               | Vue App .                                        |
| `/src/main.js`       | JS Application Entry Point                       |
| `/public/index.html` | Html Application Entry Point (`/`)               |
| `/public/static`     | Static Assets                                    |
| `/dist/`             | Bundled Assets Output (generated at `yarn build` |

## Installation

##### Before you start

Before getting started, you should have the following installed and running:

- [x] Yarn - [instructions](https://yarnpkg.com/en/docs/install#mac-stable)
- [x] Vue Cli 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [x] Python 3
- [x] Pipenv (optional)
- [x] Heroku Cli (if deploying to Heroku)

##### Template and Dependencies

- Clone this repository:

```
$ git clone https://github.com/zRnatoNeto/skore-buddy-python.git
```

- Setup virtual environment, install dependencies, and activate it:

```
$ pipenv install --dev
$ pipenv shell
```

- Install JS dependencies

```
$ yarn install
```

## Development Server

Run Flask Api development server:

```
$ python run.py
```

From another tab in the same directory, start the webpack dev server:

```
$ yarn serve
```

The Vuejs application will be served from `localhost:8080` and the Flask Api
and static files will be served from `localhost:5000`.

The dual dev-server setup allows you to take advantage of
webpack's development server with hot module replacement.

Proxy config in `vue.config.js` is used to route the requests
back to Flask's Api on port 5000.

If you would rather run a single dev server, you can run Flask's
development server only on `:5000`, but you have to build build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python run.py
```

## Production Server

This template is configured to work with Heroku + Gunicorn and it's pre-configured
to have Heroku build the application before releasing it.

#### JS Build Process

Heroku's nodejs buidlpack will handle install for all the dependencies from the `packages.json` file.
It will then trigger the `postinstall` command which calls `yarn build`.
This will create the bundled `dist` folder which will be served by whitenoise.

#### Python Build Process

The python buildpack will detect the `Pipfile` and install all the python dependencies.

#### Production Sever Setup

Here are the commands we need to run to get things setup on the Heroku side:

    ```
    $ heroku apps:create skore-buddy-python
    $ heroku git:remote --app skore-buddy-python
    $ heroku buildpacks:add --index 1 heroku/nodejs
    $ heroku buildpacks:add --index 2 heroku/python
    $ heroku config:set FLASK_ENV=production
    $ heroku config:set FLASK_SECRET=SuperSecretKey

    $ git push heroku
    ```

### Heroku deployment - One Click Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/zRnatoNeto/skore-buddy-python)
