# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import Search
from .kmp import kmp_algorithm, highlight
from .shrek import shrek_text

@login_required(login_url = "/login/")
def index(request):
    form = Search(request.POST or None)
    count = -1

    if request.method == "POST":
        if form.is_valid():
            text = form.cleaned_data.get("text")
            search = form.cleaned_data.get("search")
            pos = kmp_algorithm(text, search)
            count = len(pos)
            res = highlight(text, pos, len(search))
    else:
        form.fields['text'].initial = shrek_text
        res = shrek_text

    return render(request, "home/index.html", {"form": form, "res": res, "count": count})