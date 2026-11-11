# Security considerations

- Limit synchronization scope to the intended organizational unit using the selected-OU filter.
- Apply least privilege to directory and tenant administration accounts.
- Protect service credentials and provisioning-agent registration materials; never commit them to a public repository.
- Review password-hash synchronization policy and authentication controls according to organizational requirements.
- Ensure directory objects do not expose unnecessary personal attributes or permissions.
- Redact identifiable names, tenant/account information, object IDs, and internal configuration secrets from public screenshots.
- Consider monitoring, lifecycle management, and change control for a real deployment; the student lab did not establish production readiness.

The screenshots are snapshots of an educational environment that is no longer active.
