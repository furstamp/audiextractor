# Extrator de Áudio

## Descrição

Projeto feito em Python usando ffmpeg e moviepy. Extraia áudios de seus vídeos, basta declarar o nome e tipo de arquivo de ambos.

## Utilizando as Libraries

Packages utilizadas nesse projeto ->

- MoviePy - É um Python Module utilizado para edição de vídeos, onde pode ser utilizado para operações básicas, composições, processamentos e criação de efeitos avançados.

- FFmpeg - É um projeto de software open-source gratuíto que mexe com vídeos, áudios, e outros arquivos. Designado para processamento de arquivos de vídeos e áudios.


### Instalando Packages

MoviePy
~~~
pip install moviepy
~~~

FFmpeg
~~~py
pip install ffmpeg
~~~

### Importando as Packages

Importando o módulo moviepy
~~~py
import moviepy.editor as mp
~~~

## Executando o Código

Copiar a amostra do vídeo na pasta do projeto e definir o arquivo de vídeo no código. Utilizando a função VideoFileClip(), se consegue fazer isso.

~~~py
video = mp.VideoFileClip(r"video.mp4") # r indica que estamos lendo um arquivo
~~~

Parte de conversão de vídeo ( .mp4 ) para áudio ( .mp3 ). Basta declarar o nome do arquivo em si.

~~~py
video.audio.write_audiofile(r"audio.mp3") # r = lendo arquivo
~~~
