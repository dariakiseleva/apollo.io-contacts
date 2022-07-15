const axios = require("axios")
require('dotenv').config({path:__dirname+'/./../.env'})

const req_data = {
    "api_key": process.env.APOLLO_API_KEY,
    "details": [
        {
            "first_name": "Marcel",
            "last_name": "Moeller",
            "organization_name": "Dow"
        },
        {
            "first_name": "Lars",
            "last_name": "Domogalla",
            "organization_name": "Dow Olefinverbund GmbH"
        },
        {
            "first_name": "Lars",
            "last_name": "Domogalla",
            "organization_name": "Dow"
        }
    ]
}

axios
.post("https://api.apollo.io/api/v1/people/bulk_match", req_data)
.then(res => console.log(res.data.matches))