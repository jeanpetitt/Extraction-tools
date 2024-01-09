import json
import os
im


def Annotate_pdf(pdf_path):
    list_pdf = os.listdir(pdf_path)

    annotations = []
    for pdf in list_pdf:
        with pdfplumber.open(f"{pdf_path}/{pdf}", 'r') as pdf_file:

            # Extract all the pdf pages
            pages = pdf_file.pages

            # Initialize an empty list to store the annotation

            # browse eache page
            for i, page in enumerate(pages):
                # Extract all the tables of page
                tables = page.extract_tables()

                # Browse each table
                for j, table in enumerate(tables):
                    # compute index of the char where begin the table
                    start = page.extract_text().index(str(table))

                    #  compute index of the table where the table are finish
                    end = start + len(str(table))

                    # Add annotation to the list
                    annotations.append(
                        {
                            "start": start,
                            "end": end,
                            'data': table
                        }
                    )
    # Save annotations in the json file
    with open('annoted/annotate.json', 'w+') as jsonfile:
        json.dump(annotations, jsonfile)
