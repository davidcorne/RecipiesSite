#!/usr/bin/env python
# Written by: DGC
# -*- coding: utf-8

# python imports
import os 
import markdown

# local imports

CSS="""\
body {
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    color: #444444;
    line-height: 1;
    max-width: 960px;
    padding: 30px;
    counter-reset: section;
}

h2 {
    counter-reset: sub-section;
}

h3 {
    counter-reset: detail;
}

h1 {
    font-size:400%;
    text-align: center;
}

h1, h2 {
    color: #3366FF
}

h2:before {
    content: counter(section) ". ";
    counter-increment: section;  /* Add 1 to section */
}

h3:before {
    content: counter(section) "." counter(sub-section) ". ";
    counter-increment: sub-section;  /* Add 1 to sub-section */
}

h4:before {
    content: counter(section) "." counter(sub-section) "." counter(detail) ". ";
    counter-increment: detail;  /* Add 1 to detail */
}

dl {
    margin-bottom:50px;
}

dl dt {
    background:#5f9be3;
    color:#fff;
    float:left; 
    font-weight:bold; 
    margin-right:10px; 
    padding:5px;  
    width:150px; 
}

ol ol {
    list-style-type: lower-alpha;
}

dl dd {
    margin:2px 0; 
    padding:5px 0;
}

blockquote {
    border-left:.5em solid #eee;
    padding: 0 2em;
    margin-left:0;
    max-width: 476px;
}
blockquote  cite {
    font-size:14px;
    line-height:20px;
    color:#bfbfbf;
}
blockquote cite:before {
    content: '\2014 \00A0';
}

blockquote p {  
    color: #666;
    max-width: 460px;
}

table, th, td {
    border: 1px solid black;
}

th {
    background:#5f9be3;
    color:#fff;
    font-weight:bold; 
    margin-right:10px; 
    padding:5px;  
    width:100px; 
    text-align:left
}

table {
    border-collapse:collapse;
}
"""

HEADER = """\
<html>
<head>
  <title>Recipes</title>
  <style type="text/css">
  {}
  </style>
</head>
<body>
""".format(CSS)

#==============================================================================
def make_recipe_list(path, level=2):
    if not os.path.exists(path):
        raise Exception("{} must exist".format(path))
    if os.path.isdir(path):
        return make_recipe_list_directory(path, level)
    else:
        return make_recipe_list_file(path)

#==============================================================================
def make_recipe_list_directory(path, level):
    representation = ["\n<h{0}>{1}</h{0}>\n".format(level, os.path.basename(path))]
    # handle files and directories seperately
    dir_list = [os.path.join(path, p) for p in os.listdir(path)]
    files = [f for f in dir_list if os.path.isfile(f)]
    directories = [d for d in dir_list if os.path.isdir(d)]
    if files:
        representation.append("<ul>")
    for f in files:
        representation.append(
            make_recipe_list_file(f)
            )
    if files:
        representation.append("</ul>")
    for directory in directories:
        representation.append(
            make_recipe_list_directory(directory, level + 1)
            )
    return "\n".join(representation)

#==============================================================================
def make_recipe_list_file(path):
    if path[-1] == "~":
        return ""
    label = os.path.splitext(os.path.basename(path))[0]
    return "<li><a target=\"_blank\" href=\"{0}\">{1}</a></li>".format(path, label)

#==============================================================================
class RecipeLister(object):
    
    def __init__(self, path):
        self.path = path

    def list(self):
        directories = ["Breakfast", "Snack", "Mains", "Dessert"]
        lst = [HEADER, "<h1>Recipes</h1>"]
        for directory in directories:
            lst.append(make_recipe_list(directory))
        return lst

    def __repr__(self):
        lst = self.list()
        return "\n".join([str(a) for a in lst])

#==============================================================================
def main():
    path = os.path.dirname(os.path.realpath(__file__))
    lister = RecipeLister(path)
    print(lister)

#==============================================================================
if (__name__ == "__main__"):
    main()
