# Webiaus
> _Projeto voltado para Análise de Sentimentos com Polaridade em Nível de Sentença._

[Colaborador](https://github.com/abyzziboll)

<h5> Git Hub (Colaborador): <a href="https://github.com/abyzziboll">Juan Carlos</a></h5>
<h5> Docker Hub (Aplicação): <a href="https://hub.docker.com/repository/docker/iurisalla/devops">Webiaus</a></h5>



<p>docker-compose:<a href="https://github.com/IuriSalla/Webiaus/blob/master/Dockerfile">docker-compose.yml</a></p>
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
