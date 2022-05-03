# t_schule

## Cloud mode


Открываем [cloud.google.com](https://cloud.google.com/free) - если есть гугл-аккаунт, будет открыта консоль

Клонируем репозиторий с кодом и данными
```shell
git clone https://github.com/aleksandr-dzhumurat/t_schule.git
```


Сборка контейнера

```shell
make build
```

Тренировка модели
```shell
make train
```

Запуск Flask интерфейса
```shell
make run-flask
```

Проверка, что работает API

```shell
make test-flask
```

## Local mode

### Mac

Для локального запуска нужно добавить системные пакеты (иначе некорректно соберётся python-окружение)
```shell
brew install openssl xz gdbm
```

Затем создаём виртуальное окружение

```shell
pyenv install 3.8.10 && \
pyenv virtualenv 3.8.10 hse-env
```

Далее активируем окружение
```shell
source ~/.pyenv/versions/hse-env/bin/activate
```

После активации устанавлеваем зависимости
```shell
pip install -r requirements.txt
```

