## Vercel

> 『Make Cloud Computing as Easy and Accessible as Mobile computing』

Vercel PaaS: https://vercel.com/ 

Vercel  about:https://vercel.com/about

ZEIT(Vercel) 是一家云部署服务的公司，支持静态托管以及 Serverless 服务。

ZEIT 于 `2020年4月21日` 将 ZEIT 更名为 `Vercel` 服务不变

## Vercel With ❤ jango

> Picked from https://medium.com/@jay_hale/django-on-vercel-in-30-minutes-e69eed15b616 and https://jay-hale.medium.com/django-static-files-on-zeit-now-fef2c51215d4
>
> Set up a barebones Django application, then Use a custom builder for Python WSGI applications: [vercel-python-wsgi](https://www.npmjs.com/package/@ardnt/vercel-python-wsgi). 

### Install the Vercel command line tools

Download Vercel CLI from Package Manager 👍

```sh
npm i -g vercel
yarn global add vercel
```

Logging in is then as simple as:

```
$ vercel login
```

### Adjust your static files settings

We’ll need to configure Django’s static settings so that we can collect all of our static files to a single directory and allow Now to deploy just that folder.

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR/"static"
]

STATIC_ROOT = BASE_DIR/"staticfiles"
```

### Configure the project for Vercel

There are three chores to take care of before you’re ready for deployment: adding a Vercel configuration, fixing some settings, and listing our dependencies.

First, add a Vercel configuration file, `vercel.json`, to the root of your project:

```json
{
    "builds": [
        {
            "src": "static/**",
            "use": "@vercel/static"
        },
        {
            "src": "dpps/wsgi.py",
            "use": "@ardnt/vercel-python-wsgi",
            "config": {
                "maxLambdaSize": "30mb"
            }
        }
    ],
    "routes": [
        {
            "src": "/static/(.*)",
            "dest": "/static/$1"
        },
        {
            "src": "/(.*)",
            "dest": "dpps/wsgi.py"
        }
    ]
}
```

You can see the full documentation for the Vercel configuration file on the [docs website](https://vercel.com/docs/configuration).

Next, you’ll need to adjust two Django project settings.

First, update `ALLOWED_HOSTS` to allow `vercel.app` to be a valid hostname for your app.

Second, clear out your settings for `DATABASES` — this will prevent Django from searching for a database adapter (which is not available given the barebones nature of the Lambda compute environment).

```python
# ...

ALLOWED_HOSTS = ['.vercel.app'] # Allow *.vercel.app

# ...

DATABASES = {} # Prevent Django from loading an adapter

# ...
```

Finally, you’ll need to list out dependencies in a `requirements.txt` file so that the builder knows what to install for you before deploying.

That’s it! You’re ready to go! 🍰

### Deploy!

A little bit of configuration pays big dividends for your next step. To get a live working version of your app, all you need to do is run:

```
$ vercel
```

Follow the prompts, pointing the builder to `./` for your project code.

That’s it! After the build completes, your application will be available.

Check your results in the [Vercel dashboard](https://vercel.com/dashboard).

```
Refused to apply style from 'XXX' because its MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.
```

## ⚠️ Disclaimer

Please note that this project is only for learning and research purposes, and the author is not responsible for any legal consequences caused by the use of this project.

## REFs

- [x] [ZEIT.co 是什么样一个组织?](https://www.zhihu.com/question/59278159)

1. @[Parabola](https://www.zhihu.com/people/shuding) 大概 2018 年的某一天，我突然收到了 Guillermo Rauch 的 Twitter 私信：Hey Shu let's work together

   https://socket.io/    |  mongoose | 旧的Next.js官网: https://next-site-ivyycdnshp.now.sh/ 
   
2. @[尤雨溪](https://www.zhihu.com/people/evanyou) 