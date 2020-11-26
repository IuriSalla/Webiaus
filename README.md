# Webiaus
> _Projeto voltado para Análise de Sentimentos com Polaridade em Nível de Sentença._

<h5> Git Hub (Colaborador): <a href="https://github.com/abyzziboll">Juan Carlos</a></h5>
<h5> Docker Hub (Aplicação): <a href="https://hub.docker.com/repository/docker/iurisalla/devops">Webiaus</a></h5>
  
<p>
  <br />
</p>

### Instalação Docker para a Aplicação

OS X & Linux:

```sh
  apt-get install docker && apt-get install docker-compose
```

### Bibliotecas necessárias

- <a href="https://github.com/IuriSalla/Webiaus/blob/master/docker-compose.yml">Docker-compose.yml</a>
- <a href="https://github.com/IuriSalla/Webiaus/blob/master/Dockerfile">Dockerfile</a>
- <a href="https://github.com/IuriSalla/Webiaus/blob/master/django.txt">Django.txt</a>

### Requisitos para Execução do Software
> Alterar os caminhos absolutos dos arquivos citados abaixo para se ter 100% do software funcionando.

- [Webiaus/blob/master/analisador/AI/base.py](https://github.com/IuriSalla/Webiaus/blob/master/analisador/AI/base.py) - Atentar a linha **20**.
- [Webiaus/blob/master/analisador/AI/gerenciador.py](https://github.com/IuriSalla/Webiaus/blob/master/analisador/AI/gerenciador.py) - Atentar as linhas **27** e **31**.
- [Webiaus/blob/master/analisador/views.py](https://github.com/IuriSalla/Webiaus/blob/master/analisador/views.py) - Atentar a linha **36**.
