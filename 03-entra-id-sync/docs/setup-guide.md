# Setup and validation — evidence-based notes

1. Inspect local `db.local` objects in Active Directory Users and Computers and identify the `SyncUsers` OU.
2. In Microsoft Entra admin/ Azure portal, inspect **Microsoft Entra Connect → Cloud Sync** configuration `db.local`.
3. Verify configuration reports **Healthy**, with one enabled agent (as captured in screenshot 04).
4. Inspect **Scoping filters → Selected organizational units** and confirm `OU=SyncUsers,DC=db,DC=local` (screenshot 05).
5. Compare the cloud users/groups screens to the local directory. The captured overview shows 6 users; the group screen shows 3 direct group members (screenshots 04 and 08).
6. Treat screenshots as point-in-time observations: do not infer a successful password login, complete attribute set, or ongoing replication beyond what was captured.

This guide describes verified evidence, not a safe-to-run, production-ready installation recipe. No credentials, tenant secrets, or registration artifacts are included.
