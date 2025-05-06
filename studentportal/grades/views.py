import pandas as pd
import zipfile
from django.shortcuts import render,redirect
from django.contrib import messages
from grades.models import Grades
from grades.forms import edit_grade
from django.db import IntegrityError

# Create your views here.

def grade_upload(request):
   if request.method == 'POST':
      

        if "grades" not in request.FILES:
            print("File Checking")
            messages.warning(request, "No file uploaded.")
            return redirect('home:teacher-home')

        excel_file = request.FILES['grades']
    

        try:
            # Load Excel file
            xls = pd.ExcelFile(excel_file, engine="openpyxl")

            # Check if the SETUP sheet exists
            identifier_sheet = "SETUP"
            if identifier_sheet not in xls.sheet_names:
                messages.warning(request, f"The '{identifier_sheet}' sheet was not found.")
                print("SETUP sheet not found")
                return redirect('home:teacher-home')

            # Read SETUP sheet to determine grade type
            identifier_df = pd.read_excel(xls, sheet_name=identifier_sheet, engine="openpyxl")
          
            grade_type = str(identifier_df.iloc[5, 1]).strip()  # Read B6 cell
           

            if grade_type not in ["LECTURE", "LAB"]:
                messages.warning(request, "Invalid sheet type. Please use a valid grade sheet.")
                return redirect('home:teacher-home')

            # Select the appropriate sheet based on grade type
            if grade_type == "LAB":
                sheet_name = "ONLINE_F2F_GRADES_LABLECONLY"

            elif grade_type == "LECTURE":
                sheet_name = "ONLINE_F2F_GRADES_LECONLY"

            if sheet_name not in xls.sheet_names:
                messages.warning(request, f"The expected sheet '{sheet_name}' is missing.")
                return redirect('home:teacher-home')

            # Read the selected sheet
            df = pd.read_excel(xls, sheet_name=sheet_name, engine="openpyxl")
            
            print(df.columns.tolist())
            # Required columns check
            required_columns = ["USN/STUDENT ID", "SUBJECT CODE", "SUBJECT TITLE", "SEMESTER", "YEAR", "FINAL GRADE"]
            if not all(col in df.columns for col in required_columns):
                messages.warning(request, "Invalid sheet format. Required columns are missing.")
                return redirect('home:teacher-home')
            
            df["FINAL GRADE"] = pd.to_numeric(df["FINAL GRADE"], errors='coerce')
            df = df.dropna(subset=["FINAL GRADE"])

            # Save grades to the database
            for _, row in df.iterrows():                
                try:
                    grade_value = float(row["FINAL GRADE"])
                except:
                    continue
            
                student_usn = str(row["USN/STUDENT ID"]).split(".")[0]
                subject_code = row["SUBJECT CODE"].strip()
       
                try:
                    Grades.objects.update_or_create(
                        student_usn=student_usn,
                        subject_code=subject_code,
                        subject_name=row["SUBJECT TITLE"].strip(),
                        semester=row["SEMESTER"],
                        year=row["YEAR"],
                        defaults={
                            "grade_value":grade_value
                        }
                    )
                except IntegrityError:
                    messages.warning(request,"Duplicate entries detected, please enter new grades")
                    return redirect('home:upload-grades')

            messages.success(request, "Grades uploaded successfully!")
            return redirect('home:upload-grades')
        
        except zipfile.BadZipFile:
            messages.warning(request, "Invalid file format, please upload a .xlsx or xls file!")
            return redirect('home:upload-grades')

        except Exception as e:
            messages.warning(request, f"Error processing file: {e}")
            return redirect('home:upload-grades')
        

def grade_edit(request):
    if request.method == "POST":
        grade_id = request.POST.get('gradeID')
        grade_instance = Grades.objects.get(id=grade_id)
        form = edit_grade(request.POST, instance=grade_instance)
        if form.is_valid():
            form.save()
            messages.success(request,'Grade changed successfully!')
            return redirect('home:grade-list')
        else:
            messages.warning(request, form.errors)
            return redirect('home:grade-list')