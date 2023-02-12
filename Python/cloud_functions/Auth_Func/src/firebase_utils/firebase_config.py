from gcp.codex import f_creds


config = {
    "apiKey": f_creds[0],
    "authDomain": f_creds[1],
    "databaseURL": f_creds[2],
    "storageBucket": f_creds[3]
}
