function onOpen() {
    const ui = SpreadsheetApp.getUi();
    ui.createMenu('EasyMails')
        .addItem('Send Emails', 'sendMail')
        .addToUi();
  }
  
  function sendMail() {
    var first = 0;
    var last  = 1;
    var email = 2;
    var phone = 3;  
    var emailstatus = 7;
    var sendstatus = 8
    const EMAIL_SENT_COL = "Email Status";
  
    var emailTemp = HtmlService.createTemplateFromFile("email");
  
    var ws = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Customer");
    var wsSettings = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Settings");
  
    var name = wsSettings.getRange("B2").getValue();
    var subject = wsSettings.getRange("B1").getValue();
  
    var data = ws.getRange("A2:I" + ws.getLastRow()).getValues();
  
    // data = data.filter(function(r){return r[9] == true});
  
    data.forEach(function(row,index){
      if (row[emailstatus] === "" && row[sendstatus] ==="Send"){
        emailTemp.fn = row[first];
        emailTemp.ln = row[last];
        emailTemp.phone = row[phone];
        var htmlMessage = emailTemp.evaluate().getContent();
        GmailApp.sendEmail(
          row[email], 
          subject, 
          "Your email doesn't support HTML.",
          {name:name, htmlBody: htmlMessage}
        );
  
        var currentDate = new Date();
        ws.getRange(index + 2, emailstatus +1).setValue(currentDate);
        ws.getRange(index + 2, emailstatus +1).setBackground("green");
      }
    });
  }