import os
from fastmcp import FastMCP
from tools import (
    marks_to_grade_points, calculate_semester_gpa, calculate_new_cgpa,
    required_gpa_for_target, get_semester_courses,
    get_remaining_credit_hours, save_report,
)

mcp = FastMCP("cgpa")

for fn in [marks_to_grade_points, calculate_semester_gpa, calculate_new_cgpa,
           required_gpa_for_target, get_semester_courses,
           get_remaining_credit_hours, save_report]:
    mcp.tool(fn)

if __name__ == "__main__":
    # Locally: 127.0.0.1:8000. On a host like Render, PORT is set and we must bind 0.0.0.0.
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0" if "PORT" in os.environ else "127.0.0.1"
    mcp.run(transport="http", host=host, port=port)