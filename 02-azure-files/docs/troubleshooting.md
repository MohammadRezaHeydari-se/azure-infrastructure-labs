# Troubleshooting and verification boundaries

## SMB connectivity

The original PowerShell screenshot includes a `Test-NetConnection` command to the Azure Files endpoint on TCP port `445`, which is a useful first check when a file share cannot be mounted. A blocked outbound port, DNS error, or incorrect endpoint can prevent SMB connectivity.

## Authentication and drive mapping

A drive may fail to mount due to incorrect credentials, an expired or rotated key, or an incorrect UNC path. The original screenshot contains credential-related commands but does not document a specific authentication failure or how it was resolved. **No specific failure is claimed.**

## What was successfully verified

- A Windows mapped drive labeled `Z:` connected to the Azure Files share.
- Three test files appeared through Windows File Explorer.
- The same file names appeared in the Azure Storage browser.

## Missing historical evidence

The two relevant screenshots do not independently establish the Storage Account creation wizard, account networking rules, a complete saved PowerShell script, or key lifecycle settings. These are noted as evidence gaps rather than reconstructed as completed steps.
