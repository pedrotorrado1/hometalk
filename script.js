var apiKey = "YOUR_API_KEY";
var zillow = new Zillow(apiKey);

var houses = zillow.getHouses({
location: "San Francisco, CA"
});

console.log(houses);
