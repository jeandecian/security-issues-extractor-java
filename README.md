# CRIM Security Extractor

## Git Repository Statistics

Number of JAVA files

```
git ls-files | grep ".*\.java$" | wc -l
```

Lines of code in JAVA files

```
git ls-files | grep ".*\.java$" | xargs wc -l
```

## GitHub Extraction

- Run the script `script > githubExtraction.js` until all pages have been exported
- Put all csv files inside `github_export` folder