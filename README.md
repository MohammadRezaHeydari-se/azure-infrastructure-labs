# Azure Infrastructure Labs

Practical Microsoft Azure and hybrid infrastructure labs from my DevOps Engineer studies at Nackademin, Sweden.

Each project is documented separately with its objective, environment, technical steps, evidence, troubleshooting, security considerations and lessons learned. All claims in this portfolio are based on work performed in the lab.

## Projects

| Project | Scope | Status |
| --- | --- | --- |
| [01 — Hyper-V to Azure migration](01-hyperv-to-azure-migration/README.md) | Azure Migrate, test migration, RDP, disk export and on-premises recovery | Documented; screenshot review pending |
| 02 — Azure Files | Storage account and Azure file share | Planned |
| 03 — Entra ID sync | Hybrid identity and selected OU synchronization | Planned |
| 04 — Azure VM and Ansible | Linux and infrastructure automation | Planned |

## Contribution workflow

Work on a dedicated branch per project, open a pull request into `main`, and wait for the [lightweight validation workflow](.github/workflows/validate.yml) to pass before merging.

Branch examples: `project/01-hyperv-to-azure-migration`, `project/02-azure-files`, `project/03-entra-id-sync`.

The CI checks Markdown links to local files, basic repository structure, and selected secret patterns in **tracked text files**. It does **not** verify the truth of lab work, inspect image contents, or replace a manual security review.

## Security

Never commit passwords, SAS tokens, storage account keys, registration keys, connection strings, or VM disk exports. **Review and redact screenshots before uploading them**, since automated text checks cannot see secrets in images. Public IP addresses and subscription/account identifiers should be reviewed for exposure.

## License

No license has been selected. All rights are reserved unless a license is added later.
