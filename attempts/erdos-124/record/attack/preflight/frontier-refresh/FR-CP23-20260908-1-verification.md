# Frontier refresh verification

Date: 2026-09-08. Assessment: FR-CP23-20260908-1.

The public replan command succeeded at revision319. Fresh public status confirms root route12 and internal route13 selected, node14 deferred, all17 node lifecycle statuses retained, all10 acceptances accepted,23 checkpoints, the root open, and account1 still24 used moves with zero reservations and zero runs. The next action is replan, not execution of an older node. Acceptance10's unique progress identity was consumed for the replan; no account was renewed.

The authored policy and assessment were read back completely. These changes establish a current planning decision and a persistent operating rule, not an automatic post-checkpoint scheduler gate. No plugin source was edited. No mathematical result was generated.

An attempted in-memory canonical comparison failed because the helper was bound under the wrong local variable name. It performed no external mutation. No complete before-and-after byte comparison is claimed. The verification above uses the actual public baseline fields, successful replan response, fresh lifecycle/account/acceptance fields, and the inspected replan semantics.

```json
{
  "revision": 319,
  "selected": {
    "obligation-000001": "route-000012",
    "obligation-000002": "route-000003",
    "obligation-000035": "route-000013"
  },
  "deferred": [
    "node-000014"
  ],
  "round": 0,
  "account": {
    "historical_moves": 0,
    "historical_runs": 0,
    "historical_usage": "known",
    "id": "account-000001",
    "lineage_owner": "account-000001",
    "max_moves": 24,
    "max_runs": 24,
    "owner_claim_digest": "e2643caa3c2cab038a81cedfe16932ae0f90c248649774e3de82ff5f6278b9fe",
    "owner_obligation": "obligation-000001",
    "predecessor_account_id": null,
    "renewal_basis": null,
    "renewal_basis_digest": null,
    "reserved_moves": 0,
    "reserved_runs": 0,
    "schema_version": 1,
    "used_moves": 24,
    "used_runs": 0
  },
  "nodes": [
    {
      "id": "node-000001",
      "status": "retreated"
    },
    {
      "id": "node-000002",
      "status": "retreated"
    },
    {
      "id": "node-000003",
      "status": "retreated"
    },
    {
      "id": "node-000004",
      "status": "finished"
    },
    {
      "id": "node-000005",
      "status": "finished"
    },
    {
      "id": "node-000006",
      "status": "finished"
    },
    {
      "id": "node-000007",
      "status": "retreated"
    },
    {
      "id": "node-000008",
      "status": "retreated"
    },
    {
      "id": "node-000009",
      "status": "finished"
    },
    {
      "id": "node-000010",
      "status": "finished"
    },
    {
      "id": "node-000011",
      "status": "finished"
    },
    {
      "id": "node-000012",
      "status": "finished"
    },
    {
      "id": "node-000013",
      "status": "finished"
    },
    {
      "id": "node-000014",
      "status": "admitted"
    },
    {
      "id": "node-000015",
      "status": "retreated"
    },
    {
      "id": "node-000016",
      "status": "finished"
    },
    {
      "id": "node-000017",
      "status": "retreated"
    }
  ],
  "checkpoints": 23,
  "acceptances": [
    {
      "id": "acceptance-000001",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000008"
    },
    {
      "id": "acceptance-000002",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000009"
    },
    {
      "id": "acceptance-000003",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000010"
    },
    {
      "id": "acceptance-000004",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000015"
    },
    {
      "id": "acceptance-000005",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000016"
    },
    {
      "id": "acceptance-000006",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000017"
    },
    {
      "id": "acceptance-000007",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000018"
    },
    {
      "id": "acceptance-000008",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000019"
    },
    {
      "id": "acceptance-000009",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000022"
    },
    {
      "id": "acceptance-000010",
      "status": "accepted",
      "checkpoint_id": "checkpoint-000023"
    }
  ],
  "proof": "open",
  "newProgressKey": true
}
```
