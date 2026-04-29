## 🎯 Objective

Today's challenges are built entirely inside **VS Code** — you'll create files, edit YAML and SQL, and run commands in a terminal, all without leaving the editor. Before diving into dbt, this warm-up gives you a chance to get comfortable with the VS Code workflow you'll rely on throughout.

You covered the terminal basics already. Here you'll connect those skills to VS Code's interface and practice the exact file-editing loop used in every challenge ahead.

---

## 1. Quick Terminal Review

You already know these from before, let's make sure they're fresh. Open a terminal and try each one:

```bash
# Where am I?
pwd

# What's in this directory?
ls

# Show all files, including hidden ones (like .git, .gitignore)
ls -a

# Visualise the directory tree
tree

# Navigate into a folder
cd tests

# Go up one level
cd ..

# Go home
cd ~

# Go back to the previous folder
cd -

# You should now be back in the challenge folder, the next command should end with "data-analytics-warm-up"
pwd

# Open the current directory in VS Code
code .
```

<details>
<summary markdown="span">**💡 Reminder: what does `.` mean?**</summary>

`.` is shorthand for "the current directory". So `code .` means "open the current directory in VS Code". You'll use this constantly — it opens your whole project so you can see all files in VS Code's File Explorer.

</details>

---

## 2. VS Code Interface Tour

When you run `code .`, VS Code opens with a layout like this:

<!-- TODO: Add screenshot of VS Code open on the 00-WarmUp directory, showing all four areas clearly: Activity Bar (left icon strip), File Explorer panel (with README.md visible), the Editor pane (with README.md open), and the Integrated Terminal at the bottom with a prompt. Suggested filename: vscode-interface-overview.png -->

<img src="https://wagon-public-datasets.s3.amazonaws.com/data-analytics/03-Data-Transformation/09-Intro-to-DBT/vscode-interface-overview.png" alt="VS Code interface showing Activity Bar on the far left, File Explorer panel with project files, Editor pane open on a file, and Integrated Terminal at the bottom" width="80%">

The image above shows a typical VS Code window with four key areas highlighted:

1. **Activity Bar** (far left, vertical strip of icons) — click the icons here to switch between the File Explorer, Search, Git, and Extensions panels
2. **File Explorer** (left panel, opens when you click the top Activity Bar icon) — your project's folder and file tree; click any file to open it in the editor
3. **Editor** (centre/right) — where you read and write code; you can have multiple files open as tabs
4. **Integrated Terminal** (bottom panel) — a full terminal inside VS Code; run dbt commands here without leaving the editor

---

## 3. Opening VS Code on Your Challenge

**📍 In your terminal**, navigate to this warm-up directory and open it in VS Code:

```bash
# You should already be in this directory — confirm with:
pwd
# Expected end: /data-analytics-warm-up

# Open VS Code here
code .
```

VS Code will open and you'll see this README.md in the File Explorer.

<details>
<summary markdown="span">**💡 Why open the whole directory and not just a file?**</summary>

When you run `code .`, VS Code treats the current directory as your **workspace**. This means:

- The File Explorer shows all your project files in one place
- VS Code can resolve file references across the project (important for dbt extensions)
- The integrated terminal opens in the project root automatically

If you open a single file (`code README.md`) VS Code can't see the rest of the project — avoid this.

</details>

---

## 4. The Integrated Terminal

In the dbt challenges you'll constantly switch between editing files and running commands. The VS Code **integrated terminal** means you never have to leave the editor.

### Open the integrated terminal

**Three ways — pick the one you like:**

- **Keyboard shortcut** — Ctrl+\` (backtick) on Mac and Windows
- **Menu** — View → Terminal
- **Right-click** — right-click a folder in the Explorer → "Open in Integrated Terminal"

**📝 In VS Code**, open the integrated terminal now using any method above.

You'll see a terminal panel appear at the bottom of the screen. It opens in the same directory as your workspace — no `cd` needed.

Run this to confirm:

```bash
pwd
```

It should end with the name of your challenge directory (the exact name comes from the platform — something like `.../data-analytics-warm-up`).

<details>
<summary markdown="span">**💡 Can I use my external terminal instead?**</summary>

Yes — everything works the same in an external terminal. But the integrated terminal is faster for the dbt workflow because:

- You can see your file edits and your terminal output side by side
- It opens in the project root automatically every time
- You can run `dbt run` and immediately see output without switching windows

Get used to it now and it'll save you time every challenge.

</details>

---

## 5. Creating and Editing Files

In every dbt challenge you'll create SQL and YAML files. Here are the two ways to do it — both work, choose whichever feels natural.

### Option A: From the terminal (then open in VS Code)

```bash
# Open it in VS Code (you can also click on the file name in the explorer panel)
code my_notes.yml
```

### Option B: From VS Code's File Explorer

1. Right-click the folder in the File Explorer where you want the file
2. Select **"New File"**
3. Type the filename and press Enter
4. The file opens automatically in the editor

### Saving files

Whenever you edit a file in VS Code, **save it before running any commands**. Unsaved changes won't be picked up by dbt or tests.

- **macOS** — Cmd+S
- **Windows / Linux** — Ctrl+S

A dot (●) on the tab means unsaved changes. No dot means the file is saved.

---

## 6. YAML Basics

Most dbt configuration files use **YAML** — a format for structured data that uses indentation instead of brackets.

#### 🧩 Recommended extension: Indent Rainbow

Before reading on, install the **Indent Rainbow** extension. It colours each indentation level a different shade, making it much easier to spot misaligned YAML at a glance.

**📝 In VS Code**, open the Extensions panel (click the blocks icon in the Activity Bar, or press Cmd+Shift+X / Ctrl+Shift+X), search for **`Indent Rainbow`** (publisher: oderwat), and click **Install**.

You'll work with YAML constantly in this unit. Here are the rules that matter:

### Indentation is everything

YAML uses 2 spaces for each level of nesting. The format doesn't support tabs, but in VS Code you can use your tab key on the keyboard: VS Code will convert the tabs into two spaces.

<details>
<summary markdown="span">Where is my tab key?</summary>

tab key? All the way to the left of your keyboard, usually the third key from the top, it says TAB, or has a little arrow on it. You can use it to indent your code. Or combine SHIFT + TAB to remove an indentation level.

</details>

```yaml
# Correct — consistent 2-space indentation
version: 2

sources:
  - name: jaffle_shop
    schema: raw
    tables:
      - name: raw_customers
        description: "Customer data"

# ❌ Wrong — mixing tabs and spaces, or inconsistent indentation
sources:
    - name: jaffle_shop   # 4 spaces instead of 2
      schema: raw
       tables:            # 7 spaces — breaks parsing
```

### Key: value pairs

```yaml
name: jaffle_shop_dbt   # String value (quotes optional unless special characters)
version: '1.0.0'        # String with quotes
threads: 4              # Integer value
```

### Lists use `-`

```yaml
tables:
  - name: raw_customers
  - name: raw_orders
  - name: raw_payments
```

### Nested structure

Each level of nesting is 2 more spaces:

```yaml
sources:             # Level 1
  - name: jaffle_shop    # Level 2 (2 spaces)
    tables:              # Level 2
      - name: orders     # Level 3 (4 spaces)
        description: "Orders table"  # Level 3
```

<details>
<summary markdown="span">**💡 Why does bad indentation break things?**</summary>

YAML parsers are strict about indentation because it defines the structure of the data. A single misplaced space can cause a parse error that stops dbt from reading the file entirely.

When dbt says something like `Error reading file: mapping values are not allowed here`, it's almost always an indentation problem. Count your spaces carefully!

</details>

---

## 7. Useful Keyboard Shortcuts

These shortcuts will save you time every day in this unit:

- **Save file** — Cmd+S (macOS) / Ctrl+S (Windows/Linux)
- **Toggle terminal** — Ctrl+\`
- **Open file by name** — Cmd+P (macOS) / Ctrl+P (Windows/Linux)
- **Command Palette** — Cmd+Shift+P (macOS) / Ctrl+Shift+P (Windows/Linux)
- **Find in file** — Cmd+F (macOS) / Ctrl+F (Windows/Linux)
- **Find across project** — Cmd+Shift+F (macOS) / Ctrl+Shift+F (Windows/Linux)
- **Comment/uncomment line** — Cmd+/ (macOS) / Ctrl+/ (Windows/Linux)
- **Split editor** — Cmd+\\ (macOS) / Ctrl+\\ (Windows/Linux)

**Cmd+P / Ctrl+P** (Quick Open) is especially useful — type a filename and jump straight to it without clicking through the File Explorer.

---

## 8. Hands-On Practice

Let's put it all together with a short exercise that mirrors exactly what you'll do in Challenge 1.

### Step 1: Create a YAML file

**📝 In VS Code**, use the File Explorer (or terminal) to create a new file called `practice.yml` in this directory.

### Step 2: Add some YAML content

**📝 In VS Code**, open `practice.yml` and type (or paste) the following:

```yaml
# My first YAML file

project:
  name: warm_up_practice
  version: '1.0.0'

tools:
  - name: dbt
    purpose: "SQL transformation framework"
  - name: duckdb
    purpose: "Local analytical database"
  - name: vscode
    purpose: "Code editor with integrated terminal"
```

**💾 Save the file** (Cmd+S or Ctrl+S). Check the tab — the dot should disappear.

### Step 3: Verify from the terminal

**📍 In the integrated terminal**, confirm the file exists and check its contents:

```bash
# List files — practice.yml should appear
ls

# Print file contents to terminal
cat practice.yml
```

You should see your YAML printed in the terminal. This is the same `cat` command you'll use to verify files throughout the dbt challenges.

### Step 4: Edit and re-save

**📝 In VS Code**, add your name to the `project` section:

```yaml
project:
  name: warm_up_practice
  version: '1.0.0'
  author: "Your Name"   # ← add this line
```

**💾 Save** and run `cat practice.yml` in the terminal again to see your change reflected.

---

## 9. The Dbt Workflow Preview

In every challenge for this unit, your workflow will look like this:

```markdown
1. Open VS Code (code .)
2. Create or edit a file in VS Code
3. Save the file (Cmd+S / Ctrl+S)
4. Run a dbt command in the integrated terminal (dbt run, dbt test, dbt debug)
5. Read the output
6. Go back to step 2 if needed
```

The challenge instructions will tell you:

- **📝 In VS Code** → editing files
- **📍 In your terminal** → running commands

Get comfortable switching between the two — it's the core loop of the whole unit.

---

## 🧪 Checkpoint: Run the Tests

Before moving on, validate your `practice.yml` with the test suite.

**📍 In your terminal**, make sure you are in the challenge directory:

```bash
pwd
# Expected end: .../09-Data-Layers-And-Intro-DBT/data-analytics-warm-up
```

Then run the tests:

```bash
pytest tests/test_warmup.py -v
```

**If all tests pass**, commit and push your work:

```bash
git add practice.yml
git commit -m "Complete VS Code warm-up: practice.yml"
git push origin master
```

**❌ Any failures?** Read the error message — each one tells you exactly what to fix with a "Did you...?" hint. If you're still stuck, raise a ticket with a TA!

---

## Challenge Complete

You created, edited, and validated a structured data file — the same loop you'll repeat in every challenge ahead.

### Key takeaways

- **VS Code as your workspace** — `code .` opens file explorer, editor, and terminal in one place
- **The edit → save → run loop** — edit a file, save it, run a command, read the output
- **YAML structure** — indentation defines hierarchy; one misplaced space breaks the whole file
- **`cat` for quick verification** — the fastest way to confirm your edit was saved

---

<details>
<summary markdown="span">**� Quick Reference Card**</summary>

**Terminal commands from the Intro to Git day:**

```bash
pwd              # Where am I?
ls               # What's in this directory?
ls -a            # Show hidden files too
tree             # Show directory tree
cd folder-name   # Go into a folder
cd ..            # Go up one level
mkdir new-folder # Create a folder
touch file.yml   # Create a file
cat file.yml     # Print file contents
rm file.yml      # Delete a file (permanent!)
code .           # Open current directory in VS Code
code file.yml    # Open a specific file in VS Code
```

**VS Code shortcuts:**

- **Save file** — Cmd+S (macOS) / Ctrl+S (Windows/Linux)
- **Toggle terminal** — Ctrl+\`
- **Open file by name** — Cmd+P (macOS) / Ctrl+P (Windows/Linux)
- **Find in file** — Cmd+F (macOS) / Ctrl+F (Windows/Linux)
- **Comment line** — Cmd+/ (macOS) / Ctrl+/ (Windows/Linux)

**YAML rules:**

- 2 spaces per indent level (never tabs)
- Lists use `-` with a space after
- `key: value` with a space after the colon
- Quotes are optional for plain strings but required for values with special characters (`: # {}`)

</details>
