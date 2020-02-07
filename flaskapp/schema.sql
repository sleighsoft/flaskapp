DROP TABLE IF EXISTS reports;

-- id:                      36 characters, 4x dash                          UNIQUE
-- source:                  REPORT
-- source_identity_id:      36 characters, 4x dash
-- state:                   OPEN
-- created:                 TEXT YYYY-MM-DD'T'HH:mm:ss.SSS'Z'

-- reference_type:          REPORT
-- reference_id:            36 characters, 4x dash

-- report_type:             VIOLATES_POLICIES, SPAM, INFRINGES_PROPERTY
-- report_id:               36 characters, 4x dash                          NOT UNIQUE | report_id == reference_id
-- reference_resource_id:   36 characters, 4x dash                          NOT UNIQUE
-- reference_resource_type: REPLY, ARTICLE, POST
-- message:                 NULL or TEXT



CREATE TABLE reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id TEXT NOT NULL, -- id
    source TEXT NOT NULL,
    source_identity_id TEXT NOT NULL,
    state TEXT NOT NULL,
    created TEXT NOT NULL,

    reference_type TEXT NOT NULL,
    reference_id TEXT NOT NULL, -- might be omitted as identical to report_id (at least in provided dataset)

    report_type TEXT NOT NULL,
    report_id TEXT NOT NULL,
    reference_resource_id TEXT NOT NULL,
    reference_resource_type TEXT NOT NULL,
    message TEXT
);