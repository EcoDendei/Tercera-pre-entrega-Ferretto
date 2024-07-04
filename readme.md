# Tercera pre-entrega Ferretto

## Idea/Objetivo detras del sitio/app web
La idea detras de la app Contame es poder tener una herramienta en la cual poder cargar los gastos e ingresos personales.
Ya que no encontre actualmente ninguna app gratuita que se adapte a lo que necesito y creo que es un proyecto interesante y con mucho potencial para agregar montones de funcionalidades.
Con esto se busca poder llevar un control de los gastos por categorias (Supermercado, Servicios, Impuestos, Deporte, etc)
Tambien se busca poder tener el estado de las cuentas, como el efectivo, dineros en cuantas bancarias, fondos de inversion, etc.

Se busca una vez que se entra a la app, en el dashboard principal tener a simple vista los gastos del mes.
Mas adelante se puede poner un modelo para cargar presupuestos mensuales y tener en el dashboard el % del presupusto al día actual, para ver como se viene cumpliendo el presupuest y estar atento de no excederse.

Tambien la idea es poder tener una comparacion con meses anteriores por categoria y ver cual categoria se incremento por sobre el resto.
#

## Consignas de la tercer entrega
- Link a GitHub
- Proyecto Django
  1- Herencia HTML
  2- Al menos 3 modelos
  3- Un formalario para insertar datos de estos modelos
  4- Formulario para buscar algun dato en la DB
  5- Readme
#

## 2-Modelos
  Los modelos son 5, pero para esta entrega por favor solo tener en cuenta los modelos de Moneda, Cuenta y Asiento:
  Asiento (Algo similar a un asiento contable, se crea cuando hay algun evento que genere movimiento en las cuentas)
  Movimiento (Los movimientos de cuenta, cuando se genera un asiento la idea es generar 2 movimientos, de una cuanta se saca dinero y en otra segunda cuanta se ingresa dinero)
  Cuenta (Una categoria principal, como Salud, Deporte, Clientes, etc.)
  Subcuenta (Una subcategoria, de una categoria principal (Cuenta) como por ej. Dentista, Oculista, Padel, Futbol, etc.)
  Moneda (Ya que podemos tener movimientos es diferentes monedas)
#

## 3-Formularios para insertar datos
- asientos/asiento_form/
- monedas/moneda_form/
- cuentas/cuenta_form/
#

## 4-Formulario para busqueda (de subcuentas)
- cuentas/buscar_cuentas/
#

## Listado completo de funciones
    path('', home, name="home"),
    path('asientos/', asientos, name="asientos"),
    path('cuentas/', cuentas, name="cuentas"),
    path('subcuentas/', subcuentas, name="subcuentas"),
    path('movimientos/', movimientos, name="movimientos"),
    path('monedas/', monedas, name="monedas"),
    path('acerca/', acerca, name="acerca"),
    path('monedas/moneda_form/', monedaForm, name="monedaForm"),
    path('cuentas/cuenta_form/', cuentaForm, name="cuentaForm"),
    path('subcuentas/subcuenta_form/', subcuentaForm, name="subcuentaForm"),
    path('asientos/asiento_form/', asientoForm, name="asientoForm"),
    path('cuentas/buscar_cuentas/', buscarCuentas, name="buscarCuentas"),
    path('cuentas/encontrar_cuentas/', encontrarCuentas, name="encontrarCuentas"),
#

## Comentarios
Como template HTML se utilizo https://startbootstrap.com/template/sb-admin ya que era el unico template que era de la categoria Dashboard, que era HTML y gratuito.

He utilizado, ya que se requeria, el uso de ForeignKeys para vincular tablas, pero no he encontrado la forma de poder mostrar esto correctamente en los formularios. 
Por lo que no he podido hacer el formulario para insertar datos de los modeles con ForeignKeys.

## Orden de prueba
1 - Crear Monedas
2 - Crear Cuentas
3 - Crear Subcuentas
4 - Crear Asientos
5 - Crear Movientos

Se debe hacer en este orden ya que por ejemplo Movimiento tiene que estar vinculado a un asiento y a una cuenta que ya deben existir previamente.
