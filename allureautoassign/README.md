# Установка

```bash
git clone git@gitlab.corp.mail.ru:imqa/allureautoassign.git
cd allureautoassign
virtualenv venv  # Установка virtualenv - https://sourabhbajaj.com/mac-setup/Python/virtualenv.html
source venv/bin/activate
pip install -r requirements.txt
```


# Help

```bash
✗ python cli.py --help
                                                                                                                                                                                
 Usage: cli.py [OPTIONS] TOKEN LAUNCH_IDS...                                                                                                                                    
                                                                                                                                                                                
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    token           TEXT           [default: None] [required]                                                                                                               │
│ *    launch_ids      LAUNCH_IDS...  [default: None] [required]                                                                                                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                      │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                               │
│ --help                        Show this message and exit.                                                                                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

# Пример запуска

```bash
python cli.py 'ALLURE_TOKEN' ALLURE_LAUNCH_ID1 ALLURE_LAUNCH_ID2 ALLURE_LAUNCH_ID3
```