# Security considerations — Azure Files

## Storage Account Key

The historical Azure Portal screenshot explicitly shows `Access key` as the selected authentication method for browsing the share. The original Windows PowerShell evidence also contains a credential-related command line. For that reason, the published Windows screenshot excludes the PowerShell window.

A storage account key provides broad access to the storage account and must be treated as a secret. It should never be embedded in a public repository, command history transcript, or screenshot. If an active key has been exposed, rotate it and update dependent clients.

## Safer approaches for production

- Prefer identity-based SMB authentication where supported, including relevant Microsoft Entra/Kerberos or AD DS integration, rather than distributing account keys to users.
- Use Azure RBAC for management-plane access and least privilege for data access as appropriate.
- Restrict network exposure, consider private endpoints and DNS design, and enforce suitable firewall controls.
- Use secure SMB transport, monitor access, and maintain recovery and backup procedures.
- Use short-lived scoped SAS only when appropriate and supported for the operation; SAS does not replace SMB identity-based access control.

These are **recommendations** and must not be read as configurations proven to have been implemented during this lab.

## Screenshot publishing rules

1. Never publish raw command lines containing account keys, connection strings, tokens, or passwords.
2. Remove account identities and unnecessary personal information from Azure Portal screenshots.
3. Review all future screenshots manually before committing them.
4. The original evidence stays outside the public repository.
