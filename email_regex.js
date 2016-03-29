// Email regex

// input: "Please contact support@example.org for help." ->
// output: "Please contact <a href=\"mailto:support@example.org\">support@example.org</a> for help."

function linkEmailAddresses(text) {
    return text.replace(/\w+\@(\w+\.)+\w+/g, "<a href=\"mailto:$&\">$&</a>") // $& = "the whole match"

    return text.replace(/\w+\@(\w+\.)+\w+/g, function (wholematch) {
        return "<a href=\"mailto:" + wholematch + "\">" + wholematch + "</a>";
    });
}


console.log(linkEmailAddresses("Write me at ben@stackoverflow.com if you need help, or at my personal email mail@benjamindumke.de."))
