# Reglas de Detección: Python

```yaml
descripcion: "Detección de stack en proyectos Python"
archivos: ["pyproject.toml", "requirements.txt", "Pipfile", "setup.py"]

# =============================================================================
# GESTOR DE DEPENDENCIAS
# =============================================================================
gestor:
  poetry: { lock: "poetry.lock", install: "poetry install", run: "poetry run" }
  pip: { lock: "requirements.txt", install: "pip install -r requirements.txt" }
  pipenv: { lock: "Pipfile.lock", install: "pipenv install", run: "pipenv run" }
  uv: { lock: "uv.lock", install: "uv pip install", run: "uv run" }

# =============================================================================
# VERSIÓN
# =============================================================================
version:
  buscar: "requires-python | tool.poetry.dependencies.python | .python-version"

# =============================================================================
# FRAMEWORKS WEB
# =============================================================================
frameworks:
  django: { detectar: "django", tipo: "fullstack", config: "manage.py" }
  fastapi: { detectar: "fastapi", tipo: "api", server: "uvicorn | hypercorn" }
  flask: { detectar: "flask", tipo: "micro" }
  starlette: { detectar: "starlette", tipo: "async" }
  litestar: { detectar: "litestar", tipo: "async" }

# =============================================================================
# DEPENDENCIAS CLAVE
# =============================================================================
dependencias:
  orm: ["sqlalchemy", "django ORM", "tortoise-orm", "sqlmodel"]
  validacion: ["pydantic", "marshmallow", "attrs"]
  tareas: ["celery", "rq", "dramatiq", "arq"]
  api: ["djangorestframework", "django-ninja", "graphene"]
  http: ["httpx", "requests", "aiohttp"]

# =============================================================================
# TESTING
# =============================================================================
testing:
  frameworks: ["pytest", "unittest"]
  plugins: ["pytest-cov", "pytest-asyncio", "pytest-django"]
  mocking: ["pytest-mock", "factory-boy", "faker"]

# =============================================================================
# CONVENCIONES
# =============================================================================
convenciones:
  estructura: "src/[proyecto]/, tests/, scripts/"
  naming: "snake_case archivos y funciones, PascalCase clases"
        patron: "channels"
        significa: "WebSockets"
      django_allauth:
        patron: "django-allauth"
        significa: "Autenticación social"
    
    comandos:
      run: "python manage.py runserver"
      migrate: "python manage.py migrate"
      makemigrations: "python manage.py makemigrations"
      shell: "python manage.py shell"
      test: "python manage.py test"
  
  fastapi:
    detectar: "fastapi en dependencias"
    version: "fastapi==X.X.X"
    ejemplo: 'fastapi = "^0.109.0"'
    dependencias_asociadas:
      uvicorn:
        patron: "uvicorn"
        significa: "Servidor ASGI (requerido)"
      hypercorn:
        patron: "hypercorn"
        significa: "Servidor ASGI alternativo"
      pydantic:
        patron: "pydantic"
        significa: "Validación de datos (incluido)"
    
    comandos:
      run: "uvicorn main:app --reload"
      run_prod: "uvicorn main:app --host 0.0.0.0 --port 8000"
  
  flask:
    detectar: "flask | Flask en dependencias"
    version: "flask==X.X.X"
    ejemplo: 'flask = "^3.0"'
    dependencias_comunes:
      flask_restful:
        patron: "flask-restful"
        significa: "API REST"
      flask_sqlalchemy:
        patron: "flask-sqlalchemy"
        significa: "ORM integration"
      flask_login:
        patron: "flask-login"
        significa: "Autenticación"
      flask_migrate:
        patron: "flask-migrate"
        significa: "Migraciones DB"
    
    comandos:
      run: "flask run"
      run_debug: "flask run --debug"
  
  litestar:
    detectar: "litestar en dependencias"
    significa: "Litestar - Framework ASGI moderno (antes Starlite)"
  
  aiohttp:
    detectar: "aiohttp en dependencias"
    significa: "Framework HTTP asíncrono"
  
  sanic:
    detectar: "sanic en dependencias"
    significa: "Framework async de alto rendimiento"

# =============================================================================
# ORMs Y BASES DE DATOS
# =============================================================================
persistencia:
  sqlalchemy:
    detectar: "sqlalchemy | SQLAlchemy"
    significa: "SQLAlchemy - ORM completo"
    version_2: "Buscar sqlalchemy>=2.0 para nueva API"
    dependencias_asociadas:
      alembic:
        patron: "alembic"
        significa: "Migraciones de DB"
    comandos:
      migrate_init: "alembic init alembic"
      migrate_create: "alembic revision --autogenerate -m 'message'"
      migrate_up: "alembic upgrade head"
  
  tortoise:
    detectar: "tortoise-orm"
    significa: "Tortoise ORM - Async ORM inspirado en Django"
  
  sqlmodel:
    detectar: "sqlmodel"
    significa: "SQLModel - SQLAlchemy + Pydantic (por creador de FastAPI)"
  
  peewee:
    detectar: "peewee"
    significa: "Peewee - ORM simple y ligero"
  
  django_orm:
    detectar: "django (incluido)"
    significa: "Django ORM - Incluido en Django"
  
  motor:
    detectar: "motor"
    significa: "Motor - Driver async para MongoDB"
  
  beanie:
    detectar: "beanie"
    significa: "Beanie - ODM async para MongoDB con Pydantic"
  
  odmantic:
    detectar: "odmantic"
    significa: "ODMantic - ODM para MongoDB"

# =============================================================================
# DEPENDENCIAS COMUNES
# =============================================================================
dependencias_clave:
  validacion:
    pydantic:
      patron: "pydantic"
      significa: "Validación de datos con tipado"
      v2: "pydantic>=2.0 para nueva versión"
    marshmallow:
      patron: "marshmallow"
      significa: "Serialización/validación"
    cerberus:
      patron: "cerberus"
      significa: "Validación de schemas"
  
  http_clients:
    httpx:
      patron: "httpx"
      significa: "Cliente HTTP async/sync moderno"
    requests:
      patron: "requests"
      significa: "Cliente HTTP sync (clásico)"
    aiohttp_client:
      patron: "aiohttp"
      significa: "Cliente HTTP async"
  
  tareas_async:
    celery:
      patron: "celery"
      significa: "Cola de tareas distribuidas"
    rq:
      patron: "rq"
      significa: "Redis Queue - Tareas simples"
    dramatiq:
      patron: "dramatiq"
      significa: "Cola de tareas alternativa a Celery"
    arq:
      patron: "arq"
      significa: "Cola de tareas async con Redis"
  
  cache:
    redis:
      patron: "redis"
      significa: "Cliente Redis"
    aiocache:
      patron: "aiocache"
      significa: "Cache async multi-backend"
  
  utilidades:
    python_dotenv:
      patron: "python-dotenv"
      significa: "Carga de variables .env"
    pydantic_settings:
      patron: "pydantic-settings"
      significa: "Configuración con Pydantic v2"
    tenacity:
      patron: "tenacity"
      significa: "Retries con backoff"
    structlog:
      patron: "structlog"
      significa: "Logging estructurado"
    loguru:
      patron: "loguru"
      significa: "Logging simplificado"

# =============================================================================
# TESTING
# =============================================================================
testing:
  pytest:
    detectar: "pytest"
    config: "pytest.ini | pyproject.toml [tool.pytest]"
    significa: "Framework de testing principal"
    plugins_comunes:
      pytest_cov:
        patron: "pytest-cov"
        significa: "Coverage"
      pytest_asyncio:
        patron: "pytest-asyncio"
        significa: "Tests async"
      pytest_mock:
        patron: "pytest-mock"
        significa: "Mocking simplificado"
      pytest_xdist:
        patron: "pytest-xdist"
        significa: "Tests paralelos"
      pytest_django:
        patron: "pytest-django"
        significa: "Integración Django"
    comandos:
      run: "pytest"
      run_verbose: "pytest -v"
      run_coverage: "pytest --cov=src"
  
  unittest:
    detectar: "import unittest (built-in)"
    significa: "Framework estándar de Python"
    comandos:
      run: "python -m unittest discover"
  
  hypothesis:
    detectar: "hypothesis"
    significa: "Property-based testing"
  
  factory_boy:
    detectar: "factory-boy"
    significa: "Test factories para modelos"
  
  faker:
    detectar: "faker"
    significa: "Generación de datos fake"
  
  responses:
    detectar: "responses"
    significa: "Mock de requests HTTP"
  
  respx:
    detectar: "respx"
    significa: "Mock de httpx"

# =============================================================================
# HERRAMIENTAS DE DESARROLLO
# =============================================================================
dev_tools:
  linting:
    ruff:
      detectar: "ruff"
      config: "ruff.toml | pyproject.toml [tool.ruff]"
      significa: "Linter ultrarrápido (reemplaza flake8, isort, etc.)"
    flake8:
      detectar: "flake8"
      config: ".flake8 | setup.cfg"
      significa: "Linter clásico"
    pylint:
      detectar: "pylint"
      significa: "Linter exhaustivo"
  
  formateo:
    black:
      detectar: "black"
      config: "pyproject.toml [tool.black]"
      significa: "Formatter opinado"
    isort:
      detectar: "isort"
      significa: "Ordenador de imports"
    ruff_format:
      detectar: "ruff (incluye formatter)"
      significa: "Formatter compatible con Black"
  
  type_checking:
    mypy:
      detectar: "mypy"
      config: "mypy.ini | pyproject.toml [tool.mypy]"
      significa: "Type checker estático"
    pyright:
      detectar: "pyright"
      significa: "Type checker de Microsoft"
  
  pre_commit:
    detectar: "pre-commit"
    config: ".pre-commit-config.yaml"
    significa: "Git hooks automatizados"

# =============================================================================
# COMANDOS COMUNES
# =============================================================================
comandos_build:
  poetry:
    install: "poetry install"
    run: "poetry run python"
    test: "poetry run pytest"
    build: "poetry build"
  
  pip:
    install: "pip install -r requirements.txt"
    install_editable: "pip install -e ."
    run: "python"
    test: "pytest"

# =============================================================================
# CONVENCIONES DEL ECOSISTEMA
# =============================================================================
convenciones:
  estructura_carpetas:
    proyecto_moderno:
      - "src/[package_name]/ → Código fuente"
      - "tests/ → Tests"
      - "docs/ → Documentación"
      - "scripts/ → Scripts auxiliares"
    
    django:
      - "[project_name]/ → Configuración principal"
      - "[app_name]/ → Apps de Django"
      - "templates/ → Templates HTML"
      - "static/ → Archivos estáticos"
      - "media/ → Uploads de usuarios"
    
    fastapi:
      - "app/ → Aplicación principal"
      - "app/api/ → Endpoints"
      - "app/core/ → Configuración"
      - "app/models/ → Modelos"
      - "app/schemas/ → Pydantic schemas"
      - "app/services/ → Lógica de negocio"
  
  archivos_configuracion:
    pyproject: "pyproject.toml → Configuración moderna (PEP 518/621)"
    setup: "setup.py → Configuración legacy"
    requirements: "requirements.txt → Dependencias pip"
    env: ".env → Variables de entorno"
    gitignore: ".gitignore → Excluir __pycache__, .venv, etc."
  
  naming:
    modulos: "snake_case (user_service.py)"
    clases: "PascalCase (UserService, OrderModel)"
    funciones: "snake_case (get_user, create_order)"
    constantes: "UPPER_SNAKE_CASE (MAX_RETRIES, API_KEY)"
    variables: "snake_case (user_id, order_items)"
```
