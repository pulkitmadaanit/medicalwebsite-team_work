from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from site_2_process_instrument.models import HomeImageSlider, HomePageData,InstrumentsParametersWise


# class HomeView(TemplateView):
#     """
#     This is HOme view, This is page have both link
#     """
#     template_name = "scienco_home/index.html"

    
# class SiteOneHome(TemplateView):
#     """
#     Site One view for the Print Informations 
#     """
#     template_name = "site1_printing/project/index.html"


# class SiteTwoHome(ListView):
#     """
#     This is SIte 2 Home page and This page is for showing instruments.
#     """
#     context_object_name = "pk"
#     template_name = "site2_instruments/project/index.html"
#     # queryset = HomeImageSlider.objects.all()
#     # product = Product.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super(SiteTwoHome, self).get_context_data(**kwargs)
#         # context["images"] = self.queryset
#         # context['product'] = self.product
#         return context
    


def Home(request):
    return render(request,"scienco_home/index.html")

def SiteOneHome(request):
    return render(request,"site1_printing/project/index.html")


def SiteTwoHome(request):
    context = {
        "data":HomePageData.objects.all()[:1],
        "image_data": HomeImageSlider.objects.all(),
        "instrument" : InstrumentsParametersWise.objects.all()[:6]
    }
    data= HomePageData.objects.all()[:1]
    return render(request,"site2_instrument/project/index.html",context)

