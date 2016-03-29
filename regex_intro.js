var s = "strangeley the japanese sun is shining in the sky today";
var words_with_s = /\bs(\w*)()/g;


var result = s.replace(words_with_s, function (wholematch, group1, group2) {
    return "s" +  group1.toUpperCase();
});

//console.log(result);


s = "It has been 12.471 seconds since...";
s.replace(/(\d+)\.(\d+)/g, function (wholematch, wholepart, fractionalpart) {
    console.log(wholepart + " before the period and " + fractionalpart + " after it");
});

var host = "www.google.com";
console.log(/^(\w+\.)?google\.com$/.test(host))

//console.log(s.match(words_with_s))

// \w is equivalent to [a-zA-Z0-9_] -- in JavaScript, at least
