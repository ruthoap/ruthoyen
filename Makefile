.PHONY : clean

index.html : src/index.xlsx
	python scripts/excel_to_html.py -i src/index.xlsx -o index.html
	python scripts/excel_to_html_postfix.py

clean:
	rm -f index.html
	rm -rf index_files/