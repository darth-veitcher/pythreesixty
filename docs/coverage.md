# Coverage for documented API
https://bim360field.autodesk.com/apidoc

Last updated: 2015.06.14

## Resources

+ mobile_api
    + <s>POST /api/login</s>
    + <s>POST /api/logout</s>
    + <s>POST /api/projects</s>
    + POST /api/user_prefs
    + POST /api/project
    + POST /api/templates
    + POST /api/areas
    + POST /api/companies
    + POST /api/contacts
    + POST /api/spec_refs
    + POST /api/priorities
    + POST /api/checklist_status
    + POST /api/issue_types
    + POST /api/issue_filters
    + POST /api/vela_fields
    + POST /api/custom_fields
    + POST /api/get_voided_issues
    + <s>POST /api/get_issues</s>
    + POST /api/get_object_issues
    + POST /api/signatures
    + POST /api/attachments
    + POST /api/document_references
    + POST /api/binary_data
    + POST /api/get_checklists
    + POST /api/checklists
    + POST /api/get_checklist_headers
    + POST /api/get_current_date
    + POST /api/get_categories
    + POST /api/get_equipment
    + POST /api/customizable_categories
    + POST /api/equipment
    + POST /api/get_tasks
    + POST /api/get_task_templates
    + POST /api/tasks
+ library_api
    + POST /api/library/publish
    + POST /api/library/all_files
    + POST /api/library/all_folders
    + POST /api/library/delete_files
    + POST /api/library/delete/:id/:rev
    + POST /api/library/folder/add
    + POST /api/library/folder/delete
    + POST /api/library/folder/move
    + GET /api/library/folders
    + POST /api/library/file/:id/:type/:rev/:page
    + POST /api/library/rename/:id
    + POST /api/library/move/:id
+ project_export_api
    + GET api/latest_project_export/:project_id
    + GET api/project_export_status/:project_id
+ admin_api
    + POST /fieldapi/admin/v1/ping
    + POST /fieldapi/admin/v1/project_names
    + POST /fieldapi/admin/v1/locations
    + POST /fieldapi/admin/v1/companies
    + POST /fieldapi/admin/v1/users
    + POST /fieldapi/admin/v1/custom_field_create
    + POST /fieldapi/admin/v1/custom_field_destroy
    + POST /fieldapi/admin/v1/filters
+ issues_api
    + GET /fieldapi/issues/v1
    + POST /fieldapi/issues/v1/types
    + POST /fieldapi/issues/v1/create_type
    + POST /fieldapi/issues/v1/destroy_type
    + POST /fieldapi/issues/v1/enable_standard_field
    + POST /fieldapi/issues/v1/disable_standard_field
    + POST /fieldapi/issues/v1/fields
    + POST /fieldapi/issues/v1/root_causes
    + POST /fieldapi/issues/v1/retrieve
    + POST /fieldapi/issues/v1/list
    + POST /fieldapi/issues/v1/create
    + POST /fieldapi/issues/v1/update
    + POST /fieldapi/issues/v1/search
    + POST /fieldapi/issues/v1/destroy
    + POST /fieldapi/issues/v1/comment
+ fieldapi/checklists/v1/checklists_api
    + GET /fieldapi/checklists/v1
    + GET /fieldapi/checklists/v1/:id
+ fieldapi/companies/v1/companies_api
    + GET /fieldapi/companies/v1
    + GET /fieldapi/companies/v1/:id
    + POST /fieldapi/companies/v1
    + PUT /fieldapi/companies/v1/:id
    + DELETE /fieldapi/companies/v1/:id
    + POST /fieldapi/companies/v1/add_to_projects
    + POST /fieldapi/companies/v1/remove_from_projects
+ api/v1/admin/account_users
    + /admin/v1/accounts/:account_id/users/change_status
