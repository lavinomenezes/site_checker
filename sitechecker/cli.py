# imports
import argparse
import os
from datetime import datetime

# Function to receive an argument in the terminal.
def read_user_cli_args():
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="insira um ou mais URLs",
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="csv_file",
        type=str,
        help='insira um arquivo csv contendo as urls'
    )
    return parser.parse_args()

# function to display and save results
def display_check_result(result, url, error=""):
    # define actual date
    hour = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # File name that will be created in case it doesn't exist.
    filename = "output.txt"

    # Verify the existence.
    if not os.path.exists(filename):
    # If it doesn't exist, create it.
        print('Arquivo "output.txt" criado para salvar resultados\n')
        open(filename, "w").close()
    
    print(f'O status da "{url}" é:', end=" ")
    if result:
        # display the result ans save in the file
        print('"Online as: {}'.format(hour))
        with open(str(os.getcwd()) + '/output.txt','a') as f:
            f.write('O status da "{}" é: Online as: {}\n'.format(url,hour))
    else:
        print(f'"Offline?"  \n  Erro: "{error}"')
        with open(str(os.getcwd()) + '/output.txt','a') as f:
            f.write(f'O status da "{url}" é: "Offline?"  \n  Erro: "{error}"\n')