# 01 — Hyper-V to Azure Migration

> **Scope:** Successful lab **test migration** and data-disk recovery. This project does not claim a final production cutover.

## Objective

Migrate a Hyper-V Windows Server file-server workload into an Azure test environment, validate the recovered data and Windows Remote Desktop access, then export its data disk and attach it to a local Hyper-V virtual machine.

## Environment

| Component | Value |
| --- | --- |
| On-premises Hyper-V source VM | `DB_FileServer` |
| On-premises recovery VM | `DB_AD` |
| Azure resource group | `RG-dblocal` |
| Azure region | Sweden Central |
| Test migration VM | `DB-FileServer-test` |
| Azure jump-host VM | `VM-Server1-dblocal` |
| Test VM internal IP | `10.0.0.5` |
| Jump-host internal IP | `10.0.0.4` |
| Data verification | `E:\Share` and file `Migration to azure test` |

## Workflow

1. Set up Azure Migrate and register the local Hyper-V host.
2. Select `DB_FileServer` and configure migration settings, including compute and disks.
3. Troubleshoot region-policy, provider registration, storage-account and replication errors.
4. Start replication and wait until a recovery point is available.
5. Run a **test migration** and verify that the test VM is created and accessible.
6. RDP into the Azure jump host (which had a public IP) and use Windows Remote Desktop to access `10.0.0.5` across Azure's internal network. The test VM itself did not have a public IP.
7. Check the migrated data disk and validate test data.
8. Create a snapshot, create a disk from the snapshot, and export/download the VHD with AzCopy.
9. In Hyper-V Manager, attach the downloaded VHD to `DB_AD` via **Settings → SCSI Controller → Hard Drive**. When the file did not appear in the picker, changing the filename filter to `*.*` made it visible.
10. Verify `E:\Share` and the test file on `DB_AD`.

## Validation summary

- Azure Migrate test migration succeeded.
- RDP to the test VM worked over the private Azure network through the jump host.
- Migrated data was visible on the Azure test VM.
- The Azure disk export completed with AzCopy.
- The returned data disk was attached to the on-premises `DB_AD` VM, and the test file was accessible.

## Troubleshooting and security

Registration issues, region-policy restrictions, storage-account configuration, and replication errors required troubleshooting. In a production setting, replication would also require explicit network restrictions, encryption, access control, monitoring and a documented rollback strategy.

Avoid public RDP on workloads where possible, restrict administration through an appropriate secure access path, and never publish active SAS tokens or registration secrets. No screenshot is included until manually checked for sensitive information.

## Screenshots

Evidence screenshots will be placed under `screenshots/` **after manual review and redaction**. Use descriptive filenames and reference them from the relevant workflow sections rather than uploading all raw screenshots indiscriminately.

## Lessons learned

Migrating a VM is not only about moving compute: registration, replication health, network access, disk integrity, export and recoverability must all be validated. A **test migration** is not the same as a production cutover.
