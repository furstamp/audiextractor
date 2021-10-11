# Importando Módulos
# Módulo Utilizado > MoviePy
# Instalação > pip install moviepy

import moviepy.editor as mp


# Nesta linha, estaremos copiando a amostra do vídeo na pasta do projeto e definindo o arquivo de vídeo no código.

video = mp.VideoFileClip(r"video.mp4")


# Já nesta, é a conversão de vídeo para o áudio em si ( mp4 -> mp3 ).

video.audio.write_audiofile(r"audio.mp3")
