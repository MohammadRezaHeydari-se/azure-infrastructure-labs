# Troubleshooting and lessons learned

The original lab evidence includes screenshots of the following issues; only a reviewed subset is published in the portfolio. Descriptions below are intentionally restricted to what the lab notes support.

| Problem | Observed impact | Resolution / learning |
| --- | --- | --- |
| Azure policy / allowed-region restrictions | Some target configuration options were blocked | Inspect allowed regions and align migration settings with permitted Azure region and subscription constraints |
| Registration-key download and Hyper-V provider setup | Hyper-V host registration was interrupted | Troubleshoot registration and provider installation until Azure Migrate showed the host connected |
| Azure storage-account configuration issue | Replication setup did not initially succeed | Review storage-account requirements and related settings, then retry configuration |
| Replication job failed | Workload was not immediately ready to test | Inspect the failed job and continue only after replication started and a recovery point became available |
| Test migration job-related issue | Job tracking was part of troubleshooting | Confirm eventual **Test migration** success through the job status rather than assuming success from VM creation alone |
| No direct RDP path to the test VM | Migrated test VM had only private IP `10.0.0.5` | Use Windows RDP to an Azure jump VM and then RDP to `10.0.0.5` inside Azure |
| VHD not listed in Hyper-V file picker | Downloaded file could not be selected using the default file filter | Change the file filter to `*.*`, select the VHD and attach via SCSI Controller → Hard Drive |

## What I learned

- Replication readiness depends on successful registration, regional policy compliance and working recovery-point creation.
- A successful test migration should be verified at the workload level, including disk data and remote access.
- Exporting a disk is not the same as verifying that it can be attached and read on the destination hypervisor.
- Documentation should distinguish screenshots from steps established by operator observation.
