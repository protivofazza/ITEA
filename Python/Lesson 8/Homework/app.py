from flask import Flask
from flask import render_template, request, jsonify, redirect
import sqlite3

app = Flask(__name__)
DATABASE = "database.db"


def read_query(query="", *args):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute(query, list(args))
        result = cursor.fetchall()
    except:
        print("An error occured while querying: " + query)
    finally:
        connection.close()
        return result


def insert_query(query="", *args):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    error = ""
    try:
        cursor.execute(query, list(args))
        connection.commit()
    except Exception as e:
        error = "An error occured while querying: " + query
        print(e)
    finally:
        connection.close()
        return error


@app.route('/')
def start():
    categories = read_query("SELECT * FROM categories")
    return render_template('index.html', categories=categories)


@app.route('/category/<int:category_id>')
def show_products(category_id):
    products = read_query("SELECT * FROM products "
                          "WHERE category_id = ? "
                          "AND available_in_shop + available_on_storage > 0",
                          category_id)
    category_name = read_query("SELECT name FROM categories "
                               "WHERE id = ?",
                               category_id)
    return render_template("products.html", products=products, category_name=category_name)


@app.route('/product/<int:product_id>')
def show_product(product_id):
    product = read_query("SELECT products.*, categories.name FROM products "
                         "INNER JOIN categories on products.category_id = categories.id "
                         "WHERE products.id = ?",
                         product_id)
    return render_template("product.html", product=product)


@app.route('/admin')
def admin_main_page():
    return render_template("admin.html")


@app.route('/new_category', methods=['POST', 'GET'])
def new_category():
    if request.method == 'GET':
        return render_template("new_category.html")
    elif request.method == 'POST':
        params: dict = request.form.to_dict()
        if 'new_category_name' in params:
            old_category_name = read_query("SELECT * FROM categories WHERE name = ?", params['new_category_name'])
            if old_category_name:
                return "This category already exists. Please come back and try one more time"
            error = insert_query("INSERT INTO categories (name) VALUES (?)", params['new_category_name'])
            if not error:
                return redirect('/admin')
            return "An error occured. Please come back and try one more time. " + error
        return "An error occured. Please come back and try one more time"


@app.route('/new_product', methods=['POST', 'GET'])
def new_product():
    if request.method == 'GET':
        categories = read_query("SELECT * FROM categories")
        return render_template("new_product.html", categories=categories)
    elif request.method == 'POST':
        params: dict = request.form.to_dict()
        # validation
        if not ('name' and 'model' and 'description' and 'category_id' and 'available_in_shop'
                and 'available_on_storage' and 'price') in params:
            return "An error occured. Please come back and try one more time"
        try:
            params['category_id'] = int(params['category_id'])
            params['available_in_shop'] = int(params['available_in_shop'])
            params['available_on_storage'] = int(params['category_id'])
            params['price'] = int(params['price'])
        except ValueError:
            return "An error occured. Please come back and try one more time"
        # inserting
        error = insert_query("""INSERT INTO products 
                                (name, model, description, category_id, available_in_shop, available_on_storage, price)
                                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                             params['name'], params['model'], params['description'], params['category_id'],
                             params['available_in_shop'], params['available_on_storage'], params['price'])
        if error:
            return "An error occured. Please come back and try one more time"

        return redirect('/admin')
    return "Unknown method"


if __name__ == '__main__':
    app.run(debug=True)
