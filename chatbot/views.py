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
	if 'chat_history' not in request.session:
		request.session['chat_history'] = [
			{'role': 'system', 'content': 'Você é um recrutador especialista em currículos.'}
		]
	chat_history = request.session['chat_history']
	if request.method == 'POST':
		user_message = request.POST.get('message')
		chat_history.append({'role': 'user', 'content': user_message})
		headers = {'Authorization': f'Bearer {GEMINI_API_KEY}'}
		data = {
			'model': 'gemini-2.0-flash-experimental',
			'messages': chat_history
		}
		r = requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-experimental:generateMessage', json=data, headers=headers)
		if r.status_code == 200:
			ai_response = r.json().get('candidates', [{}])[0].get('content', '')
		else:
			ai_response = 'Erro ao conectar à IA.'
		chat_history.append({'role': 'assistant', 'content': ai_response})
		request.session['chat_history'] = chat_history
	# Filtra só mensagens user/assistant para exibir
	display_history = [msg for msg in chat_history if msg['role'] in ['user', 'assistant']]
	return render(request, 'chat.html', {'chat_history': display_history, 'user_name': user_name})

# Upload e leitura de PDF
@login_required
def upload_pdf(request):
	# Implementação do upload e leitura do PDF para análise
	return render(request, 'upload_pdf.html')
