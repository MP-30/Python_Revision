function onOpen() {
    const ui = SpreadsheetApp.getUi();
    ui.createMenu('Easymail')
        .addItem('Send Emails', 'sendMail')
        .addToUi();
  }
  
  function sendMail() {
    const ws = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Customer");
    const wsSettings = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Settings");
    // var emailTemp = HtmlService.createTemplateFromFile("email");
    const emailBodyDocId = "1w86zmJxQ62BmQ3vjFhncAJkIffMwm5JgpX8pAhvh21A";
    const name = wsSettings.getRange("B2").getValue();
    const subject = wsSettings.getRange("B1").getValue();
    const data = ws.getRange("A2:I" + ws.getLastRow()).getValues();
    const emailBodyDoc = DocumentApp.openById(emailBodyDocId);
  
    // data = data.filter(function(r){return r[9] == true});
  
    data.forEach(function(row,index){
  
      var first = row[0];
      var last  = row[1];
      var email = row[2];
      var phone = row[3];  
      var emailstatus = row[7];
      var sendstatus = row[8];
      var footer = row[5];
      var attachmentLink = row[6];
      const EMAIL_SENT_COL = "Email Status";
  
      if (row[emailstatus] === "" && row[sendstatus] ==="Send"){
        // try{
          const emailBody = emailBodyDoc.getBody().getText();
          // const emailTemp = HtmlService.createTemplate(emailBody);
  
          const htmlMessage = emailBody
            .replace("{{FirstName}}", first)
            .replace("{{LastName}}", last)
            .replace("{{phoneNumber}}", phone)
            .replace("{{attachment(link)}}", attachmentLink)
            .replace("{{footer}}", footer);
  
          GmailApp.sendEmail(
            email, 
            subject, 
            "Your email doesn't support HTML.",
            {name:name, htmlBody: htmlMessage}
          );
  
          const currentDate = new Date();
          ws.getRange(index + 2, emailstatus +1).setValue(currentDate);
          ws.getRange(index + 2, emailstatus +1).setBackground("green");
        // }catch (error){
        //   console.error("Error sending email:", error);
        // }
      }
    });
  }