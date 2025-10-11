import win32com.client
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Convert Excel file to HTML using Excel COM interface.")
    parser.add_argument('-i', '--input', required=True, help='Input Excel file (.xlsx)')
    parser.add_argument('-o', '--output', required=True, help='Output HTML file (.html)')

    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    output_path = os.path.abspath(args.output)

    if not os.path.isfile(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)

    # 🔥 上書き確認ダイアログを防ぐため、事前に削除
    if os.path.exists(output_path):
        try:
            os.remove(output_path)
        except Exception as e:
            print(f"Error deleting existing output file: {e}")
            sys.exit(1)

    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False

    try:
        wb = excel.Workbooks.Open(input_path)
        wb.SaveAs(output_path, FileFormat=44)  # 44 = xlHtml
        wb.Close(False)
        print(f"✅ Saved: {output_path}")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
    finally:
        excel.Quit()

if __name__ == "__main__":
    main()
