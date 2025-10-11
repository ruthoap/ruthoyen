.PHONY : clean

index.html : src/index.xlsx
	python scripts/excel_to_html.py -i src/index.xlsx -o index.html

# 出力を削除
clean:
	rm -f index.html
	rm -rf index_files/