import xml.etree.ElementTree

from xml.etree.ElementTree import ElementTree
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

f = open(output_file, write_mode)
folder_txt = open(output_file_folder, write_mode)

#file_list = ['./PRO_XML_20170523/ITR_PROJECT_LIFECYCLE.XML']

for file in file_list:

    directory_name = os.path.dirname(file).lstrip('./')
    file_name = os.path.basename(file)
    try:
        tree = ElementTree()
        tree.parse(file)
        folders = tree.iter(category_1)
        #sessions = tree.iter(category_3)

    except: 
        print "Error:cannot parse file:" + file

    for folder in folders:
        #print element
        folder_name = folder.get(name_attrib)
        #print name
        owner = folder.get(owner_attrib)
        #print owner
        if lookup_str in folder_name:

            folder_name = folder_name.rstrip(lookup_str)
            folder.set(name_attrib, folder_name)

        folder_name = folder.get(name_attrib)
        line = \
        directory_name + connector + \
        file_name + connector + \
        folder_name + connector + \
        owner + \
        endofline
        folder_txt.writelines(line)

        workflows = folder.iter(category_workflow)
        shortcuts = folder.iter(category_shortcut)

        for shortcut in shortcuts:

            shortcut_name = shortcut.get(name_attrib)
            shortcut_foldername = shortcut.get(foldername_attrib)

            if lookup_str in shortcut_foldername:

                shortcut_foldername = shortcut_foldername.rstrip(lookup_str)
                shortcut.set(foldername_attrib, shortcut_foldername)

            shortcut_foldername = shortcut.get(foldername_attrib)
            line = \
            file_name + connector + \
            folder_name + connector + \
            shortcut_name + connector + \
            shortcut_foldername + connector + \
            endofline
            folder_txt.writelines(line)

        for workflow in workflows:
            
            workflow_name = workflow.get(name_attrib)

            attributes = workflow.iter(category_4)
            # attributes that has worlflow directory
            for attribute in attributes:
                name = attribute.get(name_attrib)
                if name == attribute_name_4:

                    workflow_log_file_directory_value = \
                    workflow_prefix_1 + slash_connector + \
                    directory_prefix_2 + slash_connector + \
                    folder_name + slash_connector + \
                    workflow_name + slash_connector

                    attribute.set(value_attrib, workflow_log_file_directory_value)
                    
                    value = attribute.get(value_attrib)
                    workflow_log_file_directory = value

                if name == attribute_name_5:

                    workflow_log_file_name_value = \
                    workflow_name + log_postfix
                    attribute.set(value_attrib, workflow_log_file_name_value)

                    value = attribute.get(value_attrib)
                    workflow_log_file_name = value

            sessions = workflow.iter(category_3)
            for session in sessions:

                session_name = session.get(name_attrib)
                print session_name
                attributes = session.iter(category_4)
                # attributes that has worlflow directory
                for attribute in attributes:
                    name = attribute.get(name_attrib)
                    
                    if name == attribute_name_6:
                        
                        session_log_file_directory_value = \
                        session_prefix_1 + slash_connector + \
                        directory_prefix_2 + slash_connector + \
                        folder_name + slash_connector + \
                        workflow_name + slash_connector

                        attribute.set(value_attrib, session_log_file_directory_value)
                        
                        value = attribute.get(value_attrib)
                        session_log_file_directory = value

                    if name == attribute_name_7:
                        
                        session_log_file_name_value = \
                        session_name + log_postfix
                        print session_log_file_name_value
                        attribute.set(value_attrib, session_log_file_name_value)

                        value = attribute.get(value_attrib)
                        session_log_file_name = value

                line = \
                directory_name + connector + \
                file_name + connector + \
                folder_name + connector + \
                workflow_name + connector + \
                workflow_log_file_directory + connector + \
                workflow_log_file_name + connector + \
                session_log_file_directory + connector + \
                session_log_file_name + connector + \
                endofline
                f.writelines(line)

    try:
        tree.write(file)
    except:
        print "error write files"

f.close()
folder_txt.close()


#write_xml(tree, "./out.xml")
"""

"""
#tree.write('output.xml') 