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

  await page.goto('https://walmart.com');
  await page.screenshot({path: 'example.png'});

  await browser.close();
})();