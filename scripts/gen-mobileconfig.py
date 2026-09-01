#!/usr/bin/env python3
"""Generate Apple mobileconfig for Stalwart mailboxes with embedded password."""
import argparse
import plistlib
import uuid
import pathlib

def generate(email, password, display_name, org, host="mail.darideveloper.com", embed_password=False):
    user = email.split("@")[0]
    # outer identifiers
    outer_uuid = str(uuid.uuid4())
    inner_uuid = str(uuid.uuid4())
    # Use user-specific identifiers to avoid collisions when both profiles installed
    outer_id = f"com.conhilodepilo.mail.{user}"
    inner_id = f"com.conhilodepilo.mail.{user}.account"

    inner = {
        "EmailAccountDescription": display_name,
        "EmailAccountName": display_name,
        "EmailAccountType": "EmailTypeIMAP",
        "EmailAddress": email,
        "IncomingMailServerAuthentication": "EmailAuthPassword",
        "IncomingMailServerHostName": host,
        "IncomingMailServerPortNumber": 993,
        "IncomingMailServerUseSSL": True,
        "IncomingMailServerUsername": email,
        "OutgoingMailServerAuthentication": "EmailAuthPassword",
        "OutgoingMailServerHostName": host,
        "OutgoingMailServerPortNumber": 465,
        "OutgoingMailServerUseSSL": True,
        "OutgoingMailServerUsername": email,
        "OutgoingPasswordSameAsIncomingPassword": True,
        "PayloadDescription": f"{display_name} email account",
        "PayloadDisplayName": f"{display_name} Mail",
        "PayloadIdentifier": inner_id,
        "PayloadType": "com.apple.mail.managed",
        "PayloadUUID": inner_uuid,
        "PayloadVersion": 1,
    }

    outer = {
        "PayloadContent": [inner],
        "PayloadDescription": f"Installs the {display_name} email account (IMAP + SMTP) on this device.",
        "PayloadDisplayName": f"{display_name} Mail",
        "PayloadIdentifier": outer_id,
        "PayloadOrganization": org,
        "PayloadType": "Configuration",
        "PayloadUUID": outer_uuid,
        "PayloadVersion": 1,
    }
    return outer

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--email", required=True)
    p.add_argument("--password", required=True)
    p.add_argument("--display-name", default=None)
    p.add_argument("--org", default="Con Hilo Depilo")
    p.add_argument("--host", default="mail.darideveloper.com")
    p.add_argument("--out", required=True)
    args = p.parse_args()
    if args.display_name:
        display = args.display_name
    elif args.email.startswith("info@"):
        display = "Info - Con Hilo Depilo"
    else:
        display = f"{args.email.split('@')[0].capitalize()} - Con Hilo Depilo"
    data = generate(args.email, args.password, display, args.org, args.host)
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "wb") as f:
        plistlib.dump(data, f, fmt=plistlib.FMT_XML, sort_keys=False)
    # restrict perms since password in plaintext
    try:
        out.chmod(0o600)
    except: pass
    print(f"Wrote {out} for {args.email} (outer {data['PayloadUUID']})")

if __name__ == "__main__":
    main()
