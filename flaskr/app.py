from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio
from .modelos import AlbumSchema, CancionSchema, UsuarioSchema
from flask_restful import Api 
from .vistas import VistaCanciones, VistaCancion, VistaUsuarios, VistaUsuario, \
                    VistaAlbumes, VistaAlbum
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#PRUEBA
with app.app_context():
  u1 = Usuario(nombre_usuario='Usuario 1', contrasena='pass 1')
  u2 = Usuario(nombre_usuario='Usuario 2', contrasena='pass 2')
  a1 = Album(titulo='Album 1', anio=2001, descripcion='Desc album 1', medio=Medio.DISCO)
  a2 = Album(titulo='Album 2', anio=2002, descripcion='Desc album 2', medio=Medio.CASETE)
  u1.albumes.append(a1)
  u2.albumes.append(a2)
  c1 = Cancion(titulo='Canción 1', minutos=2, segundos=25, interprete='Cantante 1')
  c2 = Cancion(titulo='Canción 2', minutos=4, segundos=50, interprete='Cantante 2')
  a1.canciones.append(c1)
  a2.canciones.append(c2)
  db.session.add(c1)
  db.session.add(c2)
  db.session.add(a1)
  db.session.add(a2)
  db.session.add(u1)
  db.session.add(u2)
  db.session.commit()
  print(f'Canciones: {Cancion.query.all()}')
  print(f'Albumes: {Album.query.all()}')
  print(f'Canciones de album 1: {Album.query.all()[0].canciones}')
  print(f'Usuarios: {Usuario.query.all()}')
  print(f'Albumes de usuario 1: {Usuario.query.all()[0].albumes}')
  db.session.delete(u1)
  print(f'Usuarios después de eliminar usuario: {Usuario.query.all()} -> usuario 1 eliminado')
  print(f'Albumes después de eliminar usuario: {Album.query.all()} -> album 1 relacionado a usuario 1 eliminado en cascada')
  print(f'Canciones después de eliminar usuario: {Cancion.query.all()} -> canción 1 estaba relacionada con album 1, sin embargo no se elimina en cascada')
  
  # probando schemas
  album_schema = AlbumSchema()
  cancion_schema = CancionSchema()
  usuario_schema = UsuarioSchema()
  #a = Album(titulo='Album 3', anio=2003, descripcion='Desc album 3', medio=Medio.DISCO)
  #db.session.add(a)
  #db.session.commit()
  print("imprimir albumes usando schema")
  print([album_schema.dumps(album) for album in Album.query.all()])  # a partir del conjunto de resultados, se itera para serializarlos con album_schema e imprimir el json correspondiente
  print("imprimir canciones usando schemas")
  print([cancion_schema.dumps(cancion) for cancion in Cancion.query.all()])  # a partir del conjunto de resultados, se itera para serializarlos con album_schema e imprimir el json correspondiente
  print("imprimir usuarios usando schemas")
  print([usuario_schema.dumps(usuario) for usuario in Usuario.query.all()])  # a partir del conjunto de resultados, se itera para serializarlos con album_schema e imprimir el json correspondiente

  # prueba vistas
  api = Api(app)
  api.add_resource(VistaCanciones, '/canciones')
  api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
  api.add_resource(VistaUsuarios, '/usuarios')
  api.add_resource(VistaUsuario, '/usuario/<int:id_usuario>')
  api.add_resource(VistaAlbumes, '/albumes')
  api.add_resource(VistaAlbum, '/album/<int:id_album>')
  
  jwt = JWTManager(app)