from flask import Flask
from flask import render_template
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


if __name__ == '__main__':
    app.run(debug=True)
