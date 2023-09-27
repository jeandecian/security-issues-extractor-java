import constant as c
import github as g
import sqlConnect as sql

# FILES

# ["name of systems", number of files]
FILES = [["elasticsearch", 2], ["guava", 2]]

filters = [" security ", " threat ", " vulnerability "]

g.increase_size_limit()

category = "issues"

filterTableColumns = [
    "id INT AUTO_INCREMENT PRIMARY KEY",
    "file MEDIUMTEXT",
    "line MEDIUMTEXT",
    "link MEDIUMTEXT",
    "date MEDIUMTEXT",
    "security INT",
]
merge_table_columns = [
    "id INT AUTO_INCREMENT PRIMARY KEY",
    "issueKey VARCHAR(255)",
    "title MEDIUMTEXT",
    "link MEDIUMTEXT",
    "date MEDIUMTEXT",
    "labels MEDIUMTEXT",
    "html MEDIUMTEXT",
]
columns = ["file", "line", "link", "date", "security"]

for file in FILES:
    print("\n[FILES] \tProcessing " + file[0])

    g.merge([c.INPUT_FILES], [c.OUTPUT_FILES], file[0], category, file[1])
    out_file, write_buffer = g.filter_sort(
        "merge_" + file[0] + "_" + category, columns, filters, merge_table_columns
    )
    # sql.save(out_file, filterTableColumns, columns, write_buffer)
