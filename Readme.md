# Desafio Tecnico WPensar

## Implementação:

- Clonar projeto.
- Criar a virtual env `virtualenv -p python3 .vEnv`
- Ativar o virtualização `..vEnv/bin/activate`
- Instalar django `pip install -r requirements-dev.txt`

- Adicionar `cotacao` e `accounts` ao INSTALLED_APPS em Settings.

- Rodar `python manage.py makemigrations` e em seguida `python manage.py migrate`
- Criar o usuario admin com `python manage.py createsuperuser` e seguir o que se pede.
- Rodar `pyhton manage.py runserver`, pronto sua aplicação esta rodando.