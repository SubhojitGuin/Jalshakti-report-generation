from api_helper import get_data_from_sql , get_data_from_text
import pandas as pd
import pdfkit


def generate_report(State_name):
  question_NOC = "Give the detailed NOC quidelines"
  response = get_data_from_text(question_NOC, "NOC")

  options = {"page-size": "Letter"}

  pdf_output = pdfkit.from_string(response, False, options=options)

  return pdf_output
  