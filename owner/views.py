import form as form
from django.shortcuts import render,redirect
from owner.forms import BookForm,OrderEditForm
from django.urls import reverse_lazy
from django.views.generic import View,ListView,CreateView,DetailView,UpdateView,TemplateView
from owner.models import Books
from owner.models import Books
from customer.models import Orders
from django.core.mail import send_mail


class AddBook(CreateView):
    model = Books
    form_class = BookForm
    template_name = "add_book.html"
    success_url = reverse_lazy("allbooks")
    # def get(self, request):
    #     form = BookForm()
    #     return render(request, "add_book.html", {"form": form})
    #
    # def post(self, request):
    #     form = BookForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         # print(form.cleaned_data)
    #         # print(form.cleaned_data.get("book_name"))
    #         # print(form.cleaned_data.get("author"))
    #         # print(form.cleaned_data.get("price"))
    #         # print(form.cleaned_data.get("copies"))
    #         #
    #         # qs = Books(book_name=form.cleaned_data.get("book_name"), author=form.cleaned_data.get("author"),
    #         #            amount=form.cleaned_data.get("price"), copies=form.cleaned_data.get("copies"))
    #         # qs.save()
    #
    #         # return render(request, "add_book.html", {"msg": "book created"})
    #         return redirect("allbooks")
    #     else:
    #         return render(request, "add_book.html", {"form": form})

class BookListView(ListView):
    model = Books
    template_name = "book_list.html"
    context_object_name = "books"
    # def get(self,request):
    #     qs=Books.objects.all()
    #     return render(request,'book_list.html',{'books':qs})

class BookDetailView(DetailView):
    model = Books
    template_name = "book_detail.html"
    context_object_name = "book"

    pk_url_kwarg = "id"
    # def get(self,request,*args,**kwargs):
    #     # pass
    #     # kwargs={'id':3}
    #     qs=Books.objects.get(id=kwargs.get("id"))
    #     return render(request,'book_detail.html',{'book':qs})

class BookDelete(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect('allbooks')

class BookChange(UpdateView):
    model = Books
    template_name = "book_edit.html"
    form_class = BookForm
    success_url = reverse_lazy("allbooks")
    pk_url_kwarg = "id"
    # def get(self,request,*args,**kwargs):
    #     qs=Books.objects.get(id=kwargs.get("id"))
    #     form=BookForm(instance=qs)
    #     return render(request,"book_edit.html",{"form":form})
    #
    #
    #
    # def post(self,request,*args,**kwargs):
    #     qs = Books.objects.get(id=kwargs.get("id"))
    #     form = BookForm(request.POST,instance=qs,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("allbooks")
    #

class DashBoardView(TemplateView):
    template_name = "dashboard.html"
    def get(self,request,*args,**kwargs):
        new_orders=Orders.objects.filter(status="orderplaced")
        return render(request,self.template_name,{"new_orders":new_orders})

class OrderDetailView(DetailView):
    model = Orders
    template_name = "order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "id"

class OrderChangeView(UpdateView):
    model = Orders
    template_name = "order_change.html"
    form_class =OrderEditForm
    pk_url_kwarg = "id"

    def post(self,request,*args,**kwargs):
        order=Orders.objects.get(id=kwargs["id"])
        form=OrderEditForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            send_mail(
                'Order Notification',
                'Your Order will be deliverd on',
                'chanduprasad185@gmail.com',
                ['abhijithb2109@gmail.com'],
                fail_silently=False,
            )
            return redirect("dashboard")
