# impots
import sys
import csv
from sitechecker.checker import site_is_online
from sitechecker.cli import read_user_cli_args, display_check_result


def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)

def main():
    column = []
    user_args = read_user_cli_args()
    urls = user_args.urls
    if user_args.file:
        with open(user_args.file,newline='') as f:
            read = csv.reader(f)
            urls += [row[0] for row in read]
    if not urls:
        print("Erro: sem URLs para analisar.", file=sys.stderr)
        sys.exit(1)
    _site_check(urls)




if __name__ == "__main__":
    
    main()
