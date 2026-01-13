from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = b'khiopgfdfghj;oioiouiy'
# app.secret_key = b'khiopgfdfghj;oioiouiy'

cars = [
  {'id':1, 'brand':'Toyota', 'model':'Yaris Ativ', 'year':2024, 'price': 560000},
  {'id':2, 'brand':'Toyota', 'model':'Yaris Cross', 'year':2025, 'price': 790000},
  {'id':3, 'brand':'Nissan', 'model':'Kicks', 'year':2024, 'price': 850000}
]

@app.route('/')
def index():
  return render_template('index.html', title='Home Page')

@app.route('/cars', methods=['GET', 'POST'])
def show_cars():
  if request.method == 'POST':
    brand = request.form['brand']
    # print(brand)
    tmp_cars = []
    for car in cars:
      # print(car)
      if brand in car['brand']:
        tmp_cars.append(car)
    return render_template('cars/cars.html',
                         title='Show Cars by Brand Page',
                         cars=tmp_cars)
  
  return render_template('cars/cars.html',
                         title='Show All Cars Page',
                         cars=cars)

@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
  if request.method == 'POST':
    brand = request.form['brand']
    model = request.form['model']
    year = int(request.form['year'])
    price = int(request.form['price'])

    length = len(cars)
    if length != 0:
      id = cars[length-1]['id'] + 1
    else:
      id = 1
    car = {'id':id, 'brand':brand, 'model':model, 'year':year, 'price': price}

    cars.append(car)
    flash('Add new car successfully', 'success')
    return redirect(url_for('show_cars'))
  
  return render_template('cars/new_car.html',
                         title='New Car Page')

@app.route('/cars/<int:id>/delete')
def delete_car(id):
  for car in cars:
    if id == car['id']:
      cars.remove(car)
      break
  
  flash('Delete car successfully', 'success')
  return redirect(url_for('show_cars'))

@app.route('/cars/<int:id>/edit', methods=['GET', 'POST'])
def edit_car(id):
  for c in cars:
    if id == c['id']:
      car = c 
      break
  if request.method == 'POST':
    brand = request.form['brand']
    model = request.form['model']
    year = int(request.form['year'])
    price = int(request.form['price'])

    for car in cars:
      if id == car['id']:
        car['brand'] = brand
        car['model'] = model
        car['year'] = year
        car['price'] = price
        break

    flash('Update car successfully', 'success')
    return redirect(url_for('show_cars'))
  
  return render_template('cars/edit_car.html',
                         title='Edit Car Page',
                         car=car)