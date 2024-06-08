var crypto = require('crypto');

var hash = crypto.createHash('sha256');

var code = 'e0935c4718524d1f9629d3869476496b';

code = hash.update(code);
code = hash.digest('hex');

console.log(code);