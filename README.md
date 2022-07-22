# Portfolio-site

# Notes during development
* didn't install cloudinary as contemplating using aws s3 bucket. if Cloudinary added come back to step 2.4 Get our static and media files stored on Cloudinary: in deployment pdf

# currently working on

write content for homepage, remove blog for now and make contact page
they deploy with s3 bucket as mvp
work on pricing and stripe next


# need to work on
check about emails
change about section, link CV
deploy with aws
allauth template pages - add widget tweaks for forms
Pricing,
Members area - upload files, download files
profile
contact page
Email confirmation and verification_sent templates, align text in container still

# draft for client_account models

ProjectDetails model:
user - one to many
project_name
Project_ID
project_due_date

Costings model:
project_ID UUID
Planning_design_quote
development_quotation
deployment_quotation
hosting_agreement_inplace
hosting_quotation
maintenance_agreement_in_place - boolean
maintenance_fee
additional_expenses
current_cost
paid_to_date
remaining balance
Max budget

ProjectFiles Model:
poject_ID
Initial_contract
wireframes
color_mockup null = true
planning_doc - null = true
official_doc - null = true
repo_location

ProjectNotes model:
related_project FK