import os
import pandas
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

STU_CSV_FILE = os.getenv('STU_CSV_FILE')
INDEX_COL = os.getenv('INDEX_COL')

AGE_CRITERIA = {
	"Minor" : "minor",
	"Middle_Age": "middle_age",
	"Senior" : "senior" 
}

class ReadStudentDetailsCSV():

	def __init__(self):
		pass

	def create_data_frame(self, file_path, index_col):
		return pandas.read_csv(STU_CSV_FILE, sep=r'\s*,\s*', header=0, encoding='ascii', engine='python')

	def create_student_details_dict(self):
		df = self.create_data_frame(STU_CSV_FILE, INDEX_COL)
		for index, row in df.iterrows():
			print(index)
			full_name = f"{row.get('stuf_name')} {row.get('stul_name')}"
			print("Full Name", full_name)
			user_name = self.get_username(row.get('stuf_name'),row.get('stul_name') )
			print("Username", user_name)
			stu_age = self.get_age(row.get('stu_dob'))
			print("Age", stu_age)
			age_criteria = self.check_age(stu_age) if stu_age else None
			print("Age Criteria", age_criteria)

			

	def get_username(self, first_name, last_name):
		return f"{first_name[0:4]}{last_name[0:4]}" if first_name and last_name else None

	def get_age(self, dob):
		return datetime.now().year - datetime.strptime(dob, "%Y-%m-%d").year if dob else None

	def check_age(self, age):
		age_criteria = None
		if age < 18:
			age_criteria = AGE_CRITERIA.get("Minor")
		elif 18 <= age <= 40:
			age_criteria = AGE_CRITERIA.get("Middle_Age")
		elif age > 40:
			age_criteria = AGE_CRITERIA.get("Senior")
		return age_criteria


run = ReadStudentDetailsCSV().create_student_details_dict() 
