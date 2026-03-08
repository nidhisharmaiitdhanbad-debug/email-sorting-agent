# email-sorting-agent
A simple multi-agent email classifier built using Python.

## Agent Design

### Parser Agent
Reads the email subject and body and cleans the text.

### Classification Agent
Classifies the email into one of the following categories:
- Work
- Personal
- Spam
- Important

### Priority Agent
Assigns priority based on keywords.

High priority keywords:
- urgent
- meeting
- deadline

Low priority keywords:
- offer
- discount

Everything else → Medium priority.

### Agent Workflow

Input Email  
↓  
Parser Agent  
↓  
Classification Agent  
↓  
Priority Agent  
↓  
Final Result
