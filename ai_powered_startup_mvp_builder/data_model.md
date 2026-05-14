# Data Model

## Project Entity
- project_id (Primary Key, UUID): Unique identification string.
- title (String, Required): System title for the project scope.
- created_at (Timestamp): Auto-generated system tracking reference.

## Entity Schema
- schema_id (Primary Key, UUID): Unique definition record identification.
- project_id (Foreign Key): Relates component directly back to a Project instance.
- name (String, Required): Operational database target lookup identifier.

## GeneratedComponent Entity
- component_id (Primary Key, UUID): Structural instance identifier.
- schema_id (Foreign Key): Connects programmatic entity straight to corresponding Schema maps.
- source_code (Text): Generated technical solution assets.
