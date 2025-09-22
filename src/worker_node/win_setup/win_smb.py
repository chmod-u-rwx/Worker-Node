import os
import subprocess
import argparse
import pyuac #type:ignore
from pathlib import Path

def create_smb_dir(path: Path, smb_name:str= "CCqemu", username:str = "cc_qemu", password:str = "qemu") -> None:    
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            raise RuntimeError(f"Failed to create mount directory {path}: {e}")
    _enable_smb()
    _create_dummy_user(username=username,password=password)
    _set_smb_permissions(path=path,smb_name=smb_name,username=username)


def _enable_smb():
    path = os.path.abspath("enable_smb.ps1")
    try:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", path], check=True)
    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to enable SMB Direct feature.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred while enabling SMB Direct: {e}")

def _set_smb_permissions(path: Path , smb_name:str = "CCqemu", username:str = "cc_qemu") -> None:
    try:

        subprocess.run(["powershell", "-Command", f"New-SmbShare -Name {smb_name} -Path '{path}' -FullAccess {username}"],check=True)
        subprocess.run(["icacls", path, "/grant", f"{username}:(OI)(CI)F"], check=True)
    except subprocess.CalledProcessError:
        pass # we pass incase error raises that share already exists
    except Exception as e:
        raise RuntimeError(f"Failed to set SMB permissions: {e}")

def _create_dummy_user(username: str = "cc_qemu", password: str = "qemu"):
    try:
        subprocess.run(["net", "user", username, password, "/add"], check=True, shell=True)
    except subprocess.CalledProcessError:
        pass # we pass incase error raises that user already exists
    except Exception as e:
        raise RuntimeError(f"Failed to create dummy user: {e}")  
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("path", type=str)
    parser.add_argument("--smb_name", default="CCqemu", type=str)
    parser.add_argument("--username", default="cc_qemu", type=str)
    parser.add_argument("--password", default="qemu", type=str)

    args = parser.parse_args()
    if not pyuac.isUserAdmin():
        pyuac.runAsAdmin() #type:ignore
    create_smb_dir(path=args.path, smb_name=args.smb_name, username=args.username, password=args.password)