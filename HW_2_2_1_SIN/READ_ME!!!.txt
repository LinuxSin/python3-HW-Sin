 deactivate  # Если вы сейчас в виртуальном окружении, выйдите из него
 rm -rf .venv  # Удалите существующее окружение (осторожно!)
 python3 -m venv .venv  # Создайте новое окружение
 source .venv/bin/activate  # Активируйте окружение
 pip install ipykernel  #  Обязательно установите ipykernel
 pip install jupyter  # Установите jupyter (если еще не установлен)
 jupyter notebook      # Запустите Jupyter Notebook 
