const pd = require('paralleldots');
pd.apiKey = "uEXXr5XMcE2Ee5xo3aPeWPr9DhkIaTvCoPmTS7wN70s";

defVal="i am happy";
pd.sentiment(defVal,'en')
.then((response) => {
    var json = JSON.parse(response);
    if (json.sentiment.negative > json.sentiment.neutral && json.sentiment.negative > json.sentiment.positive){
        console.log("negative")
    }
    else console.log("I do not understand can you repeat that");
}).catch((error) =>{
    console.log(error);
});
