from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from analytics.models import ClickEvent
from .models import KirrURL
from .forms import HomeForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = HomeForm()
        context = {
            'form' : form,
        }
        return render(request, "home.html", context)

    def post(self, request, *args, **kwargs):
        form = HomeForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj = KirrURL.objects.filter(url=new_url).first()
            if not obj:
                obj = KirrURL.objects.create(url=new_url)
            ClickEvent.objects.create_event(obj)
            context['obj'] = obj
            return render(request, "success.html", context)

        return render(request, "home.html", context)


class RedirectView(View):
    def get(self, request, shortcode, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return redirect(obj.url)


