```text
███╗   ███╗██╗   ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗
████╗ ████║╚██╗ ██╔╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██╔████╔██║ ╚████╔╝ ██║     ██║   ██║██║  ██║█████╗  ██████╔╝
██║╚██╔╝██║  ╚██╔╝  ██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║   ██║   ╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
╚═╝     ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

[ TERMINAL-FIRST IDE ]
[ KEYBOARD-FIRST WORKFLOW ]
[ BUILT FOR PEOPLE WHO BUILD THEIR OWN TOOLS ]
```

# MyCoder

> A terminal-first IDE for developers who want complete control over their environment.

MyCoder is an open-source terminal IDE focused on speed, customization, transparency, and freedom. It is designed for developers who prefer understanding and shaping their tools rather than adapting to opaque software ecosystems.

Inspired by the philosophy of terminal applications, hacker culture, and highly configurable development environments, MyCoder aims to become a powerful workspace that feels native inside the terminal.

---

## Philosophy

```text
┌─────────────────────────────────────────────┐
│ Optimization                                │
│ Customization                               │
│ Integration                                 │
│ Freedom                                     │
└─────────────────────────────────────────────┘
```

MyCoder follows a few fundamental principles:

* Terminal-first
* Keyboard-first
* Project-aware
* Plugin-driven
* Open-source
* Minimal by default
* Highly configurable

The editor should adapt to the developer.

Not the other way around.

---

## Current Workflow

```bash
cd my_project
mycoder
```

The current directory automatically becomes the active workspace.

No project import.

No setup wizard.

No unnecessary clicks.

---

## Design Goals

```text
[✓] Fast startup
[✓] Lightweight architecture
[✓] Native terminal experience
[✓] Git integration
[✓] Integrated terminal
[✓] Command Palette-centric workflow
[✓] Extensible plugin system
[✓] Cross-platform ambitions
```

Reference platforms:

```text
Linux
Termux
```

Future support:

```text
Windows
macOS
```

---

## Planned Interface

```text
╔══════════════════════════════════════════════╗
║                                              ║
║                 MYCODER                      ║
║                                              ║
║ Workspace: ~/projects/mycoder                ║
║                                              ║
║ > git                                        ║
║                                              ║
║ git status                                   ║
║ git branch                                   ║
║ git commit                                   ║
║                                              ║
╚══════════════════════════════════════════════╝
```

Everything should be accessible through the Command Palette.

---

## Architecture Vision

```text
MyCoder
│
├── Core
│   ├── Commands
│   ├── Events
│   ├── Settings
│   ├── Workspace
│   ├── Terminal
│   ├── Git
│   └── Plugins
│
├── UI
│   ├── Home
│   ├── Editor
│   ├── Sidebar
│   └── StatusBar
│
└── Community Extensions
```

The Core must remain independent from the UI.

Plugins may extend behavior but should never compromise the integrity of the Core.

---

## Roadmap

### Phase 1 — Foundation

```text
[✓] Project structure
[✓] Executable command
[✓] Textual application
[✓] Home screen
[ ] Command registry
[ ] Event bus
[ ] Settings manager
```

### Phase 2 — Interaction

```text
[ ] Command Palette
[ ] Command execution
[ ] Command history
[ ] Recent files
```

### Phase 3 — Development

```text
[ ] Text editor
[ ] Multiple tabs
[ ] Syntax highlighting
[ ] Workspace indexing
```

### Phase 4 — Power Features

```text
[ ] Integrated terminal
[ ] Git integration
[ ] Themes
[ ] Plugin API
```

### Phase 5 — Ecosystem

```text
[ ] Plugin marketplace
[ ] AI integration
[ ] Advanced language support
```

---

## Why MyCoder?

```text
Most editors want you to adapt.

MyCoder wants to be adapted.
```

The goal is not to become another terminal version of an existing editor.

The goal is to create a development environment that feels transparent, hackable, and truly yours.

---

## Contributing

Contributions of all sizes are welcome.

Whether you are:

```text
• A Python developer
• A Textual enthusiast
• A terminal power user
• A designer
• A documentation writer
• A bug hunter
```

there is a place for you in the project.

---

## License

License to be defined.

---

```text
> initialize workspace...
> loading modules...
> establishing connection...
> welcome to mycoder

SYSTEM STATUS: ONLINE
```
