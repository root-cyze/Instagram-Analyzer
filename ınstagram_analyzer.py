#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import instaloader
import os
import time
import csv
import argparse
import sys
from datetime import datetime
from getpass import getpass
from colorama import init, Fore, Style
from tqdm import tqdm
from instaloader.exceptions import (
    BadCredentialsException,
    ConnectionException,
    TwoFactorAuthRequiredException,
    ProfileNotExistsException,
    QueryReturnedNotFoundException
)

init(autoreset=True)

def log(msg, status="info"):
    colors = {
        "info": Fore.BLUE,    # Mavi
        "success": Fore.GREEN,       # Yeşil
        "error": Fore.RED,     # Kırmızı (Mor yerine)
        "warn": Fore.YELLOW    # Sarı (Cyan yerine)
    }
    prefix = {
        "info": "[INFO]",
        "success": "[SUCCESS]",
        "error": "[ERROR]",
        "warn": "[WARNING]"
    }
    print(f"{colors.get(status)}{prefix.get(status)} {Style.RESET_ALL}{msg}")

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def logo():
    clear()
    print(f"""
{Fore.RED}╔═════════════════════════════════════════════════════════════════════╗
{Fore.RED}║ {Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}███{Fore.WHITE}╗   {Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}████████{Fore.WHITE}╗ {Fore.BLUE}█████{Fore.WHITE}╗ {Fore.BLUE}██████{Fore.WHITE}╗ {Fore.BLUE}██████{Fore.WHITE}╗  {Fore.BLUE}█████{Fore.WHITE}╗ {Fore.BLUE}███{Fore.WHITE}╗   {Fore.BLUE}███{Fore.WHITE}╗{Fore.RED} ║
{Fore.RED}║ {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}████{Fore.WHITE}╗  {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔════╝╚══{Fore.BLUE}██{Fore.WHITE}╔══╝{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}╔════╝{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}████{Fore.WHITE}╗ {Fore.BLUE}████{Fore.WHITE}║{Fore.RED} ║
{Fore.RED}║ {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔{Fore.BLUE}██{Fore.WHITE}╗ {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}███████{Fore.WHITE}╗   {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}███████{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║     {Fore.BLUE}██████{Fore.WHITE}╔╝{Fore.BLUE}███████{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔{Fore.BLUE}████{Fore.WHITE}╔{Fore.BLUE}██{Fore.WHITE}║{Fore.RED} ║
{Fore.RED}║ {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║╚{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}║╚════{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║     {Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}╔══{Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║╚{Fore.BLUE}██{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}║{Fore.RED} ║
{Fore.RED}║ {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║ ╚{Fore.BLUE}████{Fore.WHITE}║{Fore.BLUE}███████{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║╚{Fore.BLUE}██████{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║  {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}║ ╚═╝ {Fore.BLUE}██{Fore.WHITE}║{Fore.RED} ║
{Fore.RED}║ {Fore.WHITE}╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝{Fore.RED} ║
{Fore.RED}╠═════════════════════════════════════════════════════════════════════╣
{Fore.RED}║ {Fore.BLUE}            Instagram Master Analyzer v2.0 - Premium Edition           {Fore.RED}║
{Fore.RED}║ {Fore.GREEN}                     Developer: @cyze                           {Fore.RED}║
{Fore.RED}║ {Fore.MAGENTA}                 Updated: {datetime.now().strftime('%d.%m.%Y')}                          {Fore.RED}║
{Fore.RED}╚═════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """)


def instagram_login(username, password):
    spinner = ['|', '/', '-', '\\']
    log(f"Logging in as {username}...", "info")
    
    try:
        L = instaloader.Instaloader()
        
        # Spinner göster
        for i in range(12):
            sys.stdout.write(f"\r{Fore.BLUE}[{spinner[i % 4]}] Attempting login...{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
            
        # Giriş yap
        L.login(username, password)
        print("\r" + " " * 50, end="\r")  # Spinner temizle
        log(f"Login successful! Welcome, {username}", "success")
        return L
        
    except BadCredentialsException:
        print("\r" + " " * 50, end="\r")  # Spinner temizle
        log("Invalid credentials. Please check your username and password.", "error")
    except TwoFactorAuthRequiredException:
        print("\r" + " " * 50, end="\r")  # Spinner temizle
        log("2FA required. Complete authentication first.", "error")
    except ConnectionException:
        print("\r" + " " * 50, end="\r")  # Spinner temizle
        log("No internet connection detected. Please check your connection.", "error")
    except Exception as e:
        print("\r" + " " * 50, end="\r")  # Spinner temizle
        log(f"Unexpected error: {str(e)}", "error")
    
    sys.exit(1)

def analyze(L, target):
    try:
        log(f"Fetching profile: {target}")
        profile = instaloader.Profile.from_username(L.context, target)
        
        # Profil bilgilerini göster
        log(f"Profile found: {profile.full_name} (@{profile.username})", "success")
        log(f"Bio: {profile.biography[:50]}..." if len(profile.biography) > 50 else f"Bio: {profile.biography}")
        log(f"Posts: {profile.mediacount} | Following: {profile.followees} | Followers: {profile.followers}")

        # Takip edilenler (following) listesini al
        following = set()
        with tqdm(desc="Following", unit="user", ncols=70) as bar:
            for f in profile.get_followees():
                following.add(f)
                bar.update(1)
                time.sleep(0.01)  # Rate-limiting'i önlemek için

        # Takipçiler (followers) listesini al
        followers = set()
        with tqdm(desc="Followers", unit="user", ncols=70) as bar:
            for f in profile.get_followers():
                followers.add(f)
                bar.update(1)
                time.sleep(0.01)  # Rate-limiting'i önlemek için

        return following, followers
        
    except ProfileNotExistsException:
        log(f"Profile {target} does not exist. Please check the username.", "error")
    except QueryReturnedNotFoundException:
        log(f"Error fetching data for profile: {target}. Please try again later.", "error")
    except Exception as e:
        log(f"Error analyzing profile: {str(e)}", "error")
    
    sys.exit(1)

def export_results(filename, users):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Users not following you back - {datetime.now()}\n\n")
            for i, user in enumerate(sorted(users, key=lambda x: x.username.lower()), 1):
                f.write(f"{i}. {user.username} ({user.full_name})\n")
        log(f"Results saved to {filename}", "success")
    except Exception as e:
        log(f"Error saving results: {str(e)}", "error")

def export_csv(filename, users):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['No', 'Username', 'Full Name', 'Profile URL'])
            for i, user in enumerate(sorted(users, key=lambda x: x.username.lower()), 1):
                writer.writerow([i, user.username, user.full_name, f"https://instagram.com/{user.username}"])
        log(f"CSV saved to {filename}", "success")
    except Exception as e:
        log(f"Error exporting CSV: {str(e)}", "error")

def show_stats(following, followers):
    not_following_back = following - followers
    not_following = followers - following
    
    print(f"\n{Fore.BLUE}--- STATISTICS ---{Style.RESET_ALL}")
    print(f"You follow: {len(following)}")
    print(f"Followers : {len(followers)}")
    print(f"Not following you back: {Fore.RED}{len(not_following_back)}{Style.RESET_ALL}")
    
    # Karşılıklı takip istatistikleri
    mutual = following & followers
    mutual_count = len(mutual)
    
    # Diğer istatistikler
    print(f"Mutuals: {mutual_count} ({(mutual_count / len(following) * 100):.2f}% of following)")
    print(f"Users you don't follow back: {len(not_following)}")
    
    return not_following_back

def main():
    try:
        logo()
        parser = argparse.ArgumentParser(description="Instagram Follower Analyzer")
        parser.add_argument("-u", "--username", help="Instagram Username")
        parser.add_argument("-t", "--target", help="Target account to analyze (defaults to your own)")
        args = parser.parse_args()

        user = args.username or input(f"{Fore.BLUE}Username: {Style.RESET_ALL}")
        pwd = getpass(f"{Fore.BLUE}Password: {Style.RESET_ALL}")

        # Instagram'a giriş yap
        L = instagram_login(user, pwd)
        
        # Hedef kullanıcı (kendisi veya başka biri)
        target = args.target or user
        
        # Analiz yap
        following, followers = analyze(L, target)
        not_following_back = show_stats(following, followers)

        # Kullanıcıya seçenek sun
        print(f"\n{Fore.BLUE}[1]{Style.RESET_ALL} Export results to TXT")
        print(f"{Fore.BLUE}[2]{Style.RESET_ALL} Export results to CSV")
        print(f"{Fore.BLUE}[3]{Style.RESET_ALL} Export both formats")
        print(f"{Fore.BLUE}[4]{Style.RESET_ALL} Exit without exporting")
        
        choice = input(f"\n{Fore.BLUE}Choice: {Style.RESET_ALL}")
        
        if choice == "1":
            export_results(f"{target}_not_following_back.txt", not_following_back)
        elif choice == "2":
            export_csv(f"{target}_not_following_back.csv", not_following_back)
        elif choice == "3":
            export_results(f"{target}_not_following_back.txt", not_following_back)
            export_csv(f"{target}_not_following_back.csv", not_following_back)
        elif choice == "4":
            log("Exiting without exporting data.", "info")
        else:
            log("Invalid choice. Exiting.", "warn")
            
        log("Analysis completed. Thank you for using Instagram Master Analyzer!", "success")
        
    except KeyboardInterrupt:
        print()  # Yeni satır
        log("Program interrupted by user. Exiting...", "warn")
    except Exception as e:
        log(f"Unexpected error: {str(e)}", "error")

if __name__ == "__main__":
    main()
