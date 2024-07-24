import os
import openpyxl

# Set the path for the Excel file
file_path = 'E:\Desktop 2\My Data\My\My Code\Folder Create\CCP Data.xlsx'

# Load the Excel file
wb = openpyxl.load_workbook(file_path)

# Get the name of the sheet
sheet_name = wb.worksheets[0].title

# Set the path for the new folder
folder_path = 'E:/Desktop 2/My Data/My/My Code/Folder Create/my_folder/' + sheet_name

# Create the folder
os.mkdir(folder_path)
