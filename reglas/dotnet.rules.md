# Reglas de Detección: .NET / C#

```yaml
descripcion: "Detección de stack en proyectos .NET"
archivos: ["*.csproj", "*.sln", "global.json"]

# =============================================================================
# VERSIÓN
# =============================================================================
version:
  buscar: "TargetFramework en .csproj"
  mapeo:
    net9.0: ".NET 9"
    net8.0: ".NET 8 (LTS)"
    net7.0: ".NET 7"
    net6.0: ".NET 6 (LTS)"

# =============================================================================
# TIPO DE PROYECTO
# =============================================================================
tipo:
  web: { sdk: "Microsoft.NET.Sdk.Web" }
  worker: { sdk: "Microsoft.NET.Sdk.Worker" }
  blazor: { sdk: "Microsoft.NET.Sdk.BlazorWebAssembly" }
  maui: { sdk: "Microsoft.NET.Sdk.Maui" }
  console: { sdk: "Microsoft.NET.Sdk" }

# =============================================================================
# FRAMEWORKS
# =============================================================================
frameworks:
  aspnet_core: { detectar: "Microsoft.AspNetCore.*", variantes: ["MVC", "Razor Pages", "Minimal API", "Web API"] }
  blazor: { detectar: "Microsoft.AspNetCore.Components", variantes: ["Server", "WebAssembly", "Hybrid"] }
  ef_core: { detectar: "Microsoft.EntityFrameworkCore" }

# =============================================================================
# DEPENDENCIAS CLAVE
# =============================================================================
dependencias:
  cqrs: ["MediatR"]
  mapping: ["AutoMapper", "Mapster"]
  validacion: ["FluentValidation"]
  resiliencia: ["Polly"]
  logging: ["Serilog", "NLog"]
  orm: ["EntityFrameworkCore", "Dapper"]

# =============================================================================
# TESTING
# =============================================================================
testing:
  frameworks: ["xunit", "NUnit", "MSTest"]
  mocking: ["Moq", "NSubstitute", "FakeItEasy"]
  assertions: ["FluentAssertions", "Shouldly"]
  data: ["Bogus", "AutoFixture"]

# =============================================================================
# COMANDOS
# =============================================================================
comandos:
  build: "dotnet build"
  run: "dotnet run"
  test: "dotnet test"
  publish: "dotnet publish"

# =============================================================================
# CONVENCIONES
# =============================================================================
convenciones:
  estructura: "src/, tests/, docs/"
  naming: "PascalCase todo, I prefix interfaces"
        detectar: "AddServerSideBlazor() | MapBlazorHub()"
        significa: "Blazor Server (SignalR)"
      wasm:
        detectar: "Microsoft.AspNetCore.Components.WebAssembly"
        significa: "Blazor WebAssembly (client-side)"
      hybrid:
        detectar: "Microsoft.AspNetCore.Components.WebView"
        significa: "Blazor Hybrid (MAUI/WPF/WinForms)"
  
  ef_core:
    detectar: "Microsoft.EntityFrameworkCore"
    version: "PackageReference Version"
    providers:
      sql_server:
        patron: "Microsoft.EntityFrameworkCore.SqlServer"
        significa: "SQL Server"
      postgresql:
        patron: "Npgsql.EntityFrameworkCore.PostgreSQL"
        significa: "PostgreSQL"
      mysql:
        patron: "Pomelo.EntityFrameworkCore.MySql"
        significa: "MySQL/MariaDB"
      sqlite:
        patron: "Microsoft.EntityFrameworkCore.Sqlite"
        significa: "SQLite"
      cosmos:
        patron: "Microsoft.EntityFrameworkCore.Cosmos"
        significa: "Azure Cosmos DB"
      in_memory:
        patron: "Microsoft.EntityFrameworkCore.InMemory"
        significa: "In-Memory (testing)"
    
    comandos:
      add_migration: "dotnet ef migrations add [Name]"
      update_db: "dotnet ef database update"
      remove_migration: "dotnet ef migrations remove"
      script: "dotnet ef migrations script"
  
  identity:
    detectar: "Microsoft.AspNetCore.Identity"
    variantes:
      identity_core:
        patron: "Microsoft.AspNetCore.Identity.EntityFrameworkCore"
        significa: "ASP.NET Core Identity con EF Core"
      identity_ui:
        patron: "Microsoft.AspNetCore.Identity.UI"
        significa: "Identity con UI scaffolded"
  
  signalr:
    detectar: "Microsoft.AspNetCore.SignalR"
    significa: "Comunicación real-time (WebSockets)"
  
  grpc:
    detectar: "Grpc.AspNetCore"
    significa: "gRPC services"
  
  graphql:
    hot_chocolate:
      detectar: "HotChocolate.AspNetCore"
      significa: "GraphQL con Hot Chocolate"

# =============================================================================
# DEPENDENCIAS CLAVE (NuGet)
# =============================================================================
dependencias_clave:
  arquitectura:
    mediatr:
      patron: "MediatR"
      significa: "Patrón Mediator / CQRS"
    automapper:
      patron: "AutoMapper"
      significa: "Mapeo objeto-objeto"
    mapster:
      patron: "Mapster"
      significa: "Mapeo objeto-objeto (más rápido)"
    fluentvalidation:
      patron: "FluentValidation"
      significa: "Validación fluent"
  
  resiliencia:
    polly:
      patron: "Polly | Microsoft.Extensions.Http.Polly"
      significa: "Retry, Circuit Breaker, Timeout"
    polly_v8:
      patron: "Polly.Core"
      significa: "Polly v8+ (nueva API)"
  
  logging:
    serilog:
      patron: "Serilog | Serilog.AspNetCore"
      significa: "Logging estructurado"
      sinks_comunes:
        - "Serilog.Sinks.Console"
        - "Serilog.Sinks.File"
        - "Serilog.Sinks.Seq"
        - "Serilog.Sinks.ApplicationInsights"
    nlog:
      patron: "NLog"
      significa: "Logging flexible"
  
  orm_alternativo:
    dapper:
      patron: "Dapper"
      significa: "Micro ORM (SQL directo)"
    linq2db:
      patron: "linq2db"
      significa: "LINQ to database"
  
  http_client:
    refit:
      patron: "Refit"
      significa: "REST client type-safe"
    restsharp:
      patron: "RestSharp"
      significa: "REST client clásico"
  
  serializacion:
    newtonsoft:
      patron: "Newtonsoft.Json"
      significa: "JSON.NET (legacy, muy usado)"
    system_text_json:
      patron: "System.Text.Json (built-in)"
      significa: "JSON nativo .NET (recomendado)"
  
  documentacion:
    swashbuckle:
      patron: "Swashbuckle.AspNetCore"
      significa: "Swagger/OpenAPI"
    nswag:
      patron: "NSwag.AspNetCore"
      significa: "OpenAPI alternativo"

# =============================================================================
# TESTING
# =============================================================================
testing:
  frameworks:
    xunit:
      detectar: "xunit"
      config: "xunit.runner.json"
      significa: "Framework de testing principal"
      ejemplo: '<PackageReference Include="xunit" Version="2.6.0" />'
    nunit:
      detectar: "NUnit"
      significa: "Framework de testing alternativo"
    mstest:
      detectar: "MSTest.TestFramework | Microsoft.VisualStudio.TestTools.UnitTesting"
      significa: "Framework de testing de Microsoft"
  
  mocking:
    moq:
      detectar: "Moq"
      significa: "Mocking library principal"
    nsubstitute:
      detectar: "NSubstitute"
      significa: "Mocking alternativo (sintaxis más limpia)"
    fakeiteasy:
      detectar: "FakeItEasy"
      significa: "Mocking alternativo"
  
  assertions:
    fluentassertions:
      detectar: "FluentAssertions"
      significa: "Assertions legibles"
    shouldly:
      detectar: "Shouldly"
      significa: "Assertions alternativas"
  
  datos_prueba:
    bogus:
      detectar: "Bogus"
      significa: "Generación de datos fake"
    autofixture:
      detectar: "AutoFixture"
      significa: "Auto-generación de objetos test"
  
  integracion:
    testcontainers:
      detectar: "Testcontainers"
      significa: "Contenedores para tests de integración"
    webapplicationfactory:
      detectar: "Microsoft.AspNetCore.Mvc.Testing"
      significa: "Testing de integración ASP.NET Core"
    respawn:
      detectar: "Respawn"
      significa: "Reset de base de datos en tests"

  comandos:
    run: "dotnet test"
    run_filter: "dotnet test --filter [TestCategory]"
    run_coverage: "dotnet test --collect:\"XPlat Code Coverage\""

# =============================================================================
# BUILD Y CLI
# =============================================================================
build_tool:
  nombre: "dotnet CLI"
  comandos:
    restore: "dotnet restore"
    build: "dotnet build"
    build_release: "dotnet build -c Release"
    run: "dotnet run"
    run_watch: "dotnet watch run"
    test: "dotnet test"
    publish: "dotnet publish -c Release"
    publish_self_contained: "dotnet publish -c Release --self-contained"
    clean: "dotnet clean"
    add_package: "dotnet add package [PackageName]"
    list_packages: "dotnet list package"
    outdated: "dotnet list package --outdated"
    new: "dotnet new [template]"
    sln_add: "dotnet sln add [project.csproj]"

# =============================================================================
# HERRAMIENTAS DE DESARROLLO
# =============================================================================
dev_tools:
  analyzers:
    stylecop:
      detectar: "StyleCop.Analyzers"
      significa: "Reglas de estilo de código"
    sonaranalyzer:
      detectar: "SonarAnalyzer.CSharp"
      significa: "Análisis de calidad"
    roslynator:
      detectar: "Roslynator.Analyzers"
      significa: "500+ analyzers y refactorings"
    meziantou:
      detectar: "Meziantou.Analyzer"
      significa: "Best practices analyzer"
  
  source_generators:
    detectar: "IncludeAssets=\"runtime; build; native; contentfiles; analyzers\""
    significa: "Uso de Source Generators"
  
  nullable:
    buscar_en: "PropertyGroup > Nullable"
    ejemplo: "<Nullable>enable</Nullable>"
    significa: "Nullable reference types habilitado"
  
  implicit_usings:
    buscar_en: "PropertyGroup > ImplicitUsings"
    ejemplo: "<ImplicitUsings>enable</ImplicitUsings>"
    significa: "Usings implícitos (.NET 6+)"

# =============================================================================
# CONFIGURACIÓN
# =============================================================================
configuracion:
  archivos:
    appsettings: "appsettings.json"
    appsettings_env: "appsettings.{Environment}.json"
    user_secrets: "secrets.json (dev only)"
    launch_settings: "Properties/launchSettings.json"
  
  environments:
    development: "Development"
    staging: "Staging"
    production: "Production"
    variable: "ASPNETCORE_ENVIRONMENT | DOTNET_ENVIRONMENT"

# =============================================================================
# CONVENCIONES DEL ECOSISTEMA
# =============================================================================
convenciones:
  estructura_carpetas:
    web_api:
      - "Controllers/ → API Controllers"
      - "Models/ → DTOs y View Models"
      - "Services/ → Lógica de negocio"
      - "Data/ → DbContext y repositorios"
      - "Middleware/ → Custom middleware"
      - "Extensions/ → Extension methods"
    
    clean_architecture:
      - "Domain/ → Entidades y lógica de dominio"
      - "Application/ → Casos de uso, interfaces"
      - "Infrastructure/ → Implementaciones, DB, externos"
      - "WebApi/ | Presentation/ → Controllers, endpoints"
    
    vertical_slices:
      - "Features/[Feature]/ → Todo relacionado a una feature"
      - "Features/[Feature]/Commands/"
      - "Features/[Feature]/Queries/"
      - "Features/[Feature]/Models/"
  
  archivos_configuracion:
    csproj: "[ProjectName].csproj → Configuración del proyecto"
    sln: "[SolutionName].sln → Solución (múltiples proyectos)"
    global_json: "global.json → Versión SDK"
    nuget_config: "nuget.config → Fuentes NuGet"
    editorconfig: ".editorconfig → Estilo de código"
    gitignore: ".gitignore → Excluir bin/, obj/, etc."
  
  naming:
    clases: "PascalCase (UserService, OrderController)"
    interfaces: "IPascalCase con prefijo I (IUserRepository)"
    metodos: "PascalCase (GetUser, CreateOrder)"
    propiedades: "PascalCase (FirstName, OrderDate)"
    campos_privados: "_camelCase (_userRepository, _logger)"
    parametros: "camelCase (userId, orderItems)"
    constantes: "PascalCase (MaxRetryCount) o UPPER_SNAKE_CASE"
    namespaces: "PascalCase.Separated.By.Dots"
```
