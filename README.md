# Idea Vault  
Не продукт. Не документация. Не инструкция.

Это хранилище идей: мысли, гипотезы, модели, сомнения, наблюдения.  
Код здесь вторичен. Правда живёт в словах.

Ничто в этом репозитории не является догмой.  
Всё временно, пересматриваемо и имеет право быть неверным.

Основные якоря (papers)  
ATLAS N (RU): papers/atlas-n/ATLAS_N_RU.md  
ATLAS N (EN): papers/atlas-n/ATLAS_N_EN.md  

Канон хранения идей  
Основное правило: одна тема — одна директория.  
Внутри темы может быть сколько угодно файлов (разные мысли об одном и том же).

Как устроена маршрутизация  
Каталог тем (куда класть новые материалы): topics/_CATALOG.md  

Структура внутри каждой темы:  
- index.md (обязательный): обзор темы, текущая позиция, ссылки на все заметки  
- notes/*.md (по желанию): отдельные заметки, одна мысль — один файл  
- drafts/*.md (по желанию): черновики, наброски  
- archive/*.md (по желанию): опровергнутые/устаревшие материалы (храним для истории)  

Каждая заметка начинается с:  
Status: набросок | гипотеза | проверено | опровергнуто | заброшено  
Confidence: низкая | средняя | высокая  

Темы  
ATLAS N: topics/atlas-n/index.md  

Заметка для чтения  
Считайте это лабораторным блокнотом, а не обещанием.  
Если что-то зацепило — форкайте, добавляйте свои мысли/логи/сомнения, присылайте PR.  
Один я это не вытяну.

# Idea Vault  
Not a product. Not documentation. Not a tutorial.

This is an idea vault: thoughts, hypotheses, models, doubts, observations.  
Code is secondary. Truth lives in the wording.

Nothing in this repository is dogma.  
Everything here is provisional, revisable, and allowed to be wrong.

### Papers (anchors)
- ATLAS N (RU): [papers/atlas-n/ATLAS_N_RU.md](papers/atlas-n/ATLAS_N_RU.md)  
- ATLAS N (EN): [papers/atlas-n/ATLAS_N_EN.md](papers/atlas-n/ATLAS_N_EN.md)

### Canon: how we store ideas
Core rule: one topic = one directory.  
Each topic may contain multiple files (different thoughts about the same thing).

### Routing map
Topic catalog (where to file new material): [topics/_CATALOG.md](topics/_CATALOG.md)

### Inside each topic directory
- `index.md` (mandatory): topic overview, current stance, links to all notes  
- `notes/*.md` (optional): individual notes, one thought per file  
- `drafts/*.md` (optional): rough fragments  
- `archive/*.md` (optional): falsified/superseded material (kept for history)

### Public reading note  
Treat this as a lab notebook, not a promise.

If anything resonates — fork it, add your own thoughts/logs/doubts, send PRs.  
One person can't pull this alone.
## Как помочь (запуск экспериментов у себя)

Важно перед началом
- Только легальные тесты на общедоступных конфигурациях и в сетях, где это не запрещено правилами (работа/учёба/организация).
- НЕ используйте результаты для доступа к запрещённому контенту.
- Соблюдайте законы вашей страны.
- НЕ публикуйте IP, домены, ключи, персональные данные - редактируйте/хешируйте.
- Не прикладывайте сами конфиги: только агрегированные результаты, метаданные и наблюдения.

1. Нажмите Fork (кнопка справа сверху) - получите копию репозитория у себя.
2. Скачайте к себе:
   git clone https://github.com/ВАШ_НИК/atlas-n.git
   cd atlas-n
3. Возьмите 10-100 конфигов из открытых источников (без приватных/утёкших баз).
4. Для каждого теста запишите:
   - Итог: SUCCESS / FAILURE / ERROR
   - Класс отказа (например: timeout / handshake-fail / auth-fail / route-fail / dns-fail / unknown)
   - Гипотеза причины (опционально, если есть основания)
   - Минимальный контекст: дата, город/страна, ОС/версия, протокол, клиент/версия, сеть (Wi-Fi/LTE)
5. Создайте файл в своём форке:
   topics/atlas-n/notes/ВАШ_НИК-2026-01-30.md

   Пример:
   Status: tested
   Confidence: medium
   Дата: 2026-01-30
   Тестов: 42
   Локация: Рига, LV
   ОС: Windows 11 24H2
   Протокол: WireGuard
   Клиент: WireGuard app v0.5.4
   Сеть: Wi-Fi, провайдер Tet
   SUCCESS: 28 (67%)
   FAILURE: 10 (24%) - классы: timeout (8), handshake-fail (2) (гипотеза: filtering)
   ERROR: 4 (9%)
   Заметки: наблюдение - при MTU 1400 доля timeout выше (гипотеза, требует перепроверки)
6. Отправьте результат:
   - Pull Request (PR) - лучший вариант.
   - Или issue: вставьте шаблон и приложите ваш .md.

Даже 10 тестов - уже ценность. Спасибо!

