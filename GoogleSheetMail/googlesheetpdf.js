function onOpen() {
    const ui = SpreadsheetApp.getUi();
    ui.createMenu('Custom Menu')
      .addItem('Generate and Download PDFs', 'generatePDFs')
      .addToUi();
  }
  
  function generatePDFs() {
    try {
      var ss = SpreadsheetApp.getActiveSpreadsheet();
      var ws = ss.getSheetByName("Customer");
      var wsSettings = ss.getSheetByName("Settings");
  
      if (!ws) {
        Logger.log("Sheet 'Customer' not found");
        return;
      }
      if (!wsSettings) {
        Logger.log("Sheet 'Settings' not found");
        return;
      }
  
      var data = ws.getRange("A2:X" + ws.getLastRow()).getValues(); // Adjust range according to your columns
      Logger.log("Data retrieved: " + JSON.stringify(data));
  
      var pdfUrls = [];
  
      var folderName = "Customer PDFs";
      var folders = DriveApp.getFoldersByName(folderName);
      var folder;
  
      if (folders.hasNext()) {
        folder = folders.next();
        Logger.log("Existing folder found: " + folderName);
      } else {
        folder = DriveApp.createFolder(folderName);
        Logger.log("New folder created: " + folderName);
      }
  
      data.forEach(function(row, index) {
        if (row[22] === "" && row[23] === "Send") { // Adjust indices to match `emailstatus` and `sendstatus` columns
          var pdfTemp = HtmlService.createTemplateFromFile("pdfTemplate");
          pdfTemp.serial_no = row[0];
          pdfTemp.month = row[1];
          pdfTemp.invoice_Date = row[2];
          pdfTemp.invoice_No = row[3];
          pdfTemp.client_name = row[4];
          pdfTemp.client_gstin = row[5];
          pdfTemp.sac_hsn = row[6];
          pdfTemp.invoice_detail = row[7];
          pdfTemp.type = row[8];
          pdfTemp.invoive_value_excluding_taxes = row[9];
          pdfTemp.advance = row[10];
          pdfTemp.balance = row[11];
          pdfTemp.billed_amount = row[12];
          pdfTemp.sgst = row[13];
          pdfTemp.cgst = row[14];
          pdfTemp.igst = row[15];
          pdfTemp.total_tax = row[16];
          pdfTemp.total_amount = row[17];
          pdfTemp.tsd_deduction = row[18];
          pdfTemp.net_Earning_Excluding_GST = row[19];
          pdfTemp.net_credit_including_gst = row[20];
          pdfTemp.remarks = row[21];
          pdfTemp.invoice_status = row[22];
  
          var htmlContent = pdfTemp.evaluate().getContent();
          Logger.log("HTML content generated for " + row[3]); // Logging invoice number
  
          var blob = Utilities.newBlob(htmlContent, 'text/html').getAs('application/pdf');
          blob.setName(row[3] + ".pdf"); // Using invoice number as PDF name
  
          try {
            var file = folder.createFile(blob);
            pdfUrls.push(file.getUrl());
            Logger.log("PDF created and saved: " + file.getUrl());
  
            var currentDate = new Date();
            ws.getRange(index + 2, 23).setValue(currentDate); // Adjust index for email status column
            ws.getRange(index + 2, 23).setBackground("green"); // Adjust index for email status column
          } catch (e) {
            Logger.log("Error creating file: " + e.toString());
          }
        }
      });
  
      if (pdfUrls.length > 0) {
        showDownloadDialog(pdfUrls);
      } else {
        Logger.log("No PDFs were prepared for download.");
      }
    } catch (e) {
      Logger.log("Error in generatePDFs: " + e.toString());
    }
  }
  
  function showDownloadDialog(pdfUrls) {
    var template = HtmlService.createTemplateFromFile('DownloadDialog');
    template.pdfUrls = pdfUrls;
    var htmlOutput = template.evaluate()
      .setWidth(400)
      .setHeight(300);
    SpreadsheetApp.getUi().showModalDialog(htmlOutput, 'Download PDFs');
  }
  
  function include(filename) {
    return HtmlService.createHtmlOutputFromFile(filename).getContent();
  }
  