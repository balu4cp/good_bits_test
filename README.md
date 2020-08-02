
To run this project, do the following steps
###### 1.Clone the project
###### 2.Create a virtual environment
virtualenv -p python3 venv
###### 3.Activate environment
source venv/bin/activate
###### 4.create database with name 'finance_db' (postgres database)
###### 5.python manage makemigrations
###### 6.python manage migrate
###### 7.python manage makemigrations
###### 8.python 1create_admin.py
###### 9.In settings.py provide values for 
- STRIPE_PUBLISHABLE_KEY obtained from stripe account
- STRIPE_SECRET_KEY obtained from stripe account
- BITLY_ACCESS_TOKEN obtained from bitly account
- EMAIL_HOST_USER google email
- EMAIL_HOST_PASSWORD google email password
###### 10. In templates/invoice_payement.html,
- add STRIPE_PUBLISHABLE_KEY in line 71  // var stripe = Stripe('< YOUR STRIPE PUBLISHABLE KEY>');
###### 11 python manage.py runserver
