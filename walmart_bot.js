var casper = require('casper').create();

// login
casper.start('https://www.walmart.com/account/login')

casper.waitForSelector('form#sign-in-form', function() {
    this.fillXPath('form#sign-in-form', {
        '//*[@id="email"]': 'longu97@bu.edu',
        '//*[@id="password"]': 'Deptraiqua123'
    }, true);
});

casper.then(function() {
    this.click('#sign-in-form > button.button.m-margin-top.text-inherit');
});

casper.then(function() {
    casper.waitForSelector(
        '//*[@id="main-content"]/span/div[1]/div/nav/div[2]/div[2]/a',
        function() {
            this.capture('screenshots/after-login.png');
        },
        function() {
            this.capture('screenshots/after-login.png');
            casper.exit();
        }
        );
});


// casper.then(function() {
//     this.waitForSelector('#sign-in-form > button.button.m-margin-top.text-inherit', function() {
//         this.click('#sign-in-form > button.button.m-margin-top.text-inherit', function() {
//             this.wait(5, function() {
//                 this.open('https://www.walmart.com/cart', function() {
//                     this.capture('screenshots/after-login.png');
//                 });
//             });
//         });
//     });
// });

// casper.then(function() {
//     casper.waitForSelector("//*[@id='sign-in-form']/button[1]", function() {
//         this.click("//*[@id='sign-in-form']/button[1]");
//     });
// });

// wait couple seconds to login
// casper.then(function() {
//     casper.wait(5, function() {
//         casper.open('https://www.walmart.com/cart', function() {
//             casper.capture('screenshots/after-login.png');
//         });
//     });
// });

casper.run();