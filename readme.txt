Run tests:

$ python manage.py test <app_name>.tests.<class_name>.<method_name>

Run coverage:

$ coverage run --source='.' manage.py test <app_name> && coverage report

Generate HTML report

$ coverage html


- el quiere publicar el post varias veces y tener un control de esas publicaciones
- quiere ver los comentarios de los visitantes
- crear una publicación por defecto cada vez que cree un post
- validar la fecha de publicación de un post.
- que el nombre el correo y los comentarios sean obligatorios.
- recibir correo cada vez que recibe un comentario.
- que antes de publicar un post tenga imagenes y una fecha de publicación.
- que pueda cerrar o bloquear una publicación.
- crear api d eservicios con todo este proceso.
- responder comentarios
- enviar correo con la respuesta al comentario.
- que solo acepte imagenes png
- solo permita 3 imagenes por post.
- que se pueda ver la fecha de creación y quien creó el post.
- que la autenticaciń sea mediante token.
