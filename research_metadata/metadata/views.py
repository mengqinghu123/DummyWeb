from django.shortcuts import render, redirect
from .models import ResearchMetadata
import pluggy
from .plugin import MySpec, MetadataPlugin

def form(request):
    if request.method == 'POST':
        data_provider = request.POST.get('data_provider')
        data_format = request.POST.get('data_format')
        degree_of_aggregation = request.POST.get('degree_of_aggregation')

        # Save to the database
        metadata = ResearchMetadata(
            data_provider=data_provider,
            data_format=data_format,
            degree_of_aggregation=degree_of_aggregation
        )
        metadata.save()


        # create a manager and add the spec
        pm = pluggy.PluginManager("metadata")
        pm.add_hookspecs(MySpec)
        # register plugins
        pm.register(MetadataPlugin())
        # call "generate_readme" hook
        pm.hook.generate_readme(metadata=metadata)

        return redirect('success')

    return render(request, 'form.html')

def success(request):
    return render(request, 'success.html')
