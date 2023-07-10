
# ZB- Upload Photos

Python tool to create a csv with the correct match between profiles photos and surgeon accounts. This script needs two csv (Surgeons data and Content version data) to continue with the process to create the match and create a new csv to upload in Salesforce.


## Installation
Install [Python](https://www.python.org/downloads/).

Install requirements.txt by pip:

```bash
pip install -r requirements.txt
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/Marcko10Rayman/ZB_Match_Surgeons.git
```

Go to the project directory

```bash
  cd ZB_Match_Surgeons
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the script

```bash
  python -u "**path_of_location**\main.py"
```


## Deployment

To deploy this project run

In the terminal, show the instrucctions:

- The script open a window to choose the Account Query CSV. (**Note: Verify the correct name of the headers**) 
`You can find an example in the example folder.`

| Headers | Description |
| ------ | ------ |
| Id | Id surgeon account to upload the document with the ContentVersionId associated |
| Name | Surgeon Name |
| NPI__c | NPI number of surgeon to create the match with their correct photo |
| btydev__Picture_Id__pc | Id of the correct photo in Salesforce |

- The script open a window to choose the Content Version Insert Result CSV. (**Note: Verify the correct name of the headers**) 
`You can find an example in the example folder.`

| Headers | Description |
| ------ | ------ |
| ID | Id of the photo exists in Salesforce (ContentVersionId) |
| TITLE | Photo Name |
| DESCRIPTION | Description of the photo (Optional) |
| VERSIONDATA | Local path from the photo |
| PATHONCIENT | Local path from the photo |
| FIRSTPUBLISHLOCATIONID | If the photo is the first time publish (Optional) |
| STATUS | Description of the process if it is insert correct or have errors in the process.|

`Python has case sensitive with the words, that is the reason to verify the headers`

- The process run and match automatically the records.
- Finally, the result save in the folder **Data** with the name `Accounts`



## Used By

This project is used by the following company:

- [Zimmer Biomet](https://www.zimmerbiomet.com/en)
- [Concentrix Catalyst](https://www.concentrix.com/catalyst/)


## Authors

- Marco Antonio Cruz Barboza

