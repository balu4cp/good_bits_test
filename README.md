
To run this project, do the following steps
###### 1.Clone the project
###### 2.Create a virtual environment
virtualenv -p python3 venv
###### 3.Activate environment
source venv/bin/activate
###### 4 python manage.py -r requirement.txt
###### 5.create database with name 'finance_db' (postgres database)
###### 6.python manage makemigrations
###### 7.python manage migrate
###### 8.python manage makemigrations
###### 9.python 1create_admin.py
###### 10.In settings.py provide values for 
- STRIPE_PUBLISHABLE_KEY obtained from stripe account
- STRIPE_SECRET_KEY obtained from stripe account
- BITLY_ACCESS_TOKEN obtained from bitly account
- EMAIL_HOST_USER google email
- EMAIL_HOST_PASSWORD google email password
###### 11. In templates/invoice_payement.html,
- add STRIPE_PUBLISHABLE_KEY in line 71  // var stripe = Stripe('< YOUR STRIPE PUBLISHABLE KEY>');
###### 12 python manage.py runserver
