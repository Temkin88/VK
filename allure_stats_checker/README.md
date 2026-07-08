# Установка

```bash
git clone git@gitlab.corp.mail.ru:imqa/allure_stats_checker.git
cd allure_stats_checker
pip install -r requirements.txt
```

# Использование

```bash
(venv) test@192 allure_stats_checker % python checker.py --help 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
 Usage: checker.py [OPTIONS] ALLURE_LAUNCH_ID ALLURE_TOKEN                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
╭─ Arguments ────────────────────────────────────────────────────────╮
│ *    allure_launch_id      INTEGER  [default: None] [required]     │
│ *    allure_token          TEXT     [default: None] [required]     │
╰────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────╮
│ --report-path        TEXT  [default: allure-report.json]           │
│ --help                     Show this message and exit.             │
╰────────────────────────────────────────────────────────────────────╯


./checker.py 153494 'ALLURE_TOKEN'
INFO:__main__:Launch "#167 TARM (Pre-Production)" is finished, fetching results
INFO:__main__:Looks like there are unresolved results in report, check full report in Allure TestOps https://allure.vk.team/launch/153494
INFO:__main__:Report saved to allure-report.json, check it!
```

# Код завершения скрипта

Фейлим прогон если код завершения скрипта не равен 0

# Текст отчета

Статистика и предварительный текст отчета будет сохранен в формате json

```json
{
  "failed": {
    "content": [],
    "count": 0
  },
  "broken": {
    "content": [
      {
        "id": 36160915,
        "testCaseId": 30200,
        "name": "Ошибка добавления пользователя в группу из-за настроек приватности",
        "status": "broken"
      },
      {
        "id": 36157848,
        "testCaseId": 30197,
        "name": "Запрос элементов галереи чата",
        "status": "broken"
      }
    ],
    "count": 2
  },
  "total_count": 2,
  "report": "Тесты со статусом \"broken\":\nОшибка добавления пользователя в группу из-за настроек приватности\nЗапрос элементов галереи чата\n\n"
}
```