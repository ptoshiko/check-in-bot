# Check-in Bot
Hackathon by "School21" of Sberbank
**Task:** Develop a Telegram bot for check-in at school events

## Table of Contents

1. [Task Description](#task-description)
2. [Project Architecture](#project-architecture)
3. [Results](#results)
____

## Task Description
You can view the full task description [here.](https://github.com/ptoshiko/Checkin_Bot/blob/main/Checkin_bot_task.pdf) 

**Team:**
[urycherd](https://github.com/urycherd) [mikabuto](https://github.com/mikabuto) [hardworkerM](https://github.com/hardworkerM)

____
## Project Architecture
- [/data](https://github.com/ptoshiko/check-in-bot/tree/main/data) - storage for generated report files and QR codes
- [/database](https://github.com/ptoshiko/check-in-bot/tree/main/database) - database connection and SQL query functions
- [/deeplink](https://github.com/ptoshiko/check-in-bot/tree/main/deeplink) - event QR code generation
- [/handlers](https://github.com/ptoshiko/check-in-bot/tree/main/handlers) - handlers for bot-user interactions
- [/keyboards](https://github.com/ptoshiko/check-in-bot/tree/main/keyboards) - functions for creating Inline and Reply keyboards
- [/state](https://github.com/ptoshiko/check-in-bot/tree/main/state) - state class
- [/utils](https://github.com/ptoshiko/check-in-bot/tree/main/utils) - auxiliary formatting functions
- app.py и create_bot.py - bot connection and activation

____
## Results
Bot functionality presentation [YouTube](https://youtu.be/U5yTr65kLro)

____
