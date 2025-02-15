When setting up QEMU to run an Ubuntu image & installed bitwarden cli tool to that VM. 

# Bitwarden CLI Vault Creation
I was able to create vaults with following command after creating bitwarden account online with my umich email:
```
node bw.js get template item | jq ".name=\"local\" | .login=$(node bw.js get template item.login | jq '.username="moe" | .password="Rounds2021"')" | node bw.js encode | node bw.js create item
```
above command was ran by building the cli code locally and running locally. I ran the same command
with the cli binaries installed globally on my machine and just replaced "node bw.js" with 'bw'. 

When creating vaults I dumped memory many times and was able to find the json load to create an item
in memory with password encrypted & decrypted. Below is an example of the json objects I was able to find in memory:

```
"__PROTECTED__key": "AkMZhRMaIqyG6/XE6UsoxOACQzrNrEXO7PzLlDI9isx7DF6LIZfRq5zFKRqI9+6+WV0ON4rYCP62SaJFxe4mMc8GSKSt4WtgDKXjP6gFS4rktMoXCycu1v8q3RIg11UFJw==",
  "encOrgKeys": {},
  "securityStamp": "b14b1a01-fe40-43de-9eed-be9b891e70cd",
  "forcePasswordReset": false,
  "organizations_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "providers_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "folders_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "collections_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "ciphers_14d4a0bc-763c-436f-8e28-adb6014610f8": {
    "d1ee61d8-321a-4f9f-9688-adb6014b6916": {
      "id": "d1ee61d8-321a-4f9f-9688-adb6014b6916",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-03T20:06:37.72Z",
      "type": 1,
      "name": "2.XZz6ZTa3N/ugg1fNc+zhwQ==|owoR1HM30+33Em2oJD2cnw==|KcWwDfhDpqMF6LKXp2qY4B4YUKKswTnIQndae0CDYv8=",
      "notes": "2.s78zd5CjwYb2Pg0keks2ow==|zjpOCgeyEiZmUeMLX0FYUIxpulxpIhu0z/Umx5dUo/U=|KkhTg8pTb98QO+E0UdU/FivHe7ln0UMHYrbNWHrz8rY=",
      "collectionIds": [],
      "deletedDate": null,
      "reprompt": 0,
      "login": {
        "username": "2.qn/9SeDtS4+3in631VgFhg==|tqGvgyNgnCPN1p/g42vr0w==|o5yR7GILriPRhbIOKGrimqaWTiBUCC09Vs5GC/kxuJs=",
        "password": "2.US0Qp3LBTCrdL04Ho6VGrw==|zds4jniTI5AsXp24754OTw==|zztzQH/4MeWTDRBpcQwhWgMiEMT3JFlfL5o2W93UXxg=",
        "passwordRevisionDate": null,
        "totp": "2.AxDD5/2chKr/ouLnwwknvw==|+rO+GwV9ooRsoFFD3Er9FOOLNmAxJuPQ/gmXlnz7Adk=|vj402h+8+K+atoldckS41plzGxUU4HbHeP2ggK9lCFU=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    },
    "f259bb34-72b1-4032-9ad0-adb60178e648": {
      "id": "f259bb34-72b1-4032-9ad0-adb60178e648",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-03T22:52:14.9533333Z",
      "type": 1,
      "name": "2.jAYz8dhSGF6b4goCNp+fJA==|60TEwR17LVuEoGLelWfPYA==|+n6mzvhUwKM86Nh5Z222P4LZYK4XCji5+jP4jjkvsMo=",
      "notes": "2.ozH60bsxKaNKXmT41BLxjQ==|N9Gr5vT2g7UvPEh2jWo8K6+jtmuOZaUApuZlawk+T8A=|NFqcpc+3rfsGKIxikmI3FWQGfnoEllhvg53N6pAv1ws=",
      "collectionIds": [],
      "deletedDate": null,
      "reprompt": 0,
      "login": {
        "username": "2.gPAjuZdMn32v4uMQPoo0XA==|mvazwPAVn8+jhzGKxo/igg==|rmG4nr/pf1j+flrmFK1L/SeRH7+rJUOIU1ilywb3a8k=",
        "password": "2.LeaxTrjeeIZIFBK/f03Nfw==|Vb/f9QNmVK7pdOWEPzJKgw==|h8knNixAraN/4jSyN04gf0ZJT/j+0GH7fcOw81PqSxs=",
        "passwordRevisionDate": null,
        "totp": "2.6102qzrIqXXlVx5U40N52g==|iQkNEdaeXKiP15+4oKAgkETVKAug+QbkoQGCUJgfzo8=|XX9lVtjOltWz0ZBKdLNP5yXygqr2Wml7fOfNj1ofrew=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    },
    "1f2f7534-37a9-42db-b3b6-adb60179199f": {
      "id": "1f2f7534-37a9-42db-b3b6-adb60179199f",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-03T22:52:58.7633333Z",
      "type": 1,
      "name": "2.3i+ArrUzpqWkA9rZaIthfQ==|B9R+6b+rvOrhTACmV+9AbA==|/tqNKb9TQH4PgV0C9FuKW4KVct5/nKQupuA8Pf+F0oI=",
      "notes": "2.wTwxTsXZIxwDsyYOGAh6Vg==|6nbyUSJxeq4EwfOJDUjcCNvryWB9EMFhyX9ojXeWbog=|gp8AY7jqKWxV36IK2UgI+hGPLdw59g/LPssmBG5h4UY=",
      "collectionIds": [],
      "deletedDate": null,
      "reprompt": 0,
      "login": {
        "username": "2.YMDLYz+v1bCt0UHAdWdeEg==|mrsqrx2tpTIP3JdmRhp0IQ==|1op/8sdcvFuCISRllJD5ldysub6co9Rn+hTHDAIHagA=",
        "password": "2.AEqjnCZm+l0znHKPtaN0Jw==|4DKf9M2NCUQPTaArOvOWRQ==|Xrx37rw+eEje22HqeBvSdfuCeHZUG0Du/znmRhnTHho=",
        "passwordRevisionDate": null,
        "totp": "2.IcpcxLct30d/TZV/qeqM+Q==|LUPw6FRpPCxH16nZhfQeWQmLsEjv8N1rNBP4rfccqwc=|Pvf5qv8Z7K7o3FLydxnnPdwIMxWJr20J18LcNKUgaqs=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    }
  },
  "settings_14d4a0bc-763c-436f-8e28-adb6014610f8": {
    "equivalentDomains": []
  },
  "policies_14d4a0bc-763c-436f-8e28-adb6014610f8": {}
}
```

Json object with password decrypted state:

```
{"object":"item","id":"a9a9f214-4879-4583-bf33-adcd010623f5","organizationId":null,"folderId":null,"type":1,"reprompt":0,"name":"local","notes":"Some notes about this item.","favorite":false,"login":{"uris":[],"username":"ahmed","password":"Ngrcicd2021","totp":"JBSWY3DPEHPK3PXP","passwordRevisionDate":null},"revisionDate":"2021-10-26T15:54:25.449Z"}
```




# Bitwarden Account Login
created a testing password for my bitwarden account with "Cis_695_testing". I was able to login 
with the following command:
```
bw login
```
During login, I dumped memory and was able to find the in decrypted state as shown below in seven occurrences
```
./bw login
aaldhahe@umich.edu
Cis_695_testing

X   …Ä•°3          @ ÕG M o> oP    	Ä•°3  RœUà   _questionCallback{WÌ«=  	Ä•°3  ≤Æ®
   _oldPrompt  !  ˘Ä•°3        .@yÄ•°3     %   1`Ç÷P  —Ä•°3  IÄ•°3     %   ? Master password: [inCis_695_testing   °;8∂Ù  )

•°3  …xÇ÷P         …MÄ•°3  	]≠à<  ô8∂Ù         9Ë€40  )ÖÂÎ  Ÿ∆(˛À:  ˘Ä•°3          ˘Ä•°3   –<ëÕwBIÄ•°3        Cis_695_testing )Ä•°3         ±PÇ÷P  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  AÄ•°3  ˘Ä•°3        .@yÄ•°3     %   IzÇ÷P  —Ä•°3  IÄ•°3     %   ? Master password: [inCis_695_testing   °;8∂Ù  )

```
Also, attempted to look for patterns of aes-256-cbc encryption (`<encryption type>.<iv>|<data>|<mac>`) and base64 patterns `==|` and was only to find a place of interest in thos places:
```
2%ì®        ˇˇˇˇ    ˇˇˇˇ    Aq€   A˜   –óu   û ™Ã    b5gG7SzzuKLLNfVXPâ˚újÄÙæﬂ8“    nMNayBwuwA==|Ew98`P¶:¸4’ı”≈Ñ    Q==|

,5(∫'@        Äÿ;     ÿ;    Aq€   A˜   –óu   û ™Ã    ame":"2.RT6uztGe@ˇÜÄ$*Ta©V.    1myQGBQ==|OCaKV8¨©œã'Ê}ß†    ta":{"Uri":null,=|OjjYeEKy34wTdRn1myQGBQ==|OCaKV8gyn8OmK6Lopia64j˚

"installedVersion": "1.18.1"I¿¥     @   ,
  "appId": "5a162903-3d4f-47f7-8bbf-5deb7dd1fe73",
  "encProviy¿¥     `   ëdâˆ:  ¡dâˆ:  I¿¥     Ä   derKeys": {},
  "emailVerified": true,
  "sends_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "lastSync_14d4a0bc-763c-436f-8e28-ay¿¥     ‡   eâˆ:  1eâˆ:  I¿¥        db6014610f8": "1970-01-01T00:00:00.000Z",
  "accessToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IkJDMzZDMjE0REI0OEYyMzVCNzdEQTNGMTcyMEMxQTM1QTk2MkVBNDNSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InZEYkNGTnRJOGpXM2ZhUHhjZ3dhTmFsaTZrTSJ9.eyJuYmYiOjE2MzU3Mjk2MzMsImV4cCI6MTYy¿¥     ‡  ¡eâˆ:  ·eâˆ:  I¿¥        zNTczMzIzMywiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5iaXR3YXJkZW4uY29tIiwiY2xpZW50X2lkIjoiY2xpIiwic3ViIjoiMTRkNGEwYmMtNzYzYy00MzZmLThlMjgtYWRiNjAxNDYxMGY4IiwiYXV0aF90aW1lIjoxNjM1NzI5NjMzLCJpZHAiOiJiaXR3YXJkZW4iLCJwcmVtaXVtIjpmYWxzZSwiZW1haWwiOiJhYWxkaGFoZUB1bWljaC5lZHUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwic3N0YW1wIjoiYjE0YjFhMDEtZmU0MC00M2RlLTllZWQtYmU5Yjg5MWU3MGNkIiwibmFtZSI6IkFobWVkIEFiZHVsc2FsYW0gQWxkaGFoZXJpIiwiZGV2aWNlIjoiNWExNjI5MDMtM2Q0Zi00N2Y3LThiYmYtNWRlYjdkZDFmZTczIiwianRpIjoiQjFDRTA5NENCQ0U3MjYxQTJEMEYyNzkxQTRy¿¥     ‡  Òfâˆ:  gâˆ:  I¿¥        EQThDRUUiLCJpYXQiOjE2MzU3Mjk2MzMsInNjb3BlIjpbImFwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJBcHBsaWNhdGlvbiJdfQ.pxb4T4izeuK2TW7fqzWjy55GsIOSZjS2CXmiCEghqCB3xRnTi55DpA5AsJEIg5MqfSnflnniFBId6mat34xaRuPCOi6FIeNs5Z-e5mieOqhSGLBC_R2b8ARxDESmFaieYxmV6l9XU3JDqgnFvDL-Nrs-3xSb0PjgCNo4wJl8pY66OZjB35eeM52XgJWutuRsr08pttikI6Hpb_xQrCBX_-aNuyB2ijVLaThXGwSU-gMyOUjzsNvYSpdH09mBCyQuDqq4paI3s33jB-pebBwOZGXLGVmMp8xqTRLRmYjvIAzy7CRcv325AgfiD0UcLE_PloosVtlXgY7YCcI9kpA6AOw9h1zOpUnacZIe7aGoF-fsdmkLnmoE_KB-wz6icl-mk8nmYs539IM4jOOaiqOnKnsua8vJdCv_kc3lsgrOv6L_EIZjQP_eMaIVI0f-RTKV7kfBj502xejDOCjbAwUebGSSi4rAxsvHYMaQHEmmOS0oREk6w428ZhsCvcj8keRMmEpc9JcVV7JFLzQFladbnsT3BnrD2Vh_2t5OEvRxRbKVNH47-ekN_39Fxg2NMVgAa9mTtyr9mtYtMcUsutP5X9CPV1-nR7n_gWbpnG3ikz120MfshOAtGKfwO8wfym3M7JdGZDk8S8bpFsrf5qI_8TnCe91bR4S8n5U_28oD_go",
  "refreshToken": "E1FB13AE7B60C1AF9F0E16F7D2B5EC8EA78C06A16D029DDD2D528A006C7A7A5D",
  "userEmail": "aaldhahe@umich.edu",
  "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
  "kdf": 0,
  "kdfIterations": 100000,
  "keyHash": "q1y¿¥     ‡  !iâˆ:  Aiâˆ:  I¿¥     Ò   fyPCADGO19Uyuoc9GOAqy2XY2tUcbZ1q/Zl1ehLWU=",
  "encKey": "2.LGNQzSqPRoQgj4luZkP+tQ==|KPeSq7aINKM7DPjeBAy768vfl0d7Q84+P9XqK6vWCSE0Yun+2dgv5IjmEjlXnaqemJdl5ymMVtOJSXCOWdsGhY6SkSubx+b8uF49jqFv6+s=|KZGWdSfD4wOay6830S2kReti1kpzsVhn1+UIWwEEMYk="
}

{
  "installedVersion": "1.18.1",
  "appId": "5a162903-3d4f-47f7-8bbf-5deb7dd1fe73",
  "encProviderKeys": {},
  "emailVerified": true,
  "sends_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "lastSync_14d4a0bc-763c-436f-8e28-adb6014610f8": "2021-11-01T01:19:43.108Z",
  "accessToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IkJDMzZDMjE0REI0OEYyMzVCNzdEQTNGMTcyMEMxQTM1QTk2MkVBNDNSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InZEYkNGTnRJOGpXM2ZhUHhjZ3dhTmFsaTZrTSJ9.eyJuYmYiOjE2MzU3Mjk1ODUsImV4cCI6MTYzNTczMzE4NSwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5iaXR3YXJkZW4uY29tIiwiY2xpZW50X2lkIjoiY2xpIiwic3ViIjoiMTRkNGEwYmMtNzYzYy00MzZmLThlMjgtYWRiNjAxNDYxMGY4IiwiYXV0aF90aW1lIjoxNjM1NzI5NTgzLCJpZHAiOiJiaXR3YXJkZW4iLCJwcmVtaXVtIjpmYWxzZSwiZW1haWwiOiJhYWxkaGFoZUB1bWljaC5lZHUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwic3N0YW1wIjoiYjE0YjFhMDEtZmU0MC00M2RlLTllZWQtYmU5Yjg5MWU3MGNkIiwibmFtZSI6IkFobWVkIEFiZHVsc2FsYW0gQWxkaGFoZXJpIiwiZGV2aWNlIjoiNWExNjI5MDMtM2Q0Zi00N2Y3LThiYmYtNWRlYjdkZDFmZTczIiwianRpIjoiNzREODU5QjBDOUMxN0M1OTc3NzJFNTY3MzUxRDk5RDMiLCJpYXQiOjE2MzU3Mjk1ODUsInNjb3BlIjpbImFwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJBcHBsaWNhdGlvbiJdfQ.DvcQzmdae59Gp06CeolLSQfOdUMh9MqQnFbnrpNWxMhWbX6DQwqjVh1TJzqAJhmbPLhhoy3CpjFDHC8uSpD2ss1ivyNaNXBz--BcF9VZZ1HntMdZYMIHPlR00t1U2NWdouTDsimdiRzzO51vCkqezP35GHtYLqXq0zVC_50FueLWf-0vDs5lOpI6znfDpP_HsEus7spfQiGB0124bZc75lFsY_db6XA0-uQGYZfg6UM2M25SG_bmHaTAWqDDOcVhNSPpUbnNteKpVTHWq1kQGpOnoE20_KhgNKLmjX294u-_Y5JZlyYUG5DQjWMa0OWHUqCu6w4Dv9OAQnFb2e2odZZiMSg0sBvMk01y1mYRiWM2krZSIsiQYkGQjPwhb310a6mWe,
      "favorite": false,
      "revisionDate": "2021-10-26T01:54:13.1866667Z",
      "type": 1,
      "name": "2.N1ZuHtB1AJKbfXShi4NGGQ==|cx5ugMXIrk7+MuJbCUYFYQ==|aplFzufb/kAlps+b16r7FHUr/E3Bnb/YNfrWkn/lfJY=",
      "notes": "2.b3+nCy/BZ/2iTwLl4XLqCA==|O81Fsywakb01cN0xtQ7zImPxGpEpTV4cuyqH590eGGk=|wDY7woBgzi+SIN96lwp4mX/SGgJfQPEBSGFDcPLzBu8=",
      "collectionIds": [],
      "deletedDate": "2021-10-26T01:54:13.19Z",
      "reprompt": 0,
      "login": {
        "username": "2.O8XevgKMSSoGCyqH6NSZeg==|Wkk+leGJ518kTp7ptqkh6g==|icByfPF/dQk2PbUt3f6hFJSYaSi41sJU/qxcJaQAm/o=",
        "password": "2.W2TIcMAA+pqJFzdulFbWOw==|x7KF1EbQwcg6ue0NYO+1Hg==|ahDcXptjrDAUlYY52F2L1fySnCkm4n5KlCiHxg7Dl4A=",
        "passwordRevisionDate": null,
        "totp": "2.9qoNIc3ryYCaBPM1oRriag==|Vj+YRjY5ob9i0F6Lr50Mqmk6k6uaE/NzmH1+/OUt0Sw=|iURa+Bbd0lzA7lAx8looTryHGzo6CzZHfu6n1qDVjlE=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    },
    "42633203-9c54-4b0d-b529-adcd0019e6ba": {
      "id": "42633203-9c54-4b0d-b529-adcd0019e6ba",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-26T01:54:09.9033333Z",
      "type": 1,
      "name": "2.Cza/VZuxXzqMDo9c/kanrw==|Hnc1l7p6rqG5chIHKAcTFg==|PMqGvmCjqahz8fqv9IFOQsCv9s00gCSyZnfyA48noZE=",
      "notes": "2.GFHp8GIELJH2EHBVnY9Hbw==|Oz6KUerE94nV9F2xC5Q4udx+dxGBuR+li1GFMxIlhHU=|EFkQhVtqzvQOpVNFH8m5Nl4p0338IRdqqBYjwTx6+N0=",
      "collectionIds": [],
      "deletedDate": "2021-10-26T01:54:09.9Z",
      "reprompt": 0,
      "login": {
        "username": "2.l4v6RILp54jveasoKdT3mw==|R6T1TUFqzWzCsahdIFQPFA==|go0CPJvkc/vi/8hpcQaItMiqcSmv9X2ZubQ70kuJZpw=",
        "password": "2.Z1iKkiAqAyH0sSvPdRiocA==|kD26eDJoJZWoeLr1aJo+aA==|AVhTjqFXIWBPwOCz+j1qv2I449yoHAyipjKFi4OJXJ0=",
        "passwordRevisionDate": null,
        "totp": "2.r2xzKLbWr2mVZqdV1exu0A==|KGdmtqzDJl1mJye5+7VQXkrrybwf6Qg3VjKzgdocfhg=|ByR3hR896crK9QpVT+AdUjitV++wEuCX/9/qj4LvkRE=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    },
    "96799a24-1d6e-45c9-bef2-adcd001b4c17": {
      "id": "96799a24-1d6e-45c9-bef2-adcd001b4c17",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-26T01:54:05.8533333Z",
      "type": 1,
      "name": "2./Aq1GlNnFzgLDfpQUlKxDw==|o8WuT2r+R9JbZhNYd6vUbA==|mzM4+DtTIKmNKKrzm1/8uYIXwo5Qo18punI4xtoXEiw=",
      "notes": "2.bCaS9M4AeJbFYWVXnXkVZA==|mPo4RgsZ/LjXOXaz6D9LdWVVEnDI3PmzKc7V9V7nKWE=|QDKCnsd7SwVGoiatUU4lOgNjJW6jD/qrifkvwCLN5zI=",
      "collectionIds": [],
      "deletedDate": "2021-10-26T01:54:05.85Z",
      "reprompt": 0,
      "login": {
        "username": "2.42mZkQyL4JS7l0BNizSg6g==|9UK0R2JqdZ2CxTm7xNi04g==|9IkFCzkY2akLHntfKh8mfKypSRsHpodj0oNYlaN/+vs=",
        "password": "2.FfxcNJh/XZPYhRGAYUMZdw==|TIrtb7Kn20aP2AlC9WkByg==|HC6CaNmzn4SbTbTjasdombQrwqxb4RfpMKGVPEGrlwk=",
        "passwordRevisionDate": null,
        "totp": "2.M7JKgdB4GhsgiZm4ADJE/A==|4dJI4GRxqt+K3JGnsS5er12+dftA1Af74RSKyfGG8O8=|ZaR/rqZsDVHwT3IbZeZEYstwq3W1vrBbKWz52FuSE70=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    },
    "7beecff0-d413-44ee-8f9d-adcd001d03f8": {
      "id": "7beecff0-d413-44ee-8f9d-adcd001d03f8",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-26T01:54:01.7633333Z",
      "type": 1,
      "name": "2.1nJWjHLGT91/RpEPDZ2yWg==|ItkoayoQhTzv3yufPXSiaA==|6CII1IM7zdcFE9xqsXz2coIr+2KwuGmh6WJNkiMM20g=",
      "notes": "2.3KrTugZ5GhdSHX1lf1AbGA==|JCQJdLYOkoaH9oGvR+SD2NOudBlt9BGfy0BHO8SLM3g=|Z7DTO/OZHHLiMJxPh06z65EGtOa3Gd1sP82iBmcKlck=",
      "collectionIds": [],
      "deletedDate":85axQZ0PaH3tVO12FZiKPW0Ljnr7TsU7CiAtQ3I1WF9JcHk3hghv7GQVYaESucnnNs8ZBz_XaNr5PI0mGpry0vWgr6nbDReHOoUY8pdfnUPIliiAgeJWuoX_0hf1oyXYoEVC-li1jYl6i96BCsnVa7KjEOsBT0UQYwi9fCuJY7lgVif4EGxkRNFoRAE-bGY9qEfKzgw8RVy8Q3YELTfJUnKqNtFc9DDpnTWwFErL9oZEveFYJCMJJBF4qpSsBga-BN8n6fCLObmka4TwBlESuLkq63Gog_vINam1uIM",
  "refreshToken": "4B243FA35B09033E12D58521045832F635AB7658D8131291707FA59AEFF4F386",
  "userEmail": "aaldhahe@umich.edu",
  "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
  "kdf": 0,
  "kdfIterations": 100000,
  "keyHash": "q1fyPCADGO19Uyuoc9GOAqy2XY2tUcbZ1q/Zl1ehLWU=",
  "encKey": "2.LGNQzSqPRoQgj4luZkP+tQ==|KPeSq7aINKM7DPjeBAy768vfl0d7Q84+P9XqK6vWCSE0Yun+2dgv5IjmEjlXnaqemJdl5ymMVtOJSXCOWdsGhY6SkSubx+b8uF49jqFv6+s=|KZGWdSfD4wOay6830S2kReti1kpzsVhn1+UIWwEEMYk=",
  "encPrivateKey": "2.PRPynyMwuLHhEpyAdoAnnQ==|6c7mDSD+vU7pXk93RDiv4brNNqhqldZCMG2vaFYXK4c9XYr8Gi9FWD9jjW/UzBuH8n+h1PzGfhOaEiJcfBFI9jXNoixSBV09MPXT8Y4By3CAcAveEDYCmnZPeKqh3LhsTmxjJ+GCC5QPJVwkzmzeuW0p67kbszgkMd9SFZ4mazBy35nu1c/Z2MN50QhZSiWiaM7hDEd0xfwDnjq9/hcFydciqUTs/7dDvgTujG8Liq7wQGnBzpF+xbnn43U2f3NLohqj5ugUdfUsOh1g2lwdR6ibku/vJsuQCJphAvCUB0Uetmyax0Da3f98vf61XyFEfND4E0CR0/H028mkxhhpXLKx7n3sBu0xViHxTEaMPe52AwaxgpTmzZMayYOPFNkZB068iNoI2nNJbkCZk8z4WTg7I90Eis8U5qsnbibraO9MP4ghVcA93fgy+gq3PpyCzTLdVxgG1CraUmeNaovGDZQXeGga5T2ztaG7hpkeP/YinNo5B3gfv2iZSufN1CdcG9khuzpAab/r3VNR6tHGHgmt6ku8fJNeTC64+3oUg8DXV6EOgYmv5+K8Z4UZgIBKZWuDHecN4IuKBLNSCcR3JP4nu8d84EwZt53csCo6RB3fvgVa7ruhz1RckHzBYmwI+fX9aexn1DmNbAQt7/AFZRg1SArJnOeGX5EjNwmRkK1uil/RUzUDQOtoOfF5Ob2CQI3xZFs2PuDu4CdBAMFvyEfWiWonYyso1Acmqheepcl73zDe4v3GM09WyRzZu/yAC2wSTAzIMEMlDi8cB9wTcgdg1AwD/NMbH4Et3y80X3f67bBmKeBBZ7EqSFvWEV4JV1GcAboIHFQuErgKnr604ss0L2fJShqSwIHSlBoPKo2lvC9r8GFPuWCL31xB4MPaqOA86V91J+01bXFA2SZFJbQ3lROeCfhdi3t23r7HtYuUXN/HuF43PVlm2FuAQ9BkCKm4mf841nwDcdhH0HUC3q26PBFI7lna2F9xmaAYie2HEf82Tfm2ekh97FPjCh08Tw+JR/1hUkmv7Qm9thM0xv1o+b0T7lqPzDvMRPNoQjUdwXCxUapMGofUgAPJdLXuQrjSVShNu7B//Ylo7TK72voD7Sub9icnJrl6Tj0dXSYVFcEj/b1nSYLaOUgRVSOv0vzgUbCfoynBQHMdmr3v2fb9bhQhR2i2VAFfydczBeBKDT4FMQxnOrpKaatwLP7hOc8JOY/Ry8y2e1ZIpYpjgQcrcEv1xjS2pqz/G/b1MzBvvG7EfgQaVB7mSq5Tum1pwI/DjO8ST9ZEicYzd9UUftKYK27z5USz8lo+P3oXDuErotDYahuiwWmvZxNZXnmhay0gMXEJZ+BNHkr4QRWWLVk04z1b+A9Vf8CkdZP2B2YUzToJekVRNyn7vXYitjJrU6SK2VjzX7xW6vdiPGNlNJ/dI3MNGgQB8Absk2Jvdov/YE6q0P15wH6Bj0YtEKR03hO5RPnUVjLW6npqfuLlucpasDFMONFp0qSO/Jd/MLQd2B/EEGfqYLsoGlCCyAe0qMplWxemBOyd/GVSiOkQ0SB9Kzcsl57Dhm6CGEQPop5OV0PxyXArA0M+iTdeOWX6rycPa2DKMRWqJg4QEd8LJbj9pZ5870GYCwU7pRxZJkM=|j50YzCfHhLm/y38TX69iSMkURwcD2nhfTwc8s/vIhVQ=",
  "__PROTECTED__key": "AriZ1Gxu++fHrWZcTN/MEPMcYIjaZJhmrgqh/TNI2j/d0w6y0BGB0LW2GMlCdiZdZzuPxCBTkjgZDRHovGsu2erHjRsKotiBRrBHtu0gSyGfyB/x/fSNifHgOIBmnjC7Fg==",
  "encOrgKeys": {},
  "securityStamp": "b14b1a01-fe40-43de-9eed-be9b891e70cd",
  "forcePasswordReset": false,
  "organizations_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "providers_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "folders_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "collections_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "ciphers_14d4a0bc-763c-436f-8e28-adb6014610f8": {
    "d1ee61d8-321a-4f9f-9688-adb6014b6916": {
      "id": "d1ee61d8-321a-4f9f-9688-adb6014b6916",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-03T20:06:37.72Z",
      "type": 1,
      "name": "2.XZz6ZTa3N/ugg1fNc+zhwQ==|owoR1HM30+33Em2oJD2cnw==|KcWwDfhDpqMF6LKXp2qY4B4YUKKswTnIQndae0CDYv8=",
      "notes": "2.s78zd5CjwYb2Pg0keks2ow==|zjpOCgeyEiZmUeMLX0FYUIxpulxpIhu0z/Umx5dUo/U=|KkhTg8pTb98QO+E0UdU/FivHe7ln0UMHYrbNWHrz8rY=",
      "collectionIds": [],
      "deletedDate": null,
      "reprompt": 0,
      "login": {
        "username": "2.qn/9SeDtS4+3in631VgFhg==|tqGvgyNgnCPN1p/g42vr0w==|o5yR7GILriPRhbIOKGrimqaWTiBUCC09Vs5GC/kxuJs=",
        "password": "2.US0Qp3LBTCrdL04Ho6VGrw==|zds4jniTI5AsXp24754OTw==|zztzQH/4MeWTDRBpcQwhWgMiEMT3JFlfL5o2W93UXxg=",
        "passwordRevisionDate": null,
        "totp": "2.AxDD5/2chKr/ouLnwwknvw==|+rO+GwV9ooRsoFFD3Er9FOOLNmAxJuPQ/gmXlnz7Adk=|vj402h+8+K+atoldckS41plzGxUU4HbHeP2ggK9lCFU=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    },
    "f259bb34-72b1-4032-9ad0-adb60178e648": {
      "id": "f259bb34-72b1-4032-9ad0-adb60178e648",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-03T22:52:14.9533333Z",
      "type": 1,
      "name": "2.jAYz8dhSGF6b4goCNp+fJA==|60TEwR17LVuEoGLelWfPYA==|+n6mzvhUwKM86Nh5Z222P4LZYK4XCji5+jP4jjkvsMo=",
      "notes": "2.ozH60bsxKaNKXmT41BLxjQ==|N9Gr5vT2g7UvPEh2jWo8K6+jtmuOZaUApuZlawk+T8A=|NFqcpc+3rfsGKIxikmI3FWQGfnoEllhvg53N6pAv1ws=",
      "collectionIds": [],
      "deletedDate": null,
      "reprompt": 0,
      "login": {
        "username": "2.gPAjuZdMn32v4uMQPoo0XA==|mvazwPAVn8+jhzGKxo/igg==|rmG4nr/pf1j+flrmFK1L/SeRH7+rJUOIU1ilywb3a8k=",
        "password": "2.LeaxTrjeeIZIFBK/f03Nfw==|Vb/f9QNmVK7pdOWEPzJKgw==|h8knNixAraN/4jSyN04gf0ZJT/j+0GH7fcOw81PqSxs=",
        "passwordRevisionDate": null,
        "totp": "2.6102qzrIqXXlVx5U40N52g==|iQkNEdaeXKiP15+4oKAgkETVKAug+QbkoQGCUJgfzo8=|XX9lVtjOltWz0ZBKdLNP5yXygqr2Wml7fOfNj1ofrew=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    },
    "1f2f7534-37a9-42db-b3b6-adb60179199f": {
      "id": "1f2f7534-37a9-42db-b3b6-adb60179199f",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-03T22:52:58.7633333Z",
      "type": 1,
      "name": "2.3i+ArrUzpqWkA9rZaIthfQ==|B9R+6b+rvOrhTACmV+9AbA==|/tqNKb9TQH4PgV0C9FuKW4KVct5/nKQupuA8Pf+F0oI=",
      "notes": "2.wTwxTsXZIxwDsyYOGAh6Vg==|6nbyUSJxeq4EwfOJDUjcCNvryWB9EMFhyX9ojXeWbog=|gp8AY7jqKWxV36IK2UgI+hGPLdw59g/LPssmBG5h4UY=",
      "collectionIds": [],
      "deletedDate": null,
      "reprompt": 0,
      "login": {
        "username": "2.YMDLYz+v1bCt0UHAdWdeEg==|mrsqrx2tpTIP3JdmRhp0IQ==|1op/8sdcvFuCISRllJD5ldysub6co9Rn+hTHDAIHagA=",
        "password": "2.AEqjnCZm+l0znHKPtaN0Jw==|4DKf9M2NCUQPTaArOvOWRQ==|Xrx37rw+eEje22HqeBvSdfuCeHZUG0Du/znmRhnTHho=",
        "passwordRevisionDate": null,
        "totp": "2.IcpcxLct30d/TZV/qeqM+Q==|LUPw6FRpPCxH16nZhfQeWQmLsEjv8N1rNBP4rfccqwc=|Pvf5qv8Z7K7o3FLydxnnPdwIMxWJr20J18LcNKUgaqs=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    },
    "dd7b6833-c1a6-4e26-b816-adcd0018db4d": {
      "id": "dd7b6833-c1a6-4e26-b816-adcd0018db4d",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": false,
      "favorite": false,
      "revisionDate": "2021-10-26T01:30:30.0166667Z",
      "type": 1,
      "name": "2.ef23Mwa66wk2i9mLeNsT5Q==|4ZsuOmaE2OryEPwcoVKCTg==|LDI+6pAoA8hE3JbFwngn+tK5+jg/3CgeiNqd48W5tRQ=",
      "notes": "2.r0Sfkb+XRwXF3L7SxGihdA==|yHvXrpYvm1uRm/gpta8niWNK+PAZ8dzy8rygm5PZuRs=|Bf8BA06AOK0SQOfZL+pWcnw7eJFzDUk8G23AUR0I/to=",
      "collectionIds": [],
      "deletedDate": null,
      "reprompt": 0,
      "login": {
        "username": "2.Sn8TN1bjRyL/IIv3exiGLQ==|Eq8KXV2fMoCucmse39Qm+Q==|gEaCGlMOOX8nq0zz/yXV9gEzEIcDtvOGcisxYbHJnLE=",
        "password": "2.Y76gtR2G65X4nMy9VRnmOw==|+0DOvbG1sdZCZ1XNGDLvIQ==|S+kiB9QIsP0kLqVqfgayP3EQIUmtjps8coS15MEonEU=",
        "passwordRevisionDate": null,
        "totp": "2.IAP1HUXeUjWarozuwK27Rw==|COVLL0duLNDAo9JvG0LnVqNrVb9MT43rVV0lVde7Q20=|1Pl6Xd5MFhn5Kkt2X32F4Foibu6Zb9Tf4HSnrUFPx+A=",
        "autofillOnPageLoad": null,
        "uris": []
      }
    },
    "e79ec4a6-ab0c-4a31-a0ea-adcd00194532": {
      "id": "e79ec4a6-ab0c-4a31-a0ea-adcd00194532",
      "organizationId": null,
      "folderId": null,
      "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
      "edit": true,
      "viewPassword": true,
      "organizationUseTotp": falsâ


```

# Key Generation
I looked at Bitwarden cli source code to figure out the key generation algorithms they use to generate keys. I was able to find some key generation algorithms in WebCryptoFunction.service.ts (/cli/jslib/common/src/services/webCryptoFunction.service.ts) & (/cli/jslib/common/src/services/crypto.service.ts)
```
async pbkdf2(password: string | ArrayBuffer, salt: string | ArrayBuffer, algorithm: 'sha256' | 'sha512',
        iterations: number): Promise<ArrayBuffer> 
```
There are other key generation methods being used other than pbkdf2 but a lot of time is needed to detect those and debug. The above pbkdf2 method generates a key for the password entered by the user, it uses sha256 algorithm & uses user email for salt. Once the key is generated then other algorithms are used to generate keys from the result of pbkdf2. However, I didn't have enough time to debug or scan the source code due to time limitation. I believe if a person spends more time to add debug statements they might run into something interesting but the execution flow of the code is a bit complex to a point its hard to detect all the paths/algorithms used for password key generation.

