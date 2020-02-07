INSERT_INTO_REPORTS = """
    INSERT INTO reports(
        doc_id,
        source,
        source_identity_id,
        state,
        created,
        reference_id,
        reference_type,
        report_type,
        report_id,
        reference_resource_id,
        reference_resource_type,
        message
    ) VALUES(
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
"""

GET_UNRESOVLED_ENTRIES = "SELECT * FROM reports WHERE state <> 'RESOLVED' ORDER BY created DESC"

SET_ENTRY_TO_BLOCKED = "UPDATE reports SET state = 'BLOCKED' WHERE id = ?"

SET_ENTRY_TO_RESOLVED = "UPDATE reports SET state = 'RESOLVED' WHERE id = ?"

GET_ENTRY_BY_ID = "SELECT * FROM reports WHERE id = ?"