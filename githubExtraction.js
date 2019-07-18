/**
 * githubExtraction.js
 * Written by Jean Decian - Centre de Recherche Informatique de Montreal (CRIM)
 * Creation date : 2019/05/22
 * Last modified : 2019/06/26
 *  */

function saveCSV(fields, issues, repository, page, type) {
    let csvContent = "data:text/csv;charset=utf-8," + fields.join(";") + "\n";

    issues.forEach(issue => {
        csvContent += issue.join(";") + "\n";
    });
    
    var link = document.createElement("a");
    link.setAttribute("href", encodeURI(csvContent));
    link.setAttribute("download", repository + "_" + type + "_" + page + ".csv");
    
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function changePage(issues, page, params, url) {
    if (issues.length == 25) {
        if (page[0] == "page") {
            page[1] = String(Number(page[1]) + 1);
        } else {
            page[0] = "page=2&" + page[0];
        }
        params[0] = page.join("=");
        url[1] = params.join("&");
        window.location.href = url.join("?");
    }
}

var url = window.location.href.split("?");
var params = (url[1] != undefined) ? url[1].split("&") : ["page=1"];
var page = params[0].split("=");

var github = url[0].split("/");
var repo = github[4];
var type = github[5];

var issues = document.querySelectorAll('[id^="issue_"]:not([id$="link"])');
var filteredIssues = [];

issues.forEach(issue => {
    var section = issue.children[0].children[1];

    var issueId = section.children[0].id;
    var issueHref = section.children[0].href;
    var issueTitle = section.children[0].innerText.replace("#", "(hashtag)");
    var issueLabels = (section.children[section.children.length - 2] != undefined && section.children.length > 2) ? section.children[section.children.length - 2].innerText : "";
    var issueDate = (section.children[section.children.length - 1] != undefined) ? section.children[section.children.length - 1].children[0].children[1].getAttribute("datetime") : "";
    
    var row = [issueId, issueTitle, issueHref, issueDate, issueLabels];
    
    filteredIssues.push(row);
});

var fields = ["id", "title", "link", "date", "labels"]
var pageNumber = (page[0] == "page") ? page[1] : 1;

saveCSV(fields, filteredIssues, repo, pageNumber, type)
changePage(issues, page, params, url);