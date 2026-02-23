// GOOGLE APPS SCRIPT BACKEND FOR "FIX THE GLITCH" EVENT
// 
// INSTRUCTIONS:
// 1. Go to Google Drive and create a new Google Sheet.
// 2. Rename 'Sheet1' to 'Scores' (without quotes).
// 3. In the 'Scores' sheet, set row 1 as headers: S No, Name, College, Dept, Mail, Phone, Result.
// 4. Click the "+" button to add a new sheet, and name it 'Questions'.
// 5. In the 'Questions' sheet, set row 1 as headers: Question, Option 0, Option 1, Option 2, Option 3, Answer Index.
// 6. Go to Extensions > Apps Script in the Google Sheet menu.
// 7. Erase any existing code and PASTE this entire script.
// 8. Click 'Deploy' (top right button) > 'New Deployment'.
// 9. Click the gear icon next to 'Select type' and choose 'Web app'.
// 10. Under 'Execute as', select 'Me'.
// 11. Under 'Who has access', select 'Anyone'.
// 12. Click 'Deploy' -> 'Authorize access' -> Advanced -> Go to script.
// 13. Copy the 'Web app URL' provided.
// 14. Finally, PASTE that URL into your `index.html` and `admin.html` where it says `const SCRIPT_URL = 'YOUR_APPS_SCRIPT_URL_HERE';`

const SCORES_SHEET = "Scores";
const QUESTIONS_SHEET = "Questions";

// Handles reading data (Fetching questions and pulling scores)
function doGet(e) {
  const action = e.parameter.action;

  if (action === 'getQuestions') {
    return handleGetQuestions();
  } else if (action === 'getScores') {
    return handleGetScores();
  }

  return ContentService.createTextOutput(JSON.stringify({ "status": "error", "message": "Invalid GET action" }))
    .setMimeType(ContentService.MimeType.JSON);
}

function getSheetSafely(sheetName, fallbackIndex) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(sheetName);
  if (!sheet) {
    // If exact name not found, try falling back to the 1st or 2nd tab
    sheet = ss.getSheets()[fallbackIndex];

    // If even that doesn't exist, create it
    if (!sheet) {
      sheet = ss.insertSheet(sheetName);
    }
  }
  return sheet;
}

// Handles writings data (Submitting scores and creating new questions)
function doPost(e) {
  const action = e.parameter.action;

  if (action === 'submitScore') {
    const sheet = getSheetSafely(SCORES_SHEET, 0); // fallback to the first tab (index 0)
    const sno = Math.max(1, sheet.getLastRow());
    const name = e.parameter.name;
    const college = e.parameter.college;
    const dept = e.parameter.dept;
    const mail = e.parameter.mail;
    const phone = e.parameter.phone;
    const result = e.parameter.score + " / " + e.parameter.total;

    sheet.appendRow([sno, name, college, dept, mail, phone, result]);

    return ContentService.createTextOutput(JSON.stringify({ "status": "success" }))
      .setMimeType(ContentService.MimeType.JSON)
      .setHeader('Access-Control-Allow-Origin', '*');
  }
  else if (action === 'addQuestion') {
    const sheet = getSheetSafely(QUESTIONS_SHEET, 1); // fallback to the second tab (index 1)
    const q = e.parameter.q;
    const opt0 = e.parameter.opt0;
    const opt1 = e.parameter.opt1;
    const opt2 = e.parameter.opt2;
    const opt3 = e.parameter.opt3;
    const ans = e.parameter.ans;

    sheet.appendRow([q, opt0, opt1, opt2, opt3, ans]);

    return ContentService.createTextOutput(JSON.stringify({ "status": "success" }))
      .setMimeType(ContentService.MimeType.JSON)
      .setHeader('Access-Control-Allow-Origin', '*');
  }
}

// Helper: Fetch Questions
function handleGetQuestions() {
  const sheet = getSheetSafely(QUESTIONS_SHEET, 1);
  const data = sheet.getDataRange().getValues();

  // Skip header row
  const questions = [];
  for (let i = 1; i < data.length; i++) {
    questions.push({
      q: data[i][0],
      opts: [data[i][1], data[i][2], data[i][3], data[i][4]],
      ans: data[i][5]
    });
  }

  return ContentService.createTextOutput(JSON.stringify({ questions: questions }))
    .setMimeType(ContentService.MimeType.JSON);
}

// Helper: Fetch Scores
function handleGetScores() {
  const sheet = getSheetSafely(SCORES_SHEET, 0);
  const data = sheet.getDataRange().getValues();

  const scores = [];
  for (let i = 1; i < data.length; i++) {
    scores.push({
      sno: data[i][0],
      name: data[i][1],
      college: data[i][2],
      dept: data[i][3],
      mail: data[i][4],
      phone: data[i][5],
      result: data[i][6]
    });
  }

  return ContentService.createTextOutput(JSON.stringify({ scores: scores }))
    .setMimeType(ContentService.MimeType.JSON);
}
