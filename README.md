# APIREST para um pequeno MVP

Voce poderá fazer publicações de cotacões para peças especifícas de droids, bem como fazer a manutenção e remoção delas. 

Para utilizar o repositorio localmente, utilizar:

git clone https://github.com/andresoareez/mvp-test.git
pip -r install requirements.txt
python manage.py runserver

Você pode utilizar criar um novo superuser com o comando
python manage.py creatersuperuser

ou usar o usuario pré cadastrado

login: mainadmin
senha: mainadmin

No repositório ha uma collections de requests para utilização da API

O docker-compose pode ser utilizado juntamente com o docker file utilizando o comando 
docker-compose up

Em development poderá ser encontrada uma melhor descricao da aplicação
