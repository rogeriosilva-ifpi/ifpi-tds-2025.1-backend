# Passos para Deploy na Render

## API - Backend (Passo 0)
- Ter API Backend funcionando localmente
- Banco de Dados funcionando integrado com a API
- Testar --> OK

## Github (Passo 1)
- Ter um conta no Github
- Ter o git instalado no computador
- Tornar o Projeto(local) em um Repositório Git(local)
- Criar um Repositório no Github 
- Adicionar o Repositório (Github) como Repositório Remoto no Repositório(Local)
- Subir o código (git push) para Github
  

## Preparar Docker e requirements (Passo 2)
- Adicionar Dockerfile
- Incluir Etapas para Deploy no Dockerfile
- Etapas dependem da Linguagem e Framework
  - Você pode pedir ajudar às IAs para gerar Dockerfile para vc
- Criar arquivo requirements.txt
  - pip freeze > requirements.txt

## Render
- Criar conta na render.com usando sua conta Github
- Criar um Projeto na Render
- Criar novo Serviço (+) --> Web Service
- Configurar Github (escolher Projeto - Repositório)
- Preencher demais campos do Formulário
- Escolher plano Gratuito
- 