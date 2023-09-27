# Security Extractor Extractor Java

`random-system` : name of a random system used for the README

## How to run the Security Extractor

1. Clone the project using `git clone` over SSH or HTTPS
2. Select a target GitHub repository that have an `Issues` tab
3. Go to the `Issues` tab of selected GitHub repository
   1. Filter issues by requirements
      1. `.java` : if issues must mention Java files
      2. `security` : if issues must mention security
4. Run the script [`scripts > githubExtraction.js`](scripts/githubExtraction.js), to extract all issues of a GitHub repository, in a browser
   1. Add the script as a snippet : `Right click > Inspect > Sources > Snippets > Paste script`
   2. Run the script to generate a CSV file
   3. The page will be redirected to the next page of issues (if exists)
      1. Repeat 4.2
5. Put all extracted issues files into the `input` folder of the project
6. In `main.py`
   1. Specify the name of the system (name of the repository in the URL) and the number of files generated
      1. Add an entry in the `FILES` array as `["random-system", 6]`
   2. Run the code

## HOW DOES IT WORK

### Script on GitHub

The Javascript generate a CSV file that contains different fields about all the issues of the current page (25 issues if there is more than one page):
- `id` : id of the issue
- `title` : title of the issue
- `link` : GitHub link of the issue
- `date` : date of the issue (opened or closed)
- `labels` : labels associated to the issue

After generating the output file `random-system_issues_x` (where `x` if the page number of the `issues` tab), you will be redirected to the next page (if it exists).

### Python app

First, you must configure the app by specifying the system's name and number of files generated by the previous script in the `FILES` array. As an example, we will use the name `random-system` and 6 generated files.
```python
FILES = [
    ["random-system", 6]
]
```

The first part of the Python app is about the merge of every file generated into one. It will also add a field `html` that contains the HTML code retrieve using the `link` of the issue. It saves the output as `merge_random-system_issues.csv`.

The second part of the Python app is the filtering process of the issues present in the file previously generated. Using the `html` code of every issue :
- a `security` field is created where it contains a boolean value :
  - `1` when the HTML contains keywords such as `bug` and keywords specified in the `filters` variable in `main.py` such as `security`, `threat` and `vulnerabilities`
  - `0` when it is not related to a `security bug`
  ```python
  security = "1" if search.contains(html, filters) and search.contains(html, "bug") else 0
  ```
- a list of files `files` is generated using the function `handleExtraction` where the extension is specified in the third argument as
  ```python
  # sometimes, the line is specify after the name of the file using ":"
  files = search.handleExtraction(html, "()", ".java:")
  ```

A file `out_random-system-issues.csv` is then created with the following fiels :
- `file` : name of the file
- `line` : line of file where a bug seems to appear
- `link` : GitHub link of the issue
- `date` : date of the issue (opened or closed)
- `security` : boolean on if a file participated in a bug

## Some terminal commands for repository statistics

- Number of JAVA files
  ```bash
  git ls-files | grep ".*\.java$" | wc -l
  ```
- Total lines of code in JAVA files
  ```bash
  git ls-files | grep ".*\.java$" | xargs wc -l
  ```