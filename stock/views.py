from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Medicine
from .forms import MedicineForm

# ---------- auth ----------
def login_page(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {"error": "Invalid login"})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

# ---------- dashboard ----------
@login_required
def dashboard(request):
    total = Medicine.objects.count()
    low_stock = Medicine.objects.filter(quantity__lt=10).count()
    return render(request, 'dashboard.html', {
        "total": total,
        "low_stock": low_stock
    })

# ---------- others ----------
@login_required
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'list.html', {"medicines": medicines})

@login_required
def medicine_add(request):
    form = MedicineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('medicine-list')
    return render(request, 'form.html', {"form": form})

@login_required
def medicine_edit(request, pk):
    med = get_object_or_404(Medicine, pk=pk)
    form = MedicineForm(request.POST or None, instance=med)
    if form.is_valid():
        form.save()
        return redirect('medicine-list')
    return render(request, 'form.html', {"form": form})

@login_required
def medicine_delete(request, pk):
    med = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        med.delete()
        return redirect('medicine-list')
    return render(request, 'delete.html', {"medicine": med})
