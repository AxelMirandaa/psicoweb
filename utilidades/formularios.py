from app.models import *
from django.utils.html import format_html



#####formulario


#####admin
def set_user(obj):
	return f"{obj.user.first_name} {obj.user.last_name}"
set_user.short_description="Usuario"


def set_categoria_con_link(obj):
	return format_html(f"""<a href="/core/backend/home/categoria/{obj.categoria_id}/change/" target="_blank">{obj.categoria}</a>""")
set_categoria_con_link.short_description="Categoría"


