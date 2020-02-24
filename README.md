# CRIM Security Extractor

## HOW TO

- Run the script `scripts > githubExtraction.js` to extract all issues on GitHub
  - Right click > Inspect > Sources > Snippets > Paste script
  - Run script
- Put extracted issues into `input` folder
- In `main.py`
  - Specify the name of the system (name of the repository)
  - Specify the number of files
  - Run

## Git Repository Statistics

Number of JAVA files

```
git ls-files | grep ".*\.java$" | wc -l
```

Lines of code in JAVA files

```
git ls-files | grep ".*\.java$" | xargs wc -l
```