__author__ = 'Bernardo'

"""
CREATE TABLE table_name
(
column_name1 data_type(size),
column_name2 data_type(size),
column_name3 data_type(size),
....
);
"""



import re
class evaluator:
    def execute(self, query):
        if ("create table") in query:
            createTbl = r"(?:\s*)create table(?:\s*)(.*?)(?:\s*)\((?:\s*)(.*?)\);"
            groups =  re.findall(createTbl, query, re.S)
            print ("----->" + str(groups))
            attribsre = r"((?:.*?) (?:.*?),(?:\s*))"
            attribs = re.findall(attribsre, groups[0][1], re.S)
            print ("----->" + str(attribs))

        #select = r"select (.*?) from (.*?);"
        #groups =  re.findall(select, query, re.S)
