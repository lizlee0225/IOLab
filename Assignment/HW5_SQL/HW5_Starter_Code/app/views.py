from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm
from .forms import OrderForm
from models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    print('im here')
    if form.validate_on_submit():
        print('im in the loop')
        # Get data from the form
        # Send data from form to Database
        company = form.company.data
        email = form.email.data
        phone = form.phone.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        insert_data(company,email,phone,first_name,last_name,street_address,city,state,country,zip_code)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    print(customers)
    address = retrieve_address()
    print(address)
    orders = retrieve_order()
    return render_template('home.html', customers=customers, address=address, orders=orders)
    

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    form = OrderForm()
    if form.validate_on_submit():
        name_of_part = form.name_of_part.data
        manufacturer_of_part = form.manufacturer_of_part.data
        insert_order(name_of_part,manufacturer_of_part,value)
        return redirect('/customers')
    return render_template('order.html', form=form)
