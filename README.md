# Site checker
Este é um programa em Python que verifica se um site está online ou offline. Ele recebe um argumento com o nome do site na linha de comando e retorna a resposta "o site está online" ou "o site está offline". O programa também salva os resultados juntamente com a hora da verificação no arquivo "output.txt".

## Como Usar

### Verificação de um único site
Para verificar um único site, basta executar o programa com o nome do site como argumento. Por exemplo:

<strong>python __main___.py -u example.com</strong>

Isso irá verificar se o site example.com está online ou offline e retornará a resposta correspondente na linha de comando. Além disso, o resultado será salvo no arquivo "output.txt".

### Verificação de vários sites a partir de um arquivo

Para verificar vários sites de uma só vez, crie um arquivo CSV com a lista de URLs a serem verificados. 
Em seguida, execute o programa com o nome do arquivo CSV como argumento. Por exemplo:
<strong>python site_checker.py -f urls.csv</strong>

Isso irá verificar cada URL no arquivo e retornar a resposta correspondente na linha de comando. Além disso, os resultados serão salvos no arquivo "output.txt".

## Programação do cronjob
o Arquivo .sh presente nesse repositório conta com o código para programar o cronjob para executar o verificador a cada 24 horas, mas <strong>Atenção!!</strong> é necessário modificar o caminho dentro do arquivo para o python e o arquivo "__main__.py" poder ser executados corretamente

O arquivo está inicialmente setado para ler o aquivo "urls.csv" que está de exemplo nesse repositório, para modificalo basta seguir as instruções na seção anterior. 

