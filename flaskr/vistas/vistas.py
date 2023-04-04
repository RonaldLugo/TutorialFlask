from flask_restful import Resource
from ..modelos import db, Cancion, Usuario, Album, CancionSchema, UsuarioSchema, AlbumSchema
from flask import request 

cancion_schema = CancionSchema()
usuario_schema = UsuarioSchema()
album_schema = AlbumSchema()

class VistaCanciones(Resource):
  
  def get(self):
    return [cancion_schema.dump(cancion) for cancion in Cancion.query.all()]
  
  def post(self):
    nueva_cancion = Cancion(titulo=request.json['titulo'], \
                            minutos=request.json['minutos'], \
                            segundos=request.json['segundos'], \
                            interprete=request.json['interprete'])
    db.session.add(nueva_cancion)
    db.session.commit()
    return cancion_schema.dump(nueva_cancion)
  
class VistaCancion(Resource):
  
  def get(self, id_cancion):
    return cancion_schema.dump(Cancion.query.get_or_404(id_cancion))
  
  def put(self, id_cancion):
    cancion = Cancion.query.get_or_404(id_cancion)
    cancion.titulo = request.json.get('titulo', cancion.titulo)
    cancion.minutos = request.json.get('minutos', cancion.minutos)
    cancion.segundos = request.json.get('segundos', cancion.segundos)
    cancion.interprete = request.json.get('interprete', cancion.interprete)
    db.session.commit()
    return cancion_schema.dump(cancion)
  
  def delete(self, id_cancion):
    cancion = Cancion.query.get_or_404(id_cancion)
    db.session.delete(cancion)
    db.session.commit()
    return 'Operacion exitosa', 204
  
class VistaUsuarios(Resource):
  
  def get(self):
    return [usuario_schema.dump(usuario) for usuario in Usuario.query.all()]
  
  def post(self):
    nuevo_usuario = Usuario(nombre_usuario=request.json['nombre_usuario'], \
                            contrasena=request.json['contrasena'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return usuario_schema.dump(nuevo_usuario)
  
class VistaUsuario(Resource):
  
  def get(self, id_usuario):
    return usuario_schema.dump(Usuario.query.get_or_404(id_usuario))
  
  def put(self, id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)
    usuario.nombre_usuario = request.json.get('nombre_usuario', usuario.nombre_usuario)
    usuario.contrasena = request.json.get('contrasena', usuario.contrasena)
    db.session.commit() 
    return usuario_schema.dump(usuario)
  
  def delete(self, id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)
    db.session.delete(usuario)
    db.session.commit()
    return 'Operacion exitosa', 204
  
class VistaAlbumes(Resource):
  
  def get(self):
    return [album_schema.dump(album) for album in Album.query.all()]
  
  def post(self):
    nuevo_album = Album(titulo = request.json['titulo'], \
                        anio=request.json['anio'], \
                        descripcion=request.json['descripcion'], \
                        medio=request.json['medio'])
    db.session.add(nuevo_album)
    db.session.commit()
    return album_schema.dump(nuevo_album)
  
class VistaAlbum(Resource):
  
  def get(self, id_album):
    return album_schema.dump(Album.query.get_or_404(id_album))
  
  def put(self, id_album):
    album = Album.query.get_or_404(id_album)
    album.titulo = request.json.get('titulo', album.titulo)
    album.anio = request.json.get('anio', album.anio)
    album.descripcion = request.json.get('descripcion', album.descripcion)
    album.medio = request.json.get('medio', album.medio)
    db.session.commit()
    return album_schema.dump(album)
  
  def delete(self, id_album):
    album = Album.query.get_or_404(id_album)
    db.session.delete(album)
    db.session.commit()
    return 'Operacion exitosa', 204
  