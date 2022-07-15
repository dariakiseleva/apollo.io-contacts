const axios = require("axios")


const req_data = {
    "api_key": "z2FzoyGx4LCYPSz9g5iscw",
    "details": [
        {
            "first_name": "Tim",
            "last_name": "Zheng",
            "domain": "apollo.io",
            "email": "tim@apollo.io",
            "organization_name": "Apollo"
        },
        {
            "first_name": "Roy",
            "last_name": "Chung",
            "email": "roy@apollo.io",
            "organization_name": "Apollo"
        }
    ]
}

axios
.post("https://api.apollo.io/api/v1/people/bulk_match", req_data)
.then(res => console.log(res.data.unique_enriched_records))