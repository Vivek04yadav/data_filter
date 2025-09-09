import pandas as pd

input_file = "data.xlsx"
output_file = "final_output.xlsx"


df = pd.read_excel(input_file)

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    
    df.to_excel(writer, sheet_name="All_Data", index=False)

   
    for city, group in df.groupby("City"):
        sheet_name = str(city)[:31]   
        group.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Done ✅  Check your file: {output_file}")
