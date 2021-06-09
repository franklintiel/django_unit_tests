from .models import Post

class postestings:
    def create_post(self, title:str, content:str, created_at:str, creator:str):
        if title is None and content is None:
            if title in ['ESTE ES EL TITULO', 'Soy el contenido de este post de Maryori Sabalza', '08:06:2021','Maryori Sabalza'] and content in ['ESTE ES EL TITULO', 'Soy el contenido de este post de Maryori Sabalza', '08:06:2021','Maryori Sabalza']:
                create = create_post(title=title, content=content, created_at=created_at, creator=creator)
        return None    


    def update_post(content:str, created_at:str):
        if content is not None and created_at is not None:
            if content in ['Contenido actualizado', 'Mar'] and created_at in  ['Contenido actualizado', 'Mar']:
                update= update_post(content=content, created_at=created_at)
        return True    
