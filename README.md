Webiaus
==============

<p>Repositório criado para a aplicação Webiaus e o docker-compose deve ser executado dentro da pasta da aplicação onde contém o arquivo manage.py</p>

<h5> Git Hub (Colaborador): <a href="https://hub.docker.com/repository/docker/iurisalla/devops">Webiaus</a></h5>
<h5> Docker Hub: <a href="https://hub.docker.com/repository/docker/iurisalla/devops">Webiaus</a></h5>

```yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/Webiaus
    ports:
      - "8000:8000"
```
<br>
<p>Abra o navegador no Host e acesse: 127.0.0.1:8000</p>



pip install django-allauth

pip install django-crispy-forms

pip install pandas

pip install xlrd

python manage.py migrate  (SE NECESSÁRIO)

*Rodar no terminal dentro da pasta AI*
pip install -r requerimentos.txt


python

>> import nltk
>> nltk.download()
(baixar 'all')


Docker Hub

>> docker pull iurisalla/devops:latest
