import xml.etree.ElementTree
from xml.etree.ElementTree import ElementTree

from lxml import etree


import xml.dom.minidom



import sys
import os


coding = 'utf-8'
#filename = "ITR_SHARED_COMMON.xml"
file_list = list()
directory_list = list()

filename1 = 'ITR_PROJECT_LIFECYCLE.XML'
filename2 = 'ITR_SHARED_LIFECYCLE.XML'
filename3 = 'ITR_SHARED_COMMON.XML'

directory1 = './DEV_XML_20170523'
directory2 = './PPM'
directory3 = './XML_BACKUP_20161122'
directory4 = './PRO_XML_20170523'

workflow_prefix_1 = '$PMWorkflowLogDir'
session_prefix_1 = '$PMSessionLogDir'
directory_prefix_2 = 'itr'
log_postfix = '.log'

#filename = "test.xml"
category_1 = 'FOLDER'
#category_2 = 'SESSIONEXTENSION'
#category_3 = 'ATTRIBUTE'
#category_2 = 'SESSION'
category_workflow = 'WORKFLOW'
category_shortcut = 'SHORTCUT'
category_3 = 'SESSION'
category_4 = 'ATTRIBUTE'

#output_file = 'extraction.txt'
output_file = 'workflow_log.txt'
output_file_folder = 'folder.txt'
write_mode = 'w'

name_attrib = 'NAME'
owner_attrib = 'OWNER'
value_attrib = 'VALUE'
foldername_attrib = 'FOLDERNAME'

connector = '\t'
slash_connector = '\\'
endofline = '\n'

lookup_str = '_BAK20170427'
lookup_str = '_BAK20170522'
#error_attribute_name_1 = 'Reject file directory'
#error_attribute_name_2 = 'Reject filename'
attribute_name_4 = 'Workflow Log File Directory'
attribute_name_5 = 'Workflow Log File Name'
attribute_name_6 = 'Session Log File directory'
attribute_name_7 = 'Session Log File Name'

#directory_list.append(directory1)
#directory_list.append(directory2)
#directory_list.append(directory3)
directory_list.append(directory4)

def IsSubString(SubStrList,Str):
    flag = True
    for substr in SubStrList:
        if not(substr in Str):
            flag=False
    return flag

FlagStr = ['.XML']

for directory in directory_list:
    FileNames = os.listdir(directory)
    if (len(FileNames)>0):
       for fn in FileNames:
           if (len(FlagStr)>0):
               if (IsSubString(FlagStr,fn)):
                   full_filename=os.path.join(directory,fn)
                   file_list.append(full_filename)
           else:
               full_filename=os.path.join(directory,fn)
               file_list.append(full_filename)

doctype = '<!DOCTYPE POWERMART SYSTEM "powrmart.dtd">\n'


for file in file_list:

    directory_name = os.path.dirname(file).lstrip('./')
    file_name = os.path.basename(file)
    try:
        tree = ElementTree(file=file)

        f = open(file,'w')
        f.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
        f.write(doctype)
        tree.write(f, 'utf-8')
        f.close()

        """
        xml = xml.dom.minidom.parse(file)
        pretty_xml_as_string = xml.toprettyxml()
        f = open(file,'w')
        f.write(pretty_xml_as_string)
        f.close()
        """
        print file_name
    except:
        print "1"

#write_xml(tree, "./out.xml")
"""

"""
#tree.write('output.xml') 