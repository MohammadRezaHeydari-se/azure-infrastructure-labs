# Migration guide — steps actually performed

This guide describes a lab **test migration**, not a production migration. The resources were later deleted.

## Preparation

1. Prepare an on-premises Hyper-V lab including `DB_FileServer` and `DB_AD`.
2. In Azure, use the migration project and target settings in Sweden Central / `RG-dblocal`.
3. Install and register the Azure Migrate Hyper-V provider, confirm host connection.
4. Select `DB_FileServer` and review target compute and disk settings.

## Replication and testing

5. Address policy/registration/storage-account configuration and replication failures as documented in [Troubleshooting](troubleshooting.md).
6. Start replication; wait for a suitable recovery point.
7. Perform an **Azure Migrate Test migration** and confirm the job reports success.
8. Verify the resulting `DB-FileServer-test` VM, its data disk, and the `E:\Share` data.

## Network access validation

9. Use Remote Desktop from the local computer to an Azure jump host (`VM-Server1-dblocal`, private address `10.0.0.4`, public access during the lab).
10. From inside the jump host, start Windows Remote Desktop and connect to the test VM private address `10.0.0.5`.
11. Verify the Windows desktop and data are accessible. The test VM did not require its own public IP.

## Export and local data recovery

12. Create a snapshot from the Azure test VM data disk.
13. Create a managed disk from that snapshot and export/download VHD using AzCopy. The successful log showed 1 transfer completed, 0 failed, 5,368,709,632 bytes.
14. In Hyper-V Manager, open `DB_AD` settings and choose **SCSI Controller → Hard Drive** to attach the VHD. If it is not shown in the file picker, show all files with `*.*`.
15. Verify that the new disk exposes `E:\Share` and contains `Migration to azure test`.

## Limitations

- No screenshot of the Hyper-V attachment dialogue is included.
- The available file-share screenshot does not by itself prove the precise RDP path; that is documented from the operator's account.
- A test migration and data-disk recovery **do not prove production cutover**.
