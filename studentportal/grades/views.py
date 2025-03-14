import pandas as pd
from django.shortcuts import render,redirect
from django.contrib import messages
from grades.models import Grades

# Create your views here.

def grade_upload(request):
    if request.method == 'POST':
        if "file" not in request.FILES:
            print("No file")

        excel_file = request.FILES['grades']
        print(f"Received file: {excel_file.name} Size:{excel_file.size}")

        try:
            xls = pd.ExcelFile(excel_file, engine="openpyxl")

            identifier_sheet = "SETUP"
            if identifier_sheet not in xls.sheet_names:

                messages.error(request,f"The '{identifier_sheet}' was not found")
                return redirect('home:teacher-home')
            
            identifier_df = pd.read_excel(xls, sheet_name=identifier_sheet,engine="openpyxl")

            grade_type = identifier_df.iloc[6,1]
            
            if grade_type == "LECTURE":
                sheet_name = "ONLINE_F2F_GRADES_LECONLY"

            elif grade_type == "LAB":
                sheet_name = "ONLINE_F2F_GRADES_LEBLACONLY"

            df = pd.read_excel(xls, sheet_name=sheet_name, engine="openpyxl")

            required_columns = ["USN/STUDENT ID", "SUBJECT CODE", "SUBJECT TITLE", "SEMESTER", "YEAR", "FINAL GRADE"]
            if not all(col in df.columns for col in required_columns):
                messages.error(request,"Sheet invalid, required columns could not be found")
                return redirect('home:teacher-home')
            
            for _, row in df.iterrows():
                Grades.objects.create(
                    student_usn=row["USN/STUDENT ID"],
                    subject_code=row["SUBJECT CODE"],
                    subject_name=row["SUBJECT TITLE"],
                    semester=row["SEMESTER"],
                    year=row["YEAR"],
                    grade_value=row["FINAL GRADE"]
                )

                messages.success(request,"Grades have been uploaded successfully!")
                return redirect('home:teacher-home')

        except Exception as e:
            print(e)
            messages.error(request,f"Error processing file: {e}")
            return redirect('home:teacher-home')