from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)

# Rutas de la API CRUD

# Obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.query.all()
    productos_json = [{'id': producto.id, 'nombre': producto.nombre, 'precio': producto.precio} for producto in productos]
    return jsonify({'productos': productos_json})

# Obtener un producto por ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    return jsonify({'id': producto.id, 'nombre': producto.nombre, 'precio': producto.precio})

# Crear un nuevo producto
@app.route('/productos', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nuevo_producto = Producto(nombre=data['nombre'], precio=data['precio'])
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify({'id': nuevo_producto.id, 'nombre': nuevo_producto.nombre, 'precio': nuevo_producto.precio}), 201

# Actualizar un producto por ID
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    data = request.get_json()
    producto.nombre = data['nombre']
    producto.precio = data['precio']
    db.session.commit()
    return jsonify({'id': producto.id, 'nombre': producto.nombre, 'precio': producto.precio})

# Eliminar un producto por ID
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto eliminado con éxito'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
