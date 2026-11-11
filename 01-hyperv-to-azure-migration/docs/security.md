# Security and cost considerations

## Access and network exposure

- The Azure test VM had a private IP and was accessed by RDP through an Azure jump host, rather than exposing RDP directly from the test VM to the public internet.
- For production, restrict jump-host exposure, use authenticated secure access (for example an approved VPN or Azure Bastion configuration), and apply NSG/firewall rules and MFA where applicable.
- Private IPs alone do not guarantee secure access: identity, route restrictions and firewall policy remain important.

## Migration and data protection

- Use least-privilege Azure RBAC for migration, snapshot, export and storage operations.
- Treat exported data disks and snapshots as sensitive data; define encryption, access, retention and deletion controls.
- SAS tokens, export URLs, account keys, registration secrets and other credentials must not be committed to Git.
- The supplied source screenshot of AzCopy included an SAS URL; the curated public copy covers the entire line containing it.
- The text-based CI validator can catch only some accidental text secrets; **it cannot inspect sensitive pixels in screenshots**.

## Cost and decommissioning

After the lab was completed, its Azure resources were deleted to avoid further costs. This lab should not be interpreted as a continuously running hosted service, production disaster-recovery solution or permanently available VM deployment.

## Public screenshot review checklist

1. Open each image **before** adding it to Git.
2. Check the entire image for SAS URLs, tokens, passwords, keys, personal emails, subscription and tenant identifiers, and unexpectedly sensitive host details.
3. Redact with **opaque shapes**, not reversible blur or semi-transparent overlays.
4. Confirm that the public version still proves the claimed test result.
5. Keep original evidence locally and publish only reviewed copies.
