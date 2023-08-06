from datetime import date
class Clientes():
    def __init__(self, nombre, apellido, dni):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._compra = False
        self.cant_ventas = 0         
    
    def __str__(self):
        return f'Hola {self._nombre}, bienvenido/a a nuestra página!!!'    
    
    def compras(self, comprar):
        dt = date.today()
        if comprar == 'si':      
            self._compra = True
            self.cant_ventas += 1
            return print(f'Gracias {self._nombre} por su compra!!' f'\nFecha: {dt}' f'\nCantidad de compras: {self.cant_ventas}')           
        else:
            if comprar == 'no':
                return print(f'Compra cancelada.' f'\nGracias {self._nombre}, esperamos que vuelvas!!!')

class Vendedor:
    def __init__(self, vendedor):
        self._vendedor = vendedor    
    def __str__(self):
        return self._vendedor
    def cantidad_venta(self):
        cleo = []
        leo = []
        if 'leo' == self:
            leo.append('leo')            
            print(f'Cantidad de ventas: {len(leo)}')
        elif 'cleo' == self:
            cleo.append('cleo')
            print(f'Cantidad de ventas: {len(cleo)}')
        else:
            return print('Salir')                  
class Producto:
    def __init__(self, total_venta):
        self.total_venta = total_venta
    def __str__(self):
        return  f'\nComisión: ${str(self.total_venta*0.05)}'     

cliente_x= Clientes(input('Nombre: '), input('Apellido: '), input('DNI: '))
consulta_x = Clientes.compras(cliente_x, input('Ingresar si/no:').lower()) #si cancela compra monto $0#
monto_comision = Producto(int(input('Monto: $')))
print(monto_comision)
vendedor_a = Vendedor.cantidad_venta(input('Vendedor/a:')) #si cancela ingresa cualquier letra para salir#



    
    