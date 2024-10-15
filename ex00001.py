larg = float(input('Qual a largura? '))
altu = float(input('Qual a altura? '))
Total = larg * altu
print('A area da parede é de {:.2f} e o valor do trabalho vai ficar em {:.2f}R$ e vou precisar de {:.2f} litros de tinta'.format(Total,(Total*1.95),(Total/3.5)))




#Passo a passo para enviar um repositório ao GitHub
#1. Configurar seu usuário no Git (Apenas uma vez)
#Configura o seu nome e e-mail, que aparecerão nos commits.
#bash
#Copiar código
#git config --global user.name "SeuNome"
#git config --global user.email "seuemail@email.com"
#2. Criar um repositório local
#Entre na pasta do projeto:
#bash
#Copiar código
#cd caminho/para/seu/projeto
#Inicialize o repositório:
#bash
#Copiar código
#git init
#3. Adicionar arquivos ao repositório
#Adicionar todos os arquivos:
#bash
#Copiar código
#git add .
#Adicionar um arquivo específico:
#bash
#Copiar código
#git add nome_do_arquivo.ext
#4. Fazer um commit
#O commit salva suas alterações localmente.
#bash
#Copiar código
#git commit -m "Primeiro commit"
#5. Criar um repositório no GitHub
#Vá para o GitHub e crie um repositório novo.
#Copie a URL do repositório recém-criado (será algo como https://github.com/usuario/repositorio.git).
#6. Adicionar o repositório remoto
#Vincule seu repositório local ao GitHub usando a URL copiada.
#bash
#Copiar código
#git remote add origin https://github.com/usuario/repositorio.git
#7. Enviar o repositório para o GitHub
#Use o comando git push para enviar seu código.
#bash
#Copiar código
#git push -u origin main
#Obs: Se o branch principal do GitHub for master e não main, ajuste o comando assim:
#bash
#Copiar código
#git push -u origin master
#8. Comandos úteis adicionais
#Clonar um repositório (baixar para sua máquina):
#bash
#Copiar código
#git clone https://github.com/usuario/repositorio.git
#Verificar status dos arquivos (se foram modificados ou não adicionados):
#bash
#Copiar código
#git status
#Verificar histórico de commits:
#bash
#Copiar código
#git log
#Agora você tem um fluxo básico para criar e enviar repositórios ao GitHub! Se algum passo der erro ou se precisar de ajuda em outro ponto, é só avisar.