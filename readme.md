# Endpoints
[GET] http://localhost:8069/material_registration/materials

[GET] http://localhost:8069/material_registration/material/1

[POST] http://localhost:8069/material_registration/material

[PUT] http://localhost:8069/material_registration/material/2

[DEL] http://localhost:8069/material_registration/material/1


# Request and Response Examples
## GET Data
```curl
curl --location 'http://localhost:8069/material_registration/materials' \
--header 'Authorization: 5c5a50d2-a7b6-4a95-8492-8b06139e3e7f' \
--header 'Cookie: session_id=a2bf0d2a943a853e7ab40d9b6d07e831b9e7b7cd'
```

```json
[
    {
        "id": 1,
        "material_code": "M001",
        "material_name": "Fabric Sample",
        "material_type": "fabric",
        "material_buy_price": 120.0,
        "related_supplier": "YourCompany"
    },
    {
        "id": 2,
        "material_code": "M002",
        "material_name": "Jeans Sample",
        "material_type": "jeans",
        "material_buy_price": 150.0,
        "related_supplier": "YourCompany"
    },
    {
        "id": 3,
        "material_code": "M003",
        "material_name": "Cotton Sample",
        "material_type": "cotton",
        "material_buy_price": 100.0,
        "related_supplier": "YourCompany"
    }
]
```

```curl
curl --location 'http://localhost:8069/material_registration/material/1' \
--header 'Authorization: 5c5a50d2-a7b6-4a95-8492-8b06139e3e7f' \
--header 'Cookie: session_id=a2bf0d2a943a853e7ab40d9b6d07e831b9e7b7cd'
```

```json
[
    {
        "id": 1,
        "material_code": "M001",
        "material_name": "Fabric Sample",
        "material_type": "fabric",
        "material_buy_price": 120.0,
        "related_supplier": [
            1,
            "YourCompany"
        ],
        "display_name": "material_registration.material,1",
        "create_uid": [
            1,
            "System"
        ],
        "create_date": "2024-02-19 12:27:09",
        "write_uid": [
            1,
            "System"
        ],
        "write_date": "2024-02-19 12:27:09"
    }
]
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

```json
[
    {
        "id": 11,
        "material_code": "wkwkw",
        "material_name": "wkwkwk",
        "material_type": "cotton",
        "material_buy_price": 200.0,
        "related_supplier": [
            1,
            "YourCompany"
        ],
        "display_name": "material_registration.material,11",
        "create_uid": [
            2,
            "Mitchell Admin"
        ],
        "create_date": "2024-02-20 04:02:35",
        "write_uid": [
            2,
            "Mitchell Admin"
        ],
        "write_date": "2024-02-20 04:02:35"
    }
]
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

```json
[
    {
        "id": 2,
        "material_code": "wkwkw",
        "material_name": "wkwkwk",
        "material_type": "cotton",
        "material_buy_price": 200.0,
        "related_supplier": [
            1,
            "YourCompany"
        ],
        "display_name": "material_registration.material,2",
        "create_uid": [
            1,
            "System"
        ],
        "create_date": "2024-02-19 12:27:09",
        "write_uid": [
            2,
            "Mitchell Admin"
        ],
        "write_date": "2024-02-20 04:12:23"
    }
]
```

## Delete Data
```curl
curl --location --request DELETE 'http://localhost:8069/material_registration/material/1' \
--header 'Authorization: 5c5a50d2-a7b6-4a95-8492-8b06139e3e7f' \
--header 'Cookie: session_id=a2bf0d2a943a853e7ab40d9b6d07e831b9e7b7cd'
```

```json

{
    "id": 1,
    "status": "success",
    "message": "Material with id #1 has been deleted."
}
```

## Negative cases response
### 401 UNAUTHORIZED
```json
Unauthorized: Invalid or missing authentication token Invalid authentication token
```

# Running test
"E:\_Installed Apps\python\python.exe" "E:\_Installed Apps\server\odoo-bin" -d admin -i material_registration --test-enable