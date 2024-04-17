from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

import pyodbc

server = 'DESKTOP-EK7VOTN' 
database = 'MiniMarketEden'  

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-EK7VOTN;DATABASE=MiniMarketEden;Trusted_Connection=yes')

@app.route('/crear_usuario', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contraseña = request.form['contraseña']
        rol = request.form['rol']
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Usuarios (NombreUsuario, Contraseña, Rol) VALUES (?, ?, ?)", nombre_usuario, contraseña, rol)
        conn.commit()
        cursor.close()
        return 'Usuario creado exitosamente!'
    return render_template('crear_usuario.html')

if __name__ == '__main__':
    app.run(debug=True)

#ventas

app = Flask(__name__)

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-EK7VOTN;DATABASE=MiniMarketEden;Trusted_Connection=yes')
cursor = conn.cursor()

@app.route('/ventas')
def ventas():
    cursor.execute("SELECT ProductoID, Nombre FROM Productos")
    productos = cursor.fetchall()
    return render_template('ventas.html', productos=productos)

@app.route('/registrar_venta', methods=['POST'])
def registrar_venta():
    producto_id = request.form['producto']
    cantidad = request.form['cantidad']

    return redirect('/ventas')

if __name__ == '__main__':
    app.run(debug=True)
#kkkkkkkkkkkkkkkkkkk
from flask import Flask, render_template, request, redirect
import pyodbc

app = Flask(__name__)
server = 'DESKTOP-EK7VOTN' 
database = 'MiniMarketEden'  
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-EK7VOTN;DATABASE=MiniMarketEden;Trusted_Connection=yes')
cursor = conn.cursor()

@app.route('/crear_producto', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        cursor.execute("INSERT INTO Productos (Nombre, Descripcion, Precio, Stock) VALUES (?, ?, ?, ?)", nombre, descripcion, precio, stock)
        conn.commit()
        return 'Producto creado exitosamente!'
    return render_template('crear_producto.html')

if __name__ == '__main__':
    app.run(debug=True)
