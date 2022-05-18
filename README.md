# Customer-Management-System
The system works to store information on products, customers and the orders that the customers have made.


# Table of Contents
- [Background](#background)
- [Minimum Requirements](#minimum-requirements)
- [Quickstart](#quickstart)
- [Database SetUp](#database-setup)
- [Database Migration](#database-migration)
- [Dashboard Page](#dashboard-page)
- [Product Page](#product-page)
- [Customer Page](#customer-page)
- [SignedIn User](#signedin-user)
- [Settings Page](#settings-page)
- [SignUp Page](#signup-page)


## Background
This project is a Customer-Order Management System that tracks individual customers and orders they have made for different products. The customers have their own dashboard account to track the orders of products they have purchased. It implements a CustomerProfile Authentication and Authorization, Django-Filters functionality as well as Password Reset functionality.
he project applies Django's MVT(Model View Templates) architecture. It has a CRUD (Create Read Update Delete) application for the Orders & Products. he project is written with Function-Based Views (FBV) with focus on core fundamentals which are easy to read, understand and implement

## Minimum Requirements
This project supports Ubuntu Linux 20.04 and Windows OS with their previous stable releases. It has not been tested on Mac OS.

- [Python3](https://www.python.org/downloads/)
- [Django 3.2](https://www.djangoproject.com/)
- [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
- [PostgreSQL 14.2+](http://www.postgresql.org/)
- [Git](https://git-scm.com/downloads)

## Quickstart
```bash
$ mkdir customermanagementsystem
$ cd customermanagementsystem
$ git init
$ git clone https://github.com/Eugene-Kwaka/Customer-Management-System.git
$ cd Customer-Management-System
$ sudo apt install python3-pip python3-django
$ sudo apt install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Database Setup
``` settings.py
'ENGINE': 'django.db.backends.postgresql',
'NAME': ('DB_NAME'),
'USER': ('DB_USER'),
'PASSWORD': ('DB_PASSWORD'),
'HOST': ('DB_HOST'),
'PORT': ('DB_PORT')
```

## Database Migration
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## Dashboard Page

![Dashboard 2021-07-03 172701](https://user-images.githubusercontent.com/44529236/124357714-af6d2b00-dc25-11eb-8020-eb15c9ea2f95.png)

![Customer-Order image 2021-07-03 172919](https://user-images.githubusercontent.com/44529236/124358149-9feee180-dc27-11eb-8b2a-4495bc1a4680.png)


-	Total orders done
-	Newly recorded orders
-	All the writer’s created by the admin
-	All the orders Pending, Out for Delivery and Delivered.
-	Search & Filter functionality based on- customer, product, category, status and dates.
 
 
 
 ## Product Page
 
 ![Products Page 2021-07-03 173105](https://user-images.githubusercontent.com/44529236/124358174-bf860a00-dc27-11eb-95f8-22fa8c230583.png)

-Shows all the products and the admin can Add, Update and Delete products




## Customer Page

![Customer Page 2021-07-03 173224](https://user-images.githubusercontent.com/44529236/124358218-fb20d400-dc27-11eb-88a7-5f10030f4c72.png)

- Customer details including all the orders done
- Update, Delete and Place and Order functionality to a customer
- Search & Filter functionality based on- product, category, status and dates.


## SignedIn User

![Logged In Customer Page 2021-07-03 173456](https://user-images.githubusercontent.com/44529236/124358310-666aa600-dc28-11eb-80c3-5f3f560d19c8.png)

- Search & Filter functionality based on- product, category, status and dates. 
- Settings functionality to update profile


## Settings Page

![Customer Settings Page 2021-07-03 173627](https://user-images.githubusercontent.com/44529236/124358382-b0ec2280-dc28-11eb-8265-93923bf5c966.png)

- Customer can update their details



 ## SignUp Page

![Signup Page 2021-07-03 173339](https://user-images.githubusercontent.com/44529236/124358405-c9f4d380-dc28-11eb-9678-11d6e093e7df.png)

- Customer can sign in and create an account 
 
