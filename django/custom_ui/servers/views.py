from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from servers.models import Server


class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['name', 'ip', 'order']


def server_list(request, template_name='servers/server_list.html'):
    servers = Server.objects.all()
    data = {}
    data['object_list'] = servers
    return render(request, template_name, data)


def server_create(request, template_name='servers/server_form.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})


def server_update(request, pk, template_name='servers/server_form.html'):
    server = get_object_or_404(Server, pk=pk)
    form = ServerForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})


def server_delete(request, pk, template_name='servers/server_confirm_delete.html'):
    server = get_object_or_404(Server, pk=pk)
    if request.method=='POST':
        server.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':server})


def touhid_mia(request, template_name='servers/touhid.html'):
    return render(request, template_name)


def message(request, template_name='servers/message.html'):
    messages.error(request, "Huge success!")
    messages.success(request, "Huge success!")
    return render(request, template_name)


def message2(request, template_name='servers/message2.html'):
    return render(request, template_name)