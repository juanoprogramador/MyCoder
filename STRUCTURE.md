# STRUCTURE.md

## Estrutura Geral

```text
MyCoder/
│
├── docs/
│   ├── VISION.md
│   ├── ROADMAP.md
│   ├── STRUCTURE.md
│   └── ARCHITECTURE.md
│
├── mycoder/
│   │
│   ├── app.py
│   │
│   ├── core/
│   │   ├── commands/
│   │   ├── events/
│   │   ├── settings/
│   │   ├── i18n/
│   │   ├── workspace/
│   │   ├── terminal/
│   │   ├── git/
│   │   └── plugins/
│   │
│   ├── ui/
│   │   ├── palette/
│   │   ├── sidebar/
│   │   ├── editor/
│   │   ├── statusbar/
│   │   └── splash/
│   │
│   ├── assets/
│   │   ├── banners/
│   │   └── themes/
│   │
│   └── locales/
│       ├── en_US/
│       ├── pt_BR/
│       └── future_languages/
│
├── tests/
│
├── plugins/
│
├── pyproject.toml
│
├── README.md
│
└── main.py
```

## Responsabilidades

### docs/

Contém toda a documentação oficial do projeto.

Nenhum código-fonte deve ficar neste diretório.

### mycoder/core/

Contém toda a lógica central do sistema.

O Core não deve depender da interface gráfica ou textual.

O Core deve ser reutilizável independentemente da tecnologia de interface utilizada.

### mycoder/core/commands/

Responsável pelo registro e execução de comandos.

Exemplos:

* open_file
* save_file
* git_status
* open_terminal

### mycoder/core/events/

Sistema de eventos internos.

Permite comunicação desacoplada entre módulos.

### mycoder/core/settings/

Gerenciamento de configurações.

Responsável por carregar, validar e salvar preferências do usuário.

### mycoder/core/i18n/

Sistema de internacionalização.

Responsável por traduções e localização.

### mycoder/core/workspace/

Representação do projeto atualmente aberto.

Responsável por indexação de arquivos e informações do workspace.

### mycoder/core/terminal/

Integração com o terminal embutido.

### mycoder/core/git/

Integração nativa com Git.

### mycoder/core/plugins/

Sistema de carregamento e gerenciamento de plugins.

### mycoder/ui/

Contém todos os componentes visuais construídos com Textual.

Nenhuma regra de negócio deve existir aqui.

### mycoder/ui/palette/

Implementação da Command Palette.

### mycoder/ui/sidebar/

Painel lateral contextual.

### mycoder/ui/editor/

Widgets relacionados à edição de código.

### mycoder/ui/statusbar/

Barra de status.

### mycoder/ui/splash/

Tela de inicialização e banners ASCII.

### mycoder/assets/

Recursos estáticos.

### mycoder/assets/banners/

Fontes ASCII e banners de inicialização.

### mycoder/assets/themes/

Temas visuais.

### mycoder/locales/

Arquivos de tradução.

### plugins/

Plugins instalados pelo usuário ou distribuídos separadamente do Core.

### tests/

Testes automatizados.

Toda funcionalidade crítica deve possuir testes.

## Regras Arquiteturais

1. O Core não depende da UI.

2. A UI pode utilizar o Core.

3. Plugins não podem modificar arquivos internos do Core.

4. Toda funcionalidade deve ser acessível pela Command Palette.

5. Toda configuração deve possuir representação em arquivo.

6. Linux e Termux são plataformas de referência.

7. O teclado é o principal método de interação.
