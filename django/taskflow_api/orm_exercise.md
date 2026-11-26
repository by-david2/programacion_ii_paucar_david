>>> Veterinario.objects.all()
<QuerySet [<Veterinario: kevin quinga>]>

>>> Veterinario.objects.count()
1

>>> Veterinario.objects.get(pk=1)
<Veterinario: kevin quinga>

>>> Project.objects.filter(name="kevin quinga")
<QuerySet [<Project: kevin quinga>]>

>>> Veterinario.objects.filter(name__contains="kevin")
<QuerySet [<Project: kevin quinga>]>

>>> Veterinario.objects.filter(description__icontains="proyecto")
<QuerySet [<Project: kevin quinga>]>
