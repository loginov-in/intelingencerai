import os
from dotenv import load_dotenv


# Загружаем переменные из .env файла.
# Это позволяет запускать приложение локально без Docker,
# прочитав конфигурацию из файла .env.
load_dotenv()


SECRET_KEY=os.environ["SECRET_KEY"]