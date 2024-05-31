const SHEETID = '1L3fWSSiYQZ2vNS6fusMWPRNF3KwRW-moFkHZY7PPJ8c';
const DOCID = '1nX10-KlbQleR66bMoN2lm6BB34enw06L-D3v6iu7BxA';
const FOLDERID = '1XwHhH39czoxIod966omw8MD0O7U3UKL7';

function onOpen(){
    SpreadsheetApp.getUi()
    .createMenu('PDF')
    .addItem('Generate PDF', 'generate_pdf')
    .addToUi();
}

function generate_pdf() {
  try {
    const sheet = SpreadsheetApp.openById(SHEETID).getSheetByName('data');
    if (!sheet) {
      Logger.log("Sheet 'data' not found");
      return;
    }

    const data = sheet.getDataRange().getValues();
    if (data.length === 0) {
      Logger.log("No data found in the sheet");
      return;
    }

    const temp = DriveApp.getFileById(DOCID);
    const folder = DriveApp.getFolderById(FOLDERID);

    const rows = data.slice(1); // Skip header row
    Logger.log(rows);

    rows.forEach((row, index) => {
      const file = temp.makeCopy(folder);
      const doc = DocumentApp.openById(file.getId());
      const body = doc.getBody();

      data[0].forEach((heading, i) => {
        if (typeof heading === 'string') {
          const header1 = heading.toUpperCase();
          body.replaceText(`{${header1}}`, row[i]);
        } else {
          Logger.log("Element at index " + i + " in header row is not a string");
        }
      });

      doc.setName(row[0] + "_" + row[1]);
      doc.saveAndClose();
      
      const blob = file.getAs('application/pdf');
      const pdf = folder.createFile(blob).setName(row[3] + "-" + row[11] +"_"+row[4]+"-"+row[10] +'.pdf');

      file.setTrashed(true);
    });

  } catch (e) {
    Logger.log("Error in generate_pdf: " + e.toString());
  }
}
