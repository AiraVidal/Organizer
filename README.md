# Organizer

Aplicativo em Python com interface grafica (Tkinter) para organizar arquivos de uma pasta por extensao.

## Como funciona

- Seleciona uma pasta de origem.
- Cria a pasta `Organizados` dentro dela.
- Move os arquivos para subpastas por extensao (ex.: `pdf`, `jpg`, `txt`).
- Arquivos sem extensao vao para `sem_extensao`.
- Evita sobrescrever arquivos com nomes iguais (adiciona sufixo `_1`, `_2`, etc.).
- Mostra no log os arquivos movidos e ignorados.

## Requisitos

- Python 3.10+ (recomendado)
- Tkinter (normalmente ja vem com Python no Windows)

## Executar

No terminal, dentro da pasta do projeto:

```bash
python organizador.py
```

## Observacoes

- O script ignora o proprio `organizador.py` para nao mover o arquivo em uso.
- Pastas nao sao movidas, apenas arquivos.
