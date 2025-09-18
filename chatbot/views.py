from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Create your views here.
# Chat com Gemini
@login_required
def chat(request):
	user_name = request.user.username
	response = None
	if request.method == 'POST':
		user_message = request.POST.get('message')
		# Exemplo de chamada à API Gemini
		headers = {'Authorization': f'Bearer {GEMINI_API_KEY}'}
		data = {
			'model': 'flash2.0-experimental',
			'messages': [
				{'role': 'system', 'content': 'Você é um recrutador especialista em currículos.'},
				{'role': 'user', 'content': user_message}
			]
		}
		r = requests.post('https://generativelanguage.googleapis.com/v1beta/models/flash2.0-experimental:generateMessage', json=data, headers=headers)
		if r.status_code == 200:
			response = r.json().get('candidates', [{}])[0].get('content', '')
		else:
			response = 'Erro ao conectar à IA.'
	return render(request, 'chat.html', {'response': response, 'user_name': user_name})

# Upload e leitura de PDF
@login_required
def upload_pdf(request):
	# Implementação do upload e leitura do PDF para análise
	return render(request, 'upload_pdf.html')
