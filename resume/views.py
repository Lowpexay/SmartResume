from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.
# Formulário de currículo
@login_required
def resume_form(request):
	if request.method == 'POST':
		form = ResumeForm(request.POST)
		if form.is_valid():
			request.session['resume_data'] = form.cleaned_data
			return redirect('generate_pdf')
	else:
		form = ResumeForm()
	return render(request, 'resume_form.html', {'form': form})

# Geração de PDF
@login_required
def generate_pdf(request):
	data = request.session.get('resume_data')
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="curriculo.pdf"'
	p = canvas.Canvas(response)
	p.setFont("Helvetica", 14)
	p.drawString(100, 800, f"Nome: {data.get('name', '')}")
	p.drawString(100, 780, f"Email: {data.get('email', '')}")
	p.drawString(100, 760, f"Resumo: {data.get('summary', '')}")
	p.showPage()
	p.save()
	return response
