After using BitWarden in the VM, I was able to locate 4 AES keys in memory:

1. ca54885e e359be61 b86e0083 947d0caf f48aa3f9 49d5d30b 3ad84731 ddcfbe69
2. e6efbc2f 5e5d2b0a a044ae42 6b5624ca 7ad4ff78 77f26840 c5bf8c99 edc5a2e3
3. 49794240 9cd54caa 54e34d7a 9b882482 78d1b5b3 6ec1af33 54056cae 5391ae70
4. 07159ef3 a9cf4de8 72992e1f 071c3506 14c6e3d4 eac833e1 09376ade a377afbc

I also able to find the following JSON in memory that corresponds to the BitWarden action I called for
creating a new item:
```
{
  "installedVersion": "1.18.0",
  "appId": "1fcde865-173d-4c47-bdfc-d7580ca9aeee",
  "emailVerified": false,
  "sends_1265f860-5312-470d-9b04-aa91002199c6": {},
  "lastSync_1265f860-5312-470d-9b04-aa91002199c6": "1970-01-01T00:00:00.000Z",
  "sends_17c72ea0-f06c-40d8-b3fc-ad87000dd922": {},
  "lastSync_17c72ea0-f06c-40d8-b3fc-ad87000dd922": "1970-01-01T00:00:00.000Z",
  "accessToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IkJDMzZDMjE0REI0OEYyMzVCNzdEQTNGMTcyMEMxQTM1QTk2MkVBNDNSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InZEYkNGTnRJOGpXM2ZhUHhjZ3dhTmFsaTZrTSJ9.eyJuYmYiOjE2MjkyODYyMjEsImV4cCI6MTYyOTI4OTgyMSwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5iaXR3YXJkZW4uY29tIiwiY2xpZW50X2lkIjoiY2xpIiwic3ViIjoiYzc4MWZjNjktYzg3OC00ZDIwLWE4MzItYWQ4ODAwYmNlMjU3IiwiYXV0aF90aW1lIjoxNjI5Mjg2MjIxLCJpZHAiOiJiaXR3YXJkZW4iLCJwcmVtaXVtIjpmYWxzZSwiZW1haWwiOiJodW5lYXVqYUB1bWljaC5lZHUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInNzdGFtcCI6IlJQQ0FUUU1MRVIySUZISVRLU01JS1hFRU9HQVBGQlkyIiwibmFtZSI6Ikpha2UgSHVuZWF1IiwiZGV2aWNlIjoiMWZjZGU4NjUtMTczZC00YzQ3LWJkZmMtZDc1ODBjYTlhZWVlIiwianRpIjoiRjMxNkJBMzE1QjBFRTRGODEzNkVBM0YzMzhCRkUyNDUiLCJpYXQiOjE2MjkyODYyMjEsInNjb3BlIjpbImFwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJBcHBsaWNhdGlvbiJdfQ.ZftlIGJxA4qFrUhInNVwedF03NHqLzfYACkZI8l5MoVDQkxE643NyDwukx9SyXmZXwEErvQGCFj0p0yh2yZzgkCFytlLBqAyJkugmmaSiOX_mkXGea8QmAwnJ2jgyaE5REmgfVQiZw6NftgN0qF9lQzNgLbUmYJnTPyCrTCOADTIBbo6-cZ85OTjvKoZEIGlOyfcuA2ql2gGNJ-Jlj2PyZaXkVpDtRAHjFeKZcWMsVQkCrGnXSsB_2s-pGyZIiX_WkfM-wP8eIDOShWymUYrD8ikJmSa1bGbRyf8N1XLMwyFxF00cwLUm9hXnGQlN2vgkvbye74sdlnFxlo4ZVgCpTytJ23QFPOEjfXFFXCgtLOwGxpaDT11bW9lP_Lh_pol6ZN6f1Ef9BsC_-jMHC4NB4NoeQeu2HhgM00p2vM9Y5Xp7pVhPAsgNjU0bJ1vR8o6PplsvprBJeYR14fZNqtb7xguoumM9ek0o_AAJQVYCC7SJo0VfpP7mfnpi_o97IoC2U6qE3WRwtyzYR4xEp3TB4eyxHwAIOAXwlFue3VxkNPH4liegKrpThyO0lXPmGZGzjxDhQ2dTRSfXMUiyzjB6Qk21kZ5CSudXczoadsblGiSWeEA6Qf8utQj6RT5vD-8iT922sRSeAHq3_1dhI_kGtGLvpGxYskd3lbC4mXyXWE",
  "refreshToken": "DC5FD480AA366283E5A3B2991139F1271188F6FBE0C2E43C07BEE22C3EA5F4AB",
  "userEmail": "huneauja@umich.edu",
  "userId": "c781fc69-c878-4d20-a832-ad8800bce257",
  "kdf": 0,
  "kdfIterations": 100000,
  "keyHash": "gmV8nnSwL2/STxgvpLwUGKYDAy5KaflGtieHRliqmxA=",
  "encKey": "2.uKRQOtEUIzfB+0xGpwYN3A==|yxw5KQviVKq6onYOJedt3/6MuYHkxWapWQBL+DIsrZQHxU3BN5o7kih/9bzbB07aed4EFFQzROzXFogFMeIjFTigJqSWuQAFmG7jv9To63I=|3c1FnPa9B0lqzGEWMC8gEews8OG4FSKKQ/hTh4BRZm4=",
  "encPrivateKey": "2.8oJRGx1ti9G1BKEgihFq7g==|o5E3Uz6MESuQnXKqlsKpXm7uxmOtqyBVVJxygrCLfnyNmcJYSqCTbbAwyUUhxKvaPUJ+YjqkpqAIQtLOCOt0cxpIPlWWQit3GW2knpvCdnSQNxHGmkFx5YFwU4nSSvyrNfsrx2I5pzdlc1356p9GvBoXn5v2GeI7iy7xtNS/nbu2DXILIwzKo/WrZyYu8q9xkf1qRXnWn8tcsrS34zKAdcTWNzYlcJLW82gbTKayuNTASUqYIHUYQGoww8hPljxp6UbxyqgUokU32Zi1dqRQcYMjtr+vEHuQARpyjHudQh71Ups06nBsWo5RSzTM9xV+flaHJOrnizE3gwCFUO0TQDmRPWD521AMPl650JdT4spuea3uuJWkrrl4LSVXcEDheObe/CkFJb27uwz09Z3cfGgvcimiwkHxCmQfGNxnRd37N8de67hHIOzYhZ6l7rgbyMtlg/rbFopm23dqseBcmYxGdGS/JzJ87s6tnX2ofvFj3M/X6wc31SXeLB3Dn70LWRYJFacQ8f+xQr5xg1sGw3AbdqDfhyVtwWbtUGL1rAm54NIm69Wz7EOhmAbvhdgA1aaJ8u0EWM/tuxBvPkDYv1nWkE9lCkB29sKiVE5rx5ngTZAhZN3uXI4QDeOqzTlqVR/A8u4QtmzKm+Lemx8+2VkM8vVbDnqMzmYCjjJExmQ6f0/I7HjKqT8UmuUL1N2nlUFtjVQrHZCVDZmzSp5xoJZnSbz7rVNcRMPIugXf8U0LF1tm2en6+ytVnx0FH7Hs72r47MQX+8FKJF5sON5XCo3JssdHnFAEqE/EWbQFly3Sfqe3AhXCFAMD7pQL4wp6iyyEiccfbryba2NBgW2pXOG56dLorgv963vRg7euhfvM91+oyuyj4oyyExGC0fxHMcFAGO6Vtd6J9HBDOeXW433wZ10NdhEmhsawMEEf/icxQBEeJmGTIO36Zm7dsDeMC/GPMs6TM74aH3qjUOxllMHvc38zDE7sgzEO3Q/btHMgjCJIG9UJuSCgjQJCLj3an3urx+4A4BMQIrmnl2oJrO32BhZsBuCnnDhrtVWtVNnTxx6jeLzxa4eZD6MGIF6xNN6FZjzunNobJoQjucZYaDFp6aHSbmnJmPRQb2oY6UQgoIODGjTdWN6xXzVbxuoknlCTfyeISW8eQhBO0cI2wxeowg6IORGJ6QnjINTCNd/HLtkvUsYSA8K/m7RobILY8DueItXnSr9qXih9brZrhzXiQoks0kNy60aXwQky8NTEnvqARNVszjDHXfB8NZRJZggJVw2Dw+/Yagq4y57WQN+FmmEO+8iXpZpYP6wwqFaVLgtegW9+np27PTkQdkomUO5RbjDL5ld1Z3RF9eAx510g1aJAuxH0Nnwcb3RWw7rwDycMM7NTPdcKTiv+9USd6U4InwxUTTVi9wRtGEZih56XYVsi+O61ckZRDc1fQ2oOvC0xy6T2QmMeXHJtn5DwUIPSkAWLYXGS5XX1L5GTz8ncfvaRT9N2uVkMyQziwREYSGlLhKBXWCC7jHSRkshUPgj7sKH08DQdSmhfY+PGcROo6EpoHQfQ/wpvqk8QvmTinH5EkLzpuzPUybBe1s4N4c85MjnnAjTZmAAdpHuFOolOGlu2akowzbFyETB5dPg=|81P28FXMXjS1HbDGeFP6Ek/IzXg1UFd/UeluwMoxo0g=",
  "__PROTECTED__key": "AhldjrdCpJPuNu+y9u2ZFuSB5R8niXLQeE/zUcny4Da7yy25edUV/qpEiBpUDsPnkwBGcsV539qPMNiPGCyU3vzf6KBX/FSeFJMEqEpkwV+RlWJuHQ1ecxcM7xQuX+EBKg==",
  "encOrgKeys": {},
  "securityStamp": "RPCATQMLER2IFHITKSMIKXEEOGAPFBY2",
  "organizations_c781fc69-c878-4d20-a832-ad8800bce257": {},
  "folders_c781fc69-c878-4d20-a832-ad8800bce257": {},
  "collections_c781fc69-c878-4d20-a832-ad8800bce257": {},
  "ciphers_c781fc69-c878-4d20-a832-ad8800bce257": {
    "166f1415-5cad-468b-9b17-ad8800bdb063": {
      "id": "166f1415-5cad-468b-9b17-ad8800bdb063",
      "organizationId": null,
      "folderId": null,
      "userId": "c781fc69-c878-4d20-a832-ad8800bce257",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-08-18T11:30:38.1907593Z",
      "type": 1,
      "name": "2.ol3m1Y+NQdGNfnVoSEtb6w==|YJtmEoty615gCocaZ/wFjA==|IWNe0I4eOZIgA/aTKOZYaxOyUn8oSBoia4je4cNacYA=",
      "notes": "2.gqzzvelO1k8Pvguu7xZBaQ==|wv84YDI09IlOgnndS287CA==|rFHs6MwMAmJMqklN/QEjOi3aHYxgX2k0BW7t2McvdMk=",
      "deletedDate": null,
      "reprompt": 0,
      "login": {
        "username": "2.aBx+lujd1hJ7aFBOH2sYYw==|E56TAGdilAyepd3F4GV7KA==|I9FI14p1g9kQYWLpqAl8xc2Kmnu3GTHGqXNoqpUzonY=",
        "password": "2.Y97IK/VcxfPJrX8W/I6u7w==|mSD7J6tXHaljDDrOAtG97Q==|NUXKEHHUqHFfKhEm8BQa7oGyAvR9fqNay69OWwRzL68=",
        "passwordRevisionDate": null,
        "totp": "2.l0qwRidnJhQGWfi2zmfBbw==|yBOAZ2pDJ4g1ub9t2mO+qKjIWRPRQhRQ2sP7nLjI8T0=|6dn5q+IfheewlXmjdv0OUsfQ1SG06ymU09Hc0aocm+o=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    }
  },
  "sends_c781fc69-c878-4d20-a832-ad8800bce257": {},
  "settings_c781fc69-c878-4d20-a832-ad8800bce257": {
    "equivalentDomains": []
  },
  "policies_c781fc69-c878-4d20-a832-ad8800bce257": {},
  "lastSync_c781fc69-c878-4d20-a832-ad8800bce257": "2021-08-18T11:30:21.779Z"
}
```

The item created had the following properties:
```
name: "testItem"
notes: "Item for CIS695"
login: {
  username: "jake"
  password: "hunter2"
}
```

All my testing for trying to decrypt the password from the JSON: "2.Y97IK/VcxfPJrX8W/I6u7w==|mSD7J6tXHaljDDrOAtG97Q==|NUXKEHHUqHFfKhEm8BQa7oGyAvR9fqNay69OWwRzL68="
were unsuccessful. It was found in the BitWarden codebase that this string can be broken into `<encryption type>.<iv>|<data>|<mac>`. The encryption type of 2 seemed
to mean AES-256-CBC as expected. I added debug statements to the BitWarden source code during its encryption to have it print out the exact key, iv, data, and mac
used during the decryption and found the following values:
```
key: d4 2f 29 87 a1 b9 1e 36 8c 60 4a b5 2e ef a5 65 5e 16 ea 34 39 12 11 fc a5 ee d9 ab df bb ea f2
data: 99 20 fb 27 ab 57 1d a9 63 0c 3a ce 02 d1 bd ed
iv: 63 de c8 2b f5 5c c5 f3 c9 ad 7f 16 fc 8e ae ef
mac: 35 45 ca 10 71 d4 a8 71 5f 2a 11 26 f0 14 1a ee 81 b2 02 f4 7d 7e a3 5a cb af 4e 5b 04 73 2f af
```
```
key: d42f2987a1b91e368c604ab52eefa5655e16ea34391211fca5eed9abdfbbeaf2
```

These are the same values if the above string parts are converted from base64 to hex. If I use openssl to decrypt with aes-256-cbc using the above values, I am
able to retrieve the original password (hunter2). However, I was not able to retrieve the key from my SMI search technique. It appears BitWarden is using the
same variable for or encryptions and decryptions and for logging purposes, so it is possible that it is rewriting the memory location with a new aes key so I
might not have gotten the key before it was removed from memory. After looking in a memory dump after using BitWarden, I was able to find the key, but not the
full key schedule and the key was not near the json found above. More investigation would need to be done to potentially find those in a memory search or a
different algorithm to search for them.

