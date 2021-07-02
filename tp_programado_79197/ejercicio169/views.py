import random, math
from django.shortcuts import render
from django.views import generic
from .forms import ParametersForm

# Create your views here.


def index(request):
    return render(request, "index.html")


def acercade(request):
    return render(request, "acercade.html")


class Simulacion(generic.FormView):
    form_class = ParametersForm
    template_name = 'ejercicio169.html'

    def form_valid(self, form):
        t0 = form.cleaned_data['t0']
        t1 = form.cleaned_data['t1']
        t2 = form.cleaned_data['t2']
        p_0 = form.cleaned_data['P0']
        p_1 = form.cleaned_data['P1']
        p_2 = form.cleaned_data['P2']
        T = form.cleaned_data['T']

        e_a = (p_0 * (p_2 - p_1)) / (p_2 * (p_1 - p_0))
        a_sobre_b = round((p_1*((p_0*p_1)-2*p_0*p_2+p_1*p_2))/(p_1*p_1-p_0*p_2))

        ta = t1-t0
        tb = t2-t1

        t = 0
        tt = t0
        if T < t0:
            while tt != T:
                tt -= 1
                t -= 1 / ta
        elif T > t0:
            while tt != T:
                tt += 1
                t += 1/ta

        t = round(t, 2)
        resultado = round(a_sobre_b / ((1 + (((a_sobre_b / p_0) - 1) * e_a**t))))

        return render(self.request, self.template_name, {"e_a": e_a, "a_sobre_b": a_sobre_b, "ta": ta, "tb": tb, "T": T,
                                                         "t": t, "resultado": resultado})
