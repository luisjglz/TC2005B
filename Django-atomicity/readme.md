##Atomicidad y aislamiento en Django

<br>


1. Crear un nuevo proyecto de Django.


2. Hacer migraciones y crear superuser.

3. Crear una nueva aplicación llamada 'bank'

4. Crear el modelo del cliente del banco dentro de models.proyecto


	```
	from django.db import models
	
	class cliente(models.Model):
	  nombre = models.CharField(max_length=50)
	  saldo = models.DecimalField(max_digits=5, decimal_places=2)
	  creado = models.DateTimeField(auto_now_add=True)
	  modificado = models.DateTimeField(auto_now=True)
	
	  def __str__(self):
	    return self.nombre
	```
	

	<br>

5. Crear un template de formulario creando el archivo forms.py:

	```
	from django import forms


	class Pago(forms.Form):
	  envia = forms.CharField(max_length=30)
	  recibe = forms.CharField(max_length=30)
	  monto = forms.CharField(max_length=30)  
  	```

	<br>
6. Crear archivo de migraciones:

	```
	python3 manage.py makemigrations
	```

	<br>
7. Ejecutar la migración:

	```
	python3 manage.py migrate
	```

	<br>
8. Añadir el modelo de Cliente al backend de admin en **admin.py**:

	```
	from django.contrib import admin
	
	from .models import cliente
	
	class ClienteAdmin(admin.ModelAdmin):
	    list_display = ('nombre', 'saldo')
	admin.site.register(cliente, ClienteAdmin)
	```

	<br>
9. En el backend admin, añadir dos clientes: *cliente_a* y *cliente_b*

	<br>
10. Crea un nuevo método en **views.py** que despliegue el formulario de procesamiento de transacciones:

	```
	from django.shortcuts import render
	from .forms import Pago

	def procesador_de_pagos(request):
	  form = Pago()
	  return render(request, 'index.html', {'form': form})
	```

	<br>
11. Añade una ruta en **urls.py** hacia el formulario:
	```
	from django.contrib import admin
	from django.urls import path
	from bank import views
	
	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('', views.procesador_de_pagos, name='transferencias')
	]
	```

	<br>
12. Crea un folder llamado **templates** y dentro un archivo *index.html* con el código:

	```
	<!doctype html>
	<html lang="en">
	  <head>
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1">
	    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
	    <title>Atomicidad en transacciones</title>
	  </head>
	  <body>
	
	    <div class="container pt-5" style="max-width:400px">
	    <form method="post">
	        {% csrf_token %}
	        <table>
	        {{ form.as_table }}
	        </table>
	        <input type="submit" value="Transferir">
	    </form>
	    </div>
	    
	    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>
	  </body>
	</html>
	```

	<br>
13. Añade el folder 'templates' en **settings.py**:

	```
	'DIRS': [BASE_DIR / 'templates'],
	```

	<br>
14. Añade el código para hacer una transferencia dentro de **views.py**:

	```
	from django.http import HttpResponseRedirect
	from .models import cliente
	import decimal
	
	def procesador_de_pagos(request):
	  if request.method == 'POST':
	
	    form = Pago(request.POST)
	
	    if form.is_valid():
	        x = form.cleaned_data['envia']
	        y = form.cleaned_data['recibe']
	        z = decimal.Decimal(form.cleaned_data['monto'])
	
	        envia = cliente.objects.get(nombre=x)
	        envia.saldo -= z
	        envia.save()
	
	        recibe = cliente.objects.get(nombre=y)
	        recibe.saldo += z
	        recibe.save()
	
	        return HttpResponseRedirect('/')
	  else:
	    form = Pago()
	  return render(request, 'index.html', {'form': form})
	```
	<br>
15. Checar el caso donde se hace una transferencia a un usuario inexistente.
16. Corregir. Importar de django.db  'transactions':

	```
	from django.db import transaction
	```

	<br>
17. Opción 1: usando decorator antes del método procesador_de_pagos:

	```
	@transaction.atomic
	```

	<br>
18. Opción 2: usando context-manager:

	```
	with transaction.atomic():
	    envia = cliente.objects.get(nombre=x)
	    envia.saldo -= z
	    envia.save()
	
	    recibe = cliente.objects.get(nombre=y)
	    recibe.saldo += z
	    recibe.save()
	```

	<br>
19. Lograr la propiedad "Isolated" mediante un "lock" a las tablas durante su edición.
Para esto usaremos **select\_for\_update**, buscarlo en la API de Django.

Cambiamos el modo en que seleccionamos a 'envia' y a 'recibe':

envia = cliente.objects.get(nombre=x)

recibe = cliente.objects.get(nombre=y)

*ahora:*

**envia = cliente.objects.select_for_update().get(nombre=x)**

**recibe = cliente.objects.select_for_update().get(nombre=y)**




