# Multi tenant organizational expense tracker

The project is built with django and django restframework with a vue.js frontend.

## [Live demo](https://defyne.lewiskori.com/)

![django-multitenant](https://res.cloudinary.com/lewiskori/image/upload/v1598773348/Screenshot_2020-08-30_vue-django-multitenant_wlrpcz.png)

Frontend code can be [found here](https://github.com/lewis-kori/vue-django-multitenant)

## setup instructions

1. setup virtual environment using

   ```python
   virtualenv env_name -p python3.8
   ```

2. activate the virtual environment by going to env folder location

   ```python
   source env_name/bin/activate
    ```

   press enter

3. once the env is activate, go back to the django project directory
install all requirements by running

     ```python
    pip install -r requirements.txt
     ```

4. set up an env file with your configurations.
attached in the project folder is an example to guide you on this.
use <https://djecrety.ir/> to generate a secret key.

5. once done run

    ```python
   python manage.py migrate
   python manage.py runserver
    ```

6. check individual app folders for instructions
 on the available endpoints in the README.md
