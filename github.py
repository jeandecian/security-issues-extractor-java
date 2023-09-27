# github.py
# Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
# Creation date : 2019/05/27
# Last modified : 2020/02/24

import csv
import time

import constant as c
import csvManager
import display as disp
import requests as req
import search
import sqlConnect as sql


def increase_size_limit():
    csvManager.increase_size_limit()


def merge(path_in, path_out, file, category, count):
    # merge all github files from same repo into one + add the html code
    process_file = file + "_" + category
    fields = []
    unique = []
    write_buffer = []
    total_time = 0

    for i in range(count):
        start_time = time.time()
        disp.processingFile(process_file, i + 1, count)
        path = path_in.copy()
        path.append(process_file + "_" + str(i + 1) + ".csv")
        fields, contents = csvManager.read(csvManager.get_path(path))

        for row in contents:
            disp.loading(".")
            if (row[fields.index("id")] not in unique) and (len(row) == len(fields)):
                unique.append(row[fields.index("id")])
                row.append(req.getWebsiteHtml(row[fields.index("link")]))
                write_buffer.append(row)

        diff_time = round(time.time() - start_time, 2)
        print(" " + str(diff_time))
        total_time += diff_time

    print(
        "\n[GIT] \tProcessing "
        + process_file
        + " took in total "
        + str(round(total_time, 2))
        + "s ("
        + str(len(write_buffer))
        + ")"
    )
    path_out.append("merge_" + process_file)
    fields.append("html")
    csvManager.save(csvManager.get_path(path_out), fields, write_buffer)


def filter_sort(file, columns, filters, merge_table_columns):
    # filter the merge github file and sort
    fields, contents = csvManager.read(csvManager.get_path([c.OUTPUT_FILES, file]))
    fields[fields.index("id")] = "issueKey"
    write_buffer = []
    out_file = file.replace(".", "")
    out_file = out_file.replace("-", "")
    # sql.save(out_file, merge_table_columns, fields, contents)

    for row in contents:
        html = row[fields.index("html")]

        # check if html contains some key word related to security
        security = (
            "1"
            if search.contains(html, filters) and search.contains(html, "bug")
            else 0
        )

        # retrive every files that match .java file
        # add ":" after because sometimes, it has the line after
        files = search.handleExtraction(html, "()", ".java:")

        if files:
            date = search.extractElement("<relative-time", html, "/relative-time")
            date = search.extractElement('"', date, "T")

            for f in files:
                row_buffer = []
                fl = f.split(":")
                row_buffer.append(fl[0])
                row_buffer.append(fl[-1])
                row_buffer.append(row[fields.index("link")])
                row_buffer.append(date)
                row_buffer.append(security)

                write_buffer.append(row_buffer)

    out_file = out_file.replace("merge_", "out_")
    path_out = [c.OUTPUT_FILES, out_file]
    csvManager.save(csvManager.get_path(path_out), columns, write_buffer)

    return out_file, write_buffer
