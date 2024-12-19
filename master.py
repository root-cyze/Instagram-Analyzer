import instaloader
import os
import time
import csv
import argparse
import platform
from getpass import getpass
from instaloader.exceptions import (
    BadCredentialsException,
    ConnectionException,
    TwoFactorAuthRequiredException,
    ProfileNotExistsException,
    QueryReturnedNotFoundException
)

# Platform bağımsız ekran temizleme fonksiyonu

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# ASCII Logonuzu gösteren fonksiyon
def print_logo():
    print("""
                                                                                                    
                             !.                                                             
                            !Y~                                                             
                           :YJ7^                                                            
                           J5J77.                                                           
                          !55J77!                                                           
                         :YYY:~77^                                                          
                        .J55! .!77:                                                         
       .^^^:::::::::::::!55?   ^77!:::::^^^^^^^^^^^^^^^::::::::.........                    
        :~?YYJJ??7!~^^~~~~7:    ^~^^^^^:::::........                                        
           .~?Y555Y?~.                                                                        
              :~?Y555Y?~.        ⭐ Instagram Master Analyzer                                                             
                 :!JYYYY?.       ⭐ Developer by @archescyber                                                             
                    ^JJJ^    .                                                             
                    !JJ!  .:~77:                                                            
                   ^JJ?::~!!!7JJ7:                                                          
                  .?J?!~!!!!~^!?JJ!:                                                        
                  7J?!!!!~:.   .^!JJ!.                                                      
                 ~J7!!~:.         .^7?!.                                                    
                :?7~^.               .~!~.                                                  
                ~^.                     :^:                                                 
    """)

# Instagram'a giriş fonksiyonu
def login_to_instagram(username, password):
    L = instaloader.Instaloader()

    try:
        L.login(username, password)
        return L
    except BadCredentialsException:
        print("[INFO] Invalid username or password. Please check your credentials and try again.")
        exit()
    except TwoFactorAuthRequiredException:
        print("[INFO] Two-factor authentication is required. Please authenticate and try again.")
        exit()
    except ConnectionException:
        print("[INFO] Connection error. Please check your internet connection.")
        exit()

# Kullanıcı takipçi ve takip edilen analizini yapma
def analyze_followers(L, username, start_user, end_user):
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        following = set(profile.get_followees())
        followers = set(profile.get_followers())

        # Başlangıç ve bitiş kullanıcı adlarını kullanarak analiz sınırlandırma
        if start_user and end_user:
            following = {user for user in following if start_user <= user.username <= end_user}
            followers = {user for user in followers if start_user <= user.username <= end_user}

        return following, followers
    except ProfileNotExistsException:
        print("[INFO] The profile does not exist.")
        exit()
    except QueryReturnedNotFoundException:
        print("[INFO] Failed to fetch the profile data. Please try again later.")
        exit()

# Dosyaya yazma işlemi
def save_to_file(filename, not_following_back):
    try:
        with open(filename, "w") as file:
            file.write("Users Who Do Not Follow You Back:\n")
            file.write("-" * 30 + "\n")
            for idx, user in enumerate(not_following_back, start=1):
                file.write(f"{idx}. {user.username}\n")
            file.write("-" * 30 + "\n")
            file.write(f"Total: {len(not_following_back)} user.\n")
        print(f"[INFO] The data has been saved in {filename}.")
    except Exception as e:
        print(f"[INFO] Error while saving data to file: {e}")
        exit()

# CSV formatında kaydetme işlemi
def save_to_csv(filename, not_following_back):
    try:
        with open(filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["User", "Username"])
            for user in not_following_back:
                csv_writer.writerow([user.full_name, user.username])
        print(f"[INFO] The data has been saved in CSV format in {filename}.")
    except Exception as e:
        print(f"[INFO] Error while saving data to CSV: {e}")
        exit()

# API sınırlamalarını aşmamak için bekleme fonksiyonu
def sleep_to_avoid_api_limits(sleep_time):
    print(f"[INFO] Sleeping for {sleep_time} seconds to avoid hitting API limits...")
    time.sleep(sleep_time)

# Komut satırı argümanlarını analiz etme
def parse_arguments():
    parser = argparse.ArgumentParser(description="Instagram follower analysis tool.")
    parser.add_argument("username", help="Instagram username")
    parser.add_argument("password", help="Instagram password")
    parser.add_argument("--start_user", help="The username to start analyzing (optional).", default=None)
    parser.add_argument("--end_user", help="The username to end analyzing (optional).", default=None)
    parser.add_argument("--file_format", choices=['txt', 'csv'], default='txt', help="The format to save the results (txt/csv). Default is txt.")
    parser.add_argument("--sleep_time", type=int, default=10, help="Time to sleep (in seconds) to avoid hitting Instagram API limits.")
    return parser.parse_args()

# Ana fonksiyon
def main():
    # Logo yazdır
    print_logo()

    args = parse_arguments()

    # Ekranı temizle
    clear_screen()

    print("[INFO] The processing time is approximately 1 or 2 minutes.")
    print("[INFO] Too many consecutive attempts may trigger Instagram API limits.")
    print("[INFO] Please ensure your credentials are correct before continuing.\n")

    # Kullanıcı adı ve şifre
    username = args.username
    password = args.password

    print("\n[INFO] Logging in... Please wait.")
    L = login_to_instagram(username, password)

    print("\n[INFO] Analyzing followers and followers... Please wait.")
    following, followers = analyze_followers(L, username, args.start_user, args.end_user)

    # Takip etmeyenleri bulma
    not_following_back = following - followers

    # Kullanıcıya takip etmeyenlerin sayısı hakkında bilgi
    if len(not_following_back) == 0:
        print("[INFO] All users are following you back! Great job!")
    else:
        print(f"[INFO] Found {len(not_following_back)} users who do not follow you back.")

    # Dosya kaydetme
    filename = f"{username}-analyze.{args.file_format}"

    if args.file_format == 'txt':
        save_to_file(filename, not_following_back)
    elif args.file_format == 'csv':
        save_to_csv(filename, not_following_back)

    # API sınırlamaları için bekleme süresi
    sleep_to_avoid_api_limits(args.sleep_time)

# Programı çalıştır
if __name__ == "__main__":
    main()
