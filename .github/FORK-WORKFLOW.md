# Fork Workflow Best Practices

## ⚠️ КРИТИЧНО: Це форк, не оригінальний репозиторій

**Upstream:** `bmad-code-org/BMAD-METHOD` (оригінал)
**Origin:** `felectra/BMAD-METHOD` (твій форк)

---

## 🎯 Головний принцип

**`origin/main` = чисте дзеркало `upstream/main`**

```
upstream/main  (оригінал)
    ↓ fetch + merge
origin/main    (твій форк) ← ЧИСТИЙ, БЕЗ кастомних файлів
    ↓ branch
origin/feature/*  ← ТУТ твої зміни
```

---

## ❌ ЩО НІКОЛИ НЕ РОБИТИ

### 1. Не додавати файли в `origin/main`

**Погано:**

```bash
git checkout main
# додаю .opencode/, Makefile, etc
git commit -m "add my configs"
git push origin main
```

**Чому погано:**

- 🔥 Merge conflicts при sync з upstream
- 🔥 Неможливо зробити чистий PR в upstream
- 🔥 Складно підтримувати синхронізацію

**Правильно:**

```bash
# Кастомні файли → feature гілка або глобальна config
git checkout -b local/configs
# АБО
mv .opencode ~/.config/opencode/
```

---

### 2. Не модифікувати існуючі файли в main

**Погано:**

```bash
git checkout main
vim package.json  # змінити залежності
git commit -m "update deps"
```

**Чому погано:**

- Конфлікт з upstream при кожному sync
- Ламає можливість fast-forward merge

**Правильно:**

```bash
git checkout -b feature/update-deps
vim package.json
git commit -m "feat: update deps"
# потім PR в upstream якщо треба
```

---

### 3. Не використовувати main для розробки

**Погано:**

```bash
git checkout main
# працювати тут
git add .
git commit -m "my work"
```

**Чому погано:**

- main має бути синхронізований з upstream
- Твоя робота заважає sync

**Правильно:**

```bash
git checkout -b feature/my-work
# працювати тут
```

---

## ✅ ПРАВИЛЬНИЙ WORKFLOW

### 1. Синхронізація з upstream (щодня)

**Автоматично (рекомендується):**

```bash
# Використай персональний скрипт
git-sync-fork check   # перевірити
git-sync-fork sync    # синхронізувати
```

**Вручну:**

```bash
git checkout main
git fetch upstream
git merge upstream/main --ff-only  # тільки fast-forward!
git push origin main
```

**Якщо fast-forward не працює:**

```bash
# Щось не так! main має бути чистим
git log origin/main ^upstream/main  # що додано в main?
# Треба виправити - створити feature гілку з цих змін
```

---

### 2. Робота над features

```bash
# 1. Переконатися що main свіжий
git checkout main
git-sync-fork sync

# 2. Створити feature гілку
git checkout -b feature/my-feature

# 3. Працювати
# ... зміни ...
git add .
git commit -m "feat: my feature"

# 4. Push до origin
git push origin feature/my-feature

# 5. Створити PR:
#    - Якщо контрибут → upstream
#    - Якщо особисте → тримати в origin
```

---

### 3. Довгоживучі feature гілки

```bash
# Регулярно rebase на свіжий main
git checkout main
git-sync-fork sync

git checkout feature/long-running
git rebase main

# Якщо конфлікти - вирішити та:
git rebase --continue
git push origin feature/long-running --force-with-lease
```

---

## 🛠️ Налаштування automation

### OpenCode Commands

**Розташування:** `~/.config/opencode/command/` (ГЛОБАЛЬНО)

```bash
# Перемістити command з проєкту
mv .opencode/command/sync-upstream.md ~/.config/opencode/command/

# Видалити локальну .opencode/
rm -rf .opencode/
```

**Використання в будь-якому проєкті:**

```
/sync-upstream
```

---

### Git Sync Script

**Розташування:** `~/bin/git-sync-fork` (ГЛОБАЛЬНО)

```bash
# Зробити executable (вручну)
chmod +x ~/bin/git-sync-fork

# Додати ~/bin до PATH (якщо ще немає)
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Використання:**

```bash
cd /path/to/BMAD-METHOD
git-sync-fork check   # перевірка
git-sync-fork sync    # синхронізація
```

**Працює для ВСІХ форків автоматично!**

---

### Алісаси (опціонально)

```bash
# Додати в ~/.gitconfig
[alias]
    sync-check = !git-sync-fork check
    sync = !git-sync-fork sync

# Використання
git sync-check
git sync
```

---

## 📁 Структура файлів

### ❌ Погано (в проєкті):

```
$PROJECT_ROOT/
├── .opencode/          # ❌ буде конфліктувати
│   └── command/
├── Makefile            # ❌ може конфліктувати
└── my-scripts/         # ❌ засмічує форк
```

### ✅ Добре (глобально):

```
~/.config/opencode/     # ✅ працює скрізь
├── command/
│   └── sync-upstream.md
└── opencode.json

~/bin/                  # ✅ персональні скрипти
└── git-sync-fork

$PROJECT_ROOT/          # ✅ чистий форк
├── .git/
└── (тільки upstream код)
```

### ⚠️ Виняток (якщо ДУЖЕ треба):

```
$PROJECT_ROOT/
├── .gitignore          # додати:
│   # Local customizations
│   .local/
│
└── .local/             # локальні файли, НЕ в git
    ├── scripts/
    └── notes.md
```

---

## 🔍 Перевірка стану

### Чи чистий мій main?

```bash
# Чи є коміти в main які не в upstream?
git log origin/main ^upstream/main

# Має бути порожньо!
# Якщо щось є → проблема
```

### Чи можу робити PR в upstream?

```bash
# Перевірити чи main синхронізований
git checkout main
git fetch upstream
git diff upstream/main

# Має бути БЕЗ різниці!
```

---

## 🚨 Troubleshooting

### "Fast-forward merge не працює"

```bash
# main засмічений - треба почистити
git checkout main
git reset --hard upstream/main
git push origin main --force

# ⚠️ УВАГА: Це видалить ВСІ зміни в main!
# Спочатку зберегти їх в feature гілку:
git checkout -b backup/main-changes
git checkout main
git reset --hard upstream/main
```

### "Конфлікти при sync"

```bash
# Не має бути конфліктів якщо main чистий!
# Якщо є → main засмічений

# Вирішення:
git merge --abort
git reset --hard upstream/main
git push origin main --force
```

---

## 📚 Додаткові ресурси

- **Global script:** `~/bin/git-sync-fork`
- **OpenCode command:** `~/.config/opencode/command/sync-upstream.md`
- **Git docs:** https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches

---

## 💡 Золоте правило

> **`origin/main` - тільки read-only mirror від `upstream/main`**
>
> Всі зміни → feature гілки  
> Всі кастомізації → глобальна config  
> Ніколи не додавати файли в main

**Принцип:** Форк має бути невидимим - тільки зручний remote для sync.
