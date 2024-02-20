# Endpoints
[GET] http://localhost:8069/material_registration/materials

[GET] http://localhost:8069/material_registration/material/1

[POST] http://localhost:8069/material_registration/material

[PUT] http://localhost:8069/material_registration/material/2

[DEL] http://localhost:8069/material_registration/material/1


# Request Examples
## GET Data
```curl
curl --location 'http://localhost:8069/material_registration/materials' \
--header 'Authorization: 5c5a50d2-a7b6-4a95-8492-8b06139e3e7f' \
--header 'Cookie: session_id=a2bf0d2a943a853e7ab40d9b6d07e831b9e7b7cd'
```

```curl
curl --location 'http://localhost:8069/material_registration/material/1' \
--header 'Authorization: 5c5a50d2-a7b6-4a95-8492-8b06139e3e7f' \
--header 'Cookie: session_id=a2bf0d2a943a853e7ab40d9b6d07e831b9e7b7cd'
```

## POST Data
```curl
curl --location 'http://localhost:8069/material_registration/material' \
--header 'Authorization: 5c5a50d2-a7b6-4a95-8492-8b06139e3e7f' \
--header 'Content-Type: application/json' \
--header 'Cookie: session_id=a2bf0d2a943a853e7ab40d9b6d07e831b9e7b7cd' \
--data '{
    "material_code": "wkwkw",
    "material_name": "wkwkwk",
    "material_type": "cotton",
    "material_buy_price": 200,
    "supplier_id": 1
}'
```


## Update Data
```curl
curl --location --request PUT 'http://localhost:8069/material_registration/material/2' \
--header 'Authorization: 5c5a50d2-a7b6-4a95-8492-8b06139e3e7f' \
--header 'Content-Type: application/json' \
--header 'Cookie: session_id=a2bf0d2a943a853e7ab40d9b6d07e831b9e7b7cd' \
--data '{
    "material_code": "wkwkw",
    "material_name": "wkwkwk",
    "material_type": "cotton",
    "material_buy_price": 200,
    "supplier_id": 1
}'
```

## Delete Data
```curl
curl --location --request DELETE 'http://localhost:8069/material_registration/material/1' \
--header 'Authorization: 5c5a50d2-a7b6-4a95-8492-8b06139e3e7f' \
--header 'Cookie: session_id=a2bf0d2a943a853e7ab40d9b6d07e831b9e7b7cd'
```
