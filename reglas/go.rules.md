# Reglas de Detección: Go

```yaml
descripcion: "Detección de stack en proyectos Go"
archivos: ["go.mod", "go.sum"]

# =============================================================================
# VERSIÓN
# =============================================================================
version:
  buscar: "go X.XX en go.mod | toolchain go1.XX.X"

# =============================================================================
# FRAMEWORKS WEB
# =============================================================================
frameworks:
  gin: { detectar: "github.com/gin-gonic/gin" }
  echo: { detectar: "github.com/labstack/echo" }
  fiber: { detectar: "github.com/gofiber/fiber" }
  chi: { detectar: "github.com/go-chi/chi" }
  stdlib: { detectar: "Sin framework → net/http puro" }

# =============================================================================
# DEPENDENCIAS CLAVE
# =============================================================================
dependencias:
  orm: ["gorm.io/gorm", "github.com/jmoiron/sqlx", "entgo.io/ent"]
  config: ["github.com/spf13/viper", "github.com/knadh/koanf"]
  cli: ["github.com/spf13/cobra", "github.com/urfave/cli"]
  logging: ["go.uber.org/zap", "github.com/rs/zerolog"]
  di: ["github.com/google/wire", "go.uber.org/fx"]
  http: ["github.com/go-resty/resty"]

# =============================================================================
# TESTING
# =============================================================================
testing:
  frameworks: ["testing (stdlib)", "github.com/stretchr/testify"]
  mocking: ["go.uber.org/mock", "github.com/vektra/mockery"]
  integracion: ["github.com/testcontainers/testcontainers-go"]

# =============================================================================
# COMANDOS
# =============================================================================
comandos:
  build: "go build"
  run: "go run ."
  test: "go test ./..."
  lint: "golangci-lint run"

# =============================================================================
# DEPENDENCIAS CLAVE
# =============================================================================
dependencias_clave:
  configuracion:
    viper:
      detectar: "github.com/spf13/viper"
      significa: "Configuración multi-fuente (env, yaml, json, etc.)"
    envconfig:
      detectar: "github.com/kelseyhightower/envconfig"
      significa: "Configuración desde variables de entorno"
    koanf:
      detectar: "github.com/knadh/koanf"
      significa: "Configuración ligera y extensible"
  
  cli:
    cobra:
      detectar: "github.com/spf13/cobra"
      significa: "Framework para CLIs"
    urfave_cli:
      detectar: "github.com/urfave/cli"
      significa: "Framework CLI alternativo"
  
  logging:
    zap:
      detectar: "go.uber.org/zap"
      significa: "Logging estructurado de alto rendimiento"
    zerolog:
      detectar: "github.com/rs/zerolog"
      significa: "Logging JSON de alto rendimiento"
    logrus:
      detectar: "github.com/sirupsen/logrus"
      significa: "Logging estructurado (legacy, aún popular)"
    slog:
      detectar: "log/slog (built-in Go 1.21+)"
      significa: "Logging estructurado estándar"
  
  validacion:
    validator:
      detectar: "github.com/go-playground/validator"
      significa: "Validación de structs con tags"
    ozzo_validation:
      detectar: "github.com/go-ozzo/ozzo-validation"
      significa: "Validación programática"
  
  http_client:
    resty:
      detectar: "github.com/go-resty/resty"
      significa: "Cliente HTTP con sintaxis fluent"
    req:
      detectar: "github.com/imroc/req"
      significa: "Cliente HTTP moderno"
  
  dependency_injection:
    wire:
      detectar: "github.com/google/wire"
      significa: "DI compile-time de Google"
    fx:
      detectar: "go.uber.org/fx"
      significa: "DI framework de Uber"
    dig:
      detectar: "go.uber.org/dig"
      significa: "DI container de Uber (base de fx)"
  
  serialization:
    json_iter:
      detectar: "github.com/json-iterator/go"
      significa: "JSON más rápido que encoding/json"
    easyjson:
      detectar: "github.com/mailru/easyjson"
      significa: "JSON con code generation"
  
  uuid:
    google_uuid:
      detectar: "github.com/google/uuid"
      significa: "UUIDs de Google"
    gofrs_uuid:
      detectar: "github.com/gofrs/uuid"
      significa: "UUIDs alternativo"
  
  errores:
    pkg_errors:
      detectar: "github.com/pkg/errors"
      significa: "Error wrapping (pre Go 1.13)"
      nota: "Go 1.13+ tiene fmt.Errorf con %w"
    cockroachdb_errors:
      detectar: "github.com/cockroachdb/errors"
      significa: "Error handling avanzado"

# =============================================================================
# TESTING
# =============================================================================
testing:
  standard:
    detectar: "testing (built-in)"
    significa: "Package testing estándar"
    archivos: "*_test.go"
    comandos:
      run: "go test ./..."
      verbose: "go test -v ./..."
      coverage: "go test -cover ./..."
      coverage_html: "go test -coverprofile=coverage.out && go tool cover -html=coverage.out"
      race: "go test -race ./..."
      bench: "go test -bench=. ./..."
  
  testify:
    detectar: "github.com/stretchr/testify"
    significa: "Assertions y mocks populares"
    subpaquetes:
      assert: "Assertions que no detienen el test"
      require: "Assertions que detienen el test"
      mock: "Mocking framework"
      suite: "Test suites"
  
  gomock:
    detectar: "github.com/golang/mock | go.uber.org/mock"
    significa: "Mocking con code generation"
    nota: "go.uber.org/mock es el fork mantenido"
  
  mockery:
    detectar: "github.com/vektra/mockery"
    significa: "Generador de mocks para interfaces"
  
  ginkgo:
    detectar: "github.com/onsi/ginkgo"
    significa: "BDD testing framework"
    complemento: "github.com/onsi/gomega (matchers)"
  
  goconvey:
    detectar: "github.com/smartystreets/goconvey"
    significa: "BDD con UI web"
  
  testcontainers:
    detectar: "github.com/testcontainers/testcontainers-go"
    significa: "Contenedores para integration tests"
  
  httptest:
    detectar: "net/http/httptest (built-in)"
    significa: "Testing de HTTP handlers"

# =============================================================================
# BUILD Y HERRAMIENTAS
# =============================================================================
build_tool:
  nombre: "go CLI"
  comandos:
    build: "go build"
    build_output: "go build -o [binary_name]"
    run: "go run ."
    test: "go test ./..."
    mod_init: "go mod init [module_path]"
    mod_tidy: "go mod tidy"
    mod_download: "go mod download"
    mod_vendor: "go mod vendor"
    fmt: "go fmt ./..."
    vet: "go vet ./..."
    generate: "go generate ./..."
    install: "go install"
    get: "go get [package]"
    work_init: "go work init (workspaces)"

  cross_compile:
    linux: "GOOS=linux GOARCH=amd64 go build"
    windows: "GOOS=windows GOARCH=amd64 go build"
    mac_intel: "GOOS=darwin GOARCH=amd64 go build"
    mac_arm: "GOOS=darwin GOARCH=arm64 go build"

# =============================================================================
# HERRAMIENTAS DE DESARROLLO
# =============================================================================
dev_tools:
  linting:
    golangci_lint:
      detectar: ".golangci.yml | .golangci.yaml"
      significa: "Meta-linter (incluye múltiples linters)"
      comando: "golangci-lint run"
    staticcheck:
      detectar: "honnef.co/go/tools/cmd/staticcheck"
      significa: "Análisis estático avanzado"
    golint:
      nota: "Deprecated, usar golangci-lint"
  
  formateo:
    gofmt: "go fmt (built-in)"
    goimports: "golang.org/x/tools/cmd/goimports"
    gofumpt: "mvdan.cc/gofumpt (stricter formatting)"
  
  code_generation:
    go_generate: "//go:generate directive"
    stringer: "golang.org/x/tools/cmd/stringer (enum strings)"
    mockgen: "Generación de mocks"
    sqlc: "SQL to Go code"
    wire: "DI code generation"
  
  hot_reload:
    air:
      detectar: ".air.toml"
      significa: "Live reload para desarrollo"
      comando: "air"
    reflex:
      significa: "File watcher alternativo"

# =============================================================================
# CONVENCIONES DEL ECOSISTEMA
# =============================================================================
convenciones:
  estructura_carpetas:
    standard_layout:
      - "cmd/[app]/ → Entry points (main.go)"
      - "internal/ → Código privado del módulo"
      - "pkg/ → Código público reutilizable"
      - "api/ → Definiciones OpenAPI, proto, etc."
      - "configs/ → Archivos de configuración"
      - "scripts/ → Scripts de build, CI, etc."
      - "test/ → Tests adicionales (e2e, fixtures)"
      - "docs/ → Documentación"
      - "tools/ → Herramientas de soporte"
    
    simple:
      - "main.go → Entry point"
      - "handler.go, service.go, repo.go → Por responsabilidad"
      - "*_test.go → Tests junto al código"
    
    domain_driven:
      - "domain/ → Entidades y lógica de negocio"
      - "application/ → Casos de uso"
      - "infrastructure/ → Implementaciones externas"
      - "interfaces/ → Handlers HTTP, CLI, etc."
  
  archivos_configuracion:
    go_mod: "go.mod → Dependencias del módulo"
    go_sum: "go.sum → Checksums de dependencias"
    go_work: "go.work → Workspace multi-módulo"
    golangci: ".golangci.yml → Configuración linter"
    air: ".air.toml → Hot reload config"
    goreleaser: ".goreleaser.yml → Release automation"
  
  naming:
    paquetes: "lowercase, singular (user, order, not users)"
    archivos: "lowercase, snake_case (user_handler.go)"
    interfaces: "PascalCase con sufijo '-er' si es posible (Reader, Writer, UserService)"
    structs: "PascalCase (User, OrderService)"
    funciones_publicas: "PascalCase (GetUser, CreateOrder)"
    funciones_privadas: "camelCase (getUserFromDB)"
    constantes: "PascalCase o camelCase (MaxRetries, defaultTimeout)"
    variables: "camelCase (userID, orderItems)"
    
  idioms:
    error_handling: |
      if err != nil {
          return fmt.Errorf("context: %w", err)
      }
    interface_check: "var _ Interface = (*Struct)(nil)"
    constructor: "func NewService(deps) *Service"
```
