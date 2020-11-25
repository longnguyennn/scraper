const fs = require('fs');

const puppeteer = require('puppeteer');

(async () => {
  const args = [
    '--no-sandbox',
    '--disable-setuid-sandbox',
    '--disable-infobars',
    '--window-position=0,0',
    '--ignore-certifcate-errors',
    '--ignore-certifcate-errors-spki-list',
    '--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36"'
  ];

  const options = {
    args,
    headless: true,
    ignoreHTTPSErrors: true,
    userDataDir: './tmp'
  };

  const browser = await puppeteer.launch(options);

  const page = await browser.newPage();
  const preloadFile = fs.readFileSync('./preload.js', 'utf8');
  await page.evaluateOnNewDocument(preloadFile);

  await page.goto('https://www.walmart.com/account/login');

  await page.type('#email', 'longu97@bu.edu');
  await page.type('#password', 'Deptraiqua123');

  const login_button = await page.$x('//*[@id="sign-in-form"]/button[1]');
  await login_button[0].click();
  try {
    await page.waitForNavigation();
  } catch (err) {
    await page.screenshot({ path: 'example.png' });
  }

  await page.screenshot({ path: 'example.png' });

  await browser.close();
})();