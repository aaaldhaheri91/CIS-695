import regex
import dirtyjson 
import json 
# str words = ""

with open('../bitwarden_dump1.txt', 'rb') as f:
    for line in f:
        # json_expr = "{"+line.partition("{")[2]
        # the_dict = json.loads(json_expr)
        # print (the_dict)
        print (line)

# regex = '{(?:[^{}]|(?R))*}'
text = '''laksjdflksjdflksjdlfjasldfjas;ldfjsdklfjaslkjdflks{
  "installedVersion": "1.18.1",
  "appId": "5a162903-3d4f-47f7-8bbf-5deb7dd1fe73",
  "accessToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IkJDMzZDMjE0REI0OEYyMzVCNzdEQTNGMTcyMEMxQTM1QTk2MkVBNDNSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InZEYkNGTnRJOGpXM2ZhUHhjZ3dhTmFsaTZrTSJ9.eyJuYmYiOjE2MzMzMDE1MzQsImV4cCI6MTYzMzMwNTEzNCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5iaXR3YXJkZW4uY29tIiwiY2xpZW50X2lkIjoiY2xpIiwic3ViIjoiMTRkNGEwYmMtNzYzYy00MzZmLThlMjgtYWRiNjAxNDYxMGY4IiwiYXV0aF90aW1lIjoxNjMzMjkzMjY4LCJpZHAiOiJiaXR3YXJkZW4iLCJwcmVtaXVtIjpmYWxzZSwiZW1haWwiOiJhYWxkaGFoZUB1bWljaC5lZHUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInNzdGFtcCI6IlhVWENRVDJSWVVaRkw3SENDNE1UM1kyM0RJWk9PSEtUIiwibmFtZSI6IkFobWVkIEFiZHVsc2FsYW0gQWxkaGFoZXJpIiwiZGV2aWNlIjoiNWExNjI5MDMtM2Q0Zi00N2Y3LThiYmYtNWRlYjdkZDFmZTczIiwianRpIjoiQjM5NTg3ODJDNzMyNEUyRUZCOTM5QUQzRURCODM3MjkiLCJpYXQiOjE2MzMzMDE1MzQsInNjb3BlIjpbImFwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJBcHBsaWNhdGlvbiJdfQ.SoNdysByTq4-CNOkVuieFt1V6GFYpeIKnPAw93scqr6pj3nbUBgRyDwS9nC0Kd4rF1cdRMdMbQYBPjErbE-W3jNRJmPz-rH45KdNQeR7ieVgZyO3V2lickRtLcr_A__n-YN4TFkbFOvp3ttDsgdMFOUZqD_RrsJ-kA6MtLa48Z6cfQl-7Gemg8rQcXveT2XgqK6xR6hEn5zS6K_sRBY7TEcUGUlxTYTgUD69G4B3JyO6eTseaHXQmzQ97nlPHOSHefyGyZ3l6dKAUG4Czd7YpfBZOKvfc1ZB6-CWwJMBLXwv1nbUtBGncuayYo6lC6QzWX3Ni1KCsyvb7pIgxTsujJ0KXPaCdLi_Wrhdu-p94EIQ1e-AnMDw3VqFLbu9IgoK5b3eMaE_zPHtejSkbFNzo1263nNiw2fZlBEGT7orto-Na9Os_60qADBca2E501NzdEf2CSJy6w_eSEK8LWMbjwCkS5O4AEQggyTsyv02PKMwhXQaxpm6buP93Z_QzNiBX6-_2d3lVrefll4cEMh7V56wP0Xu2dVXkGhc4_3TJNhMJbjFLcER9JhxDsniBwMM8fz3c0E4kO06cMK7hCUqYQsv-jebKonLcQKuzfiqi2RTgSOqjBIK9N1rCVYbTI1jTb3q5c_arj0V0rmUKhgyGXXukuQf8g4_BbQ82jteq0A",
  "refreshToken": "3272797A73367D50A96E27E9B91F9996A0D83FDE718B1D1832E316AE5DC51F83",
  "userEmail": "aaldhahe@umich.edu",
  "userId": "14d4a0bc-763c-436f-8e28-adb6014610f8",
  "kdf": 0,
  "kdfIterations": 100000,
  "keyHash": "PpgXV7602FjuLKNM9PRJtWyd3CEhrKzO/AhGUQ8YbUA=",
  "encKey": "2.yFRDKeTymo5TKOR8KUsctw==|XPzxfdql0IGG07iyb+tfnaq47yeOvmJujRSxFWpfzaHUVV5ZgyPRltxMYzPvGf2LSfYJU3b7xE9bGnAB8NAQkwNEz5ZHVGLp8AVa6LFXnzw=|/wcq3HxxEedE8Moa7PouRwAyCIRrp3yeeExf4rM93yE=",
  "encPrivateKey": "2.PRPynyMwuLHhEpyAdoAnnQ==|6c7mDSD+vU7pXk93RDiv4brNNqhqldZCMG2vaFYXK4c9XYr8Gi9FWD9jjW/UzBuH8n+h1PzGfhOaEiJcfBFI9jXNoixSBV09MPXT8Y4By3CAcAveEDYCmnZPeKqh3LhsTmxjJ+GCC5QPJVwkzmzeuW0p67kbszgkMd9SFZ4mazBy35nu1c/Z2MN50QhZSiWiaM7hDEd0xfwDnjq9/hcFydciqUTs/7dDvgTujG8Liq7wQGnBzpF+xbnn43U2f3NLohqj5ugUdfUsOh1g2lwdR6ibku/vJsuQCJphAvCUB0Uetmyax0Da3f98vf61XyFEfND4E0CR0/H028mkxhhpXLKx7n3sBu0xViHxTEaMPe52AwaxgpTmzZMayYOPFNkZB068iNoI2nNJbkCZk8z4WTg7I90Eis8U5qsnbibraO9MP4ghVcA93fgy+gq3PpyCzTLdVxgG1CraUmeNaovGDZQXeGga5T2ztaG7hpkeP/YinNo5B3gfv2iZSufN1CdcG9khuzpAab/r3VNR6tHGHgmt6ku8fJNeTC64+3oUg8DXV6EOgYmv5+K8Z4UZgIBKZWuDHecN4IuKBLNSCcR3JP4nu8d84EwZt53csCo6RB3fvgVa7ruhz1RckHzBYmwI+fX9aexn1DmNbAQt7/AFZRg1SArJnOeGX5EjNwmRkK1uil/RUzUDQOtoOfF5Ob2CQI3xZFs2PuDu4CdBAMFvyEfWiWonYyso1Acmqheepcl73zDe4v3GM09WyRzZu/yAC2wSTAzIMEMlDi8cB9wTcgdg1AwD/NMbH4Et3y80X3f67bBmKeBBZ7EqSFvWEV4JV1GcAboIHFQuErgKnr604ss0L2fJShqSwIHSlBoPKo2lvC9r8GFPuWCL31xB4MPaqOA86V91J+01bXFA2SZFJbQ3lROeCfhdi3t23r7HtYuUXN/HuF43PVlm2FuAQ9BkCKm4mf841nwDcdhH0HUC3q26PBFI7lna2F9xmaAYie2HEf82Tfm2ekh97FPjCh08Tw+JR/1hUkmv7Qm9thM0xv1o+b0T7lqPzDvMRPNoQjUdwXCxUapMGofUgAPJdLXuQrjSVShNu7B//Ylo7TK72voD7Sub9icnJrl6Tj0dXSYVFcEj/b1nSYLaOUgRVSOv0vzgUbCfoynBQHMdmr3v2fb9bhQhR2i2VAFfydczBeBKDT4FMQxnOrpKaatwLP7hOc8JOY/Ry8y2e1ZIpYpjgQcrcEv1xjS2pqz/G/b1MzBvvG7EfgQaVB7mSq5Tum1pwI/DjO8ST9ZEicYzd9UUftKYK27z5USz8lo+P3oXDuErotDYahuiwWmvZxNZXnmhay0gMXEJZ+BNHkr4QRWWLVk04z1b+A9Vf8CkdZP2B2YUzToJekVRNyn7vXYitjJrU6SK2VjzX7xW6vdiPGNlNJ/dI3MNGgQB8Absk2Jvdov/YE6q0P15wH6Bj0YtEKR03hO5RPnUVjLW6npqfuLlucpasDFMONFp0qSO/Jd/MLQd2B/EEGfqYLsoGlCCyAe0qMplWxemBOyd/GVSiOkQ0SB9Kzcsl57Dhm6CGEQPop5OV0PxyXArA0M+iTdeOWX6rycPa2DKMRWqJg4QEd8LJbj9pZ5870GYCwU7pRxZJkM=|j50YzCfHhLm/y38TX69iSMkURwcD2nhfTwc8s/vIhVQ=",
  "__PROTECTED__key": "AnyG72dyGElQ5uo6x36JYvQQHESaNjMnkzrtuYzMkOjsDu8sEgSlI972JNcTtz0wJ7HD9bZgEPcV1NfnH9UJ2K+6e7rZ8n80Jee+Cp1MCYwT6zBGxqOCddSUFKJhx+I/Kg==",
  "encProviderKeys": {},
  "encOrgKeys": {},
  "securityStamp": "XUXCQT2RYUZFL7HCC4MT3Y23DIZOOHKT",
  "emailVerified": false,
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
      "revisionDate": "2021-10-03T22:52:14.9536475Z",
      "type": 1,
      "name": "2.jAYz8dhSGF6b4goCNp+fJA==|60TEwR17LVuEoGLelWfPYA==|+n6mzvhUwKM86Nh5Z222P4LZYK4XCji5+jP4jjkvsMo=",
      "notes": "2.ozH60bsxKaNKXmT41BLxjQ==|N9Gr5vT2g7UvPEh2jWo8K6+jtmuOZaUApuZlawk+T8A=|NFqcpc+3rfsGKIxikmI3FWQGfnoEllhvg53N6pAv1ws=",
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
    }
  },
  "sends_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "settings_14d4a0bc-763c-436f-8e28-adb6014610f8": {
    "equivalentDomains": []
  },
  "policies_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "lastSync_14d4a0bc-763c-436f-8e28-adb6014610f8": "2021-10-03T20:34:28.320Z"
}qÇΩü YNw)ı!ı·ıqıqı)ùÈö3)ı!ıNw§§¿∂Ì˘ı¯)ı…:UÁÄ&Ÿ&õ
î4∂YDÄΩü )ıÈNwIı
/home/aaldli(˘%ÄΩü )ı)ıôı{ıafk#ıâû¥	Kıaçol!©ÉΩü )ı)ı…:UÁÄ&)ıÅNw§
'''
print (regex.match(r'{(?:[^{}]|(?R))*}', text))
# d = dirtyjson.loads(text)
# print (d)

print ("-----------------------------------------------------")

text2 = '''
FZRg1SArJnOeGX5EjNwmRkK1uil/RUzUDQOtoOfF5Ob2CQI3xZFs2PuDu4CdBAMFvyEfWiWonYyso1Acmqheepcl73zDe4v3GM09WyRzZu/yAC2wSTAzIMEMlDi8cB9wTcgdg1AwD/NMbH4Et3y80X3f67bBmKeBBZ7EqSFvWEV4JV1GcAboIHFQuErgKnr604ss0L2fJShqSwIHSlBoPKo2lvC9r8GFPuWCL31xB4MPaqOA86V91J+01bXFA2SZFJbQ3lROeCfhdi3t23r7HtYuUXN/HuF43PVlm2FuAQ9BkCKm4mf841nwDcdhH0HUC3q26PBFI7lna2F9xmaAYie2HEf82Tfm2ekh97FPjCh08Tw+JR/1hUkmv7Qm9thM0xv1o+b0T7lqPzDvMRPNoQjUdwXCxUapMGofUgAPJdLXuQrjSVShNu7B//Ylo7TK72voD7Sub9icnJrl6Tj0dXSYVFcEj/b1nSYLaOUgRVSOv0vzgUbCfoynBQHMdmr3v2fb9bhQhR2i2VAFfydczBeBKDT4FMQxnOrpKaatwLP7hOc8JOY/Ry8y2e1ZIpYpjgQcrcEv1xjS2pqz/G/b1MzBvvG7EfgQaVB7mSq5Tum1pwI/DjO8ST9ZEicYzd9UUftKYK27z5USz8lo+P3oXDuErotDYahuiwWmvZxNZXnmhay0gMXEJZ+BNHkr4QRWWLVk04z1b+A9Vf8CkdZP2B2YUzToJekVRNyn7vXYitjJrU6SK2VjzX7xW6vdiPGNlNJ/dI3MNGgQB8Absk2Jvdov/YE6q0P15wH6Bj0YtEKR03hO5RPnUVjLW6npqfuLlucpasDFMONFp0qSO/Jd/MLQd2B/EEGfqYLsoGlCCyAe0qMplWxemBOyd/GVSiOkQ0SB9Kzcsl57Dhm6CGEQPop5OV0PxyXArA0M+iTdeOWX6rycPa2DKMRWqJg4QEd8LJbj9pZ5870GYCwU7pRxZJkM=|j50YzCfHhLm/y38TX69iSMkURwcD2nhfTwc8s/vIhVQ=",
  "__PROTECTED__key": "AhO8SoHwxLa7hiGZSGsObniZgHoqqCM5JRvgSaRd59CAMIv5f72jwhiSk0oxMe97/vVarMBKAqikz/ZbYRfbL0HlQgIkpE+VFVnew/KB+akOUq1d+2fkBvRPcs4jHEFoXQ==",
  "encProviderKeys": {},
  "encOrgKeys": {},
  "securityStamp": "XUXCQT2RYUZFL7HCC4MT3Y23DIZOOHKT",
  "emailVerified": false,
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
      "revisionDate": "2021-10-03T22:52:14.9536475Z",
      "type": 1,
      "name": "2.jAYz8dhSGF6b4goCNp+fJA==|60TEwR17LVuEoGLelWfPYA==|+n6mzvhUwKM86Nh5Z222P4LZYK4XCji5+jP4jjkvsMo=",
      "notes": "2.ozH60bsxKaNKXmT41BLxjQ==|N9Gr5vT2g7UvPEh2jWo8K6+jtmuOZaUApuZlawk+T8A=|NFqcpc+3rfsGKIxikmI3FWQGfnoEllhvg53N6pAv1ws=",
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
    }
  },
  "sends_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "settings_14d4a0bc-763c-436f-8e28-adb6014610f8": {
    "equivalentDomains": []
  },
  "policies_14d4a0bc-763c-436f-8e28-adb6014610f8": {},
  "lastSync_14d4a0bc-763c-436f-8e28-adb6014610f8": "2021-10-03T20:34:28.320Z"
}^   ËÏD%<:     $   5a162903-3d4f-47f7-8bbf-5deb7dd1fe73ator ÌD%<:     ◊  eyJhbGciOiJSUzI1NiIsImtpZCI6IkJDMzZDMjE0REI0OEYyMzVCNzdEQTNGMTcyMEMxQTM1QTk2MkVBNDNSUzI1NiIsInR5cCI6ImF0K2p3dCIsIng1dCI6InZEYkNGTnRJOGpXM2ZhUHhjZ3dhTmFsaTZrTSJ9.eyJuYmYiOjE2MzMzMDE1MzQsImV4cCI6MTYzMzMwNTEzNCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5iaXR3YXJkZW4uY29tIiwiY2xpZW50X2lkIjoiY2xpIiwic3ViIjoiMTRkNGEwYmMtNzYzYy00MzZmLThlMjgtYWRiNjAxNDYxMGY4IiwiYXV0aF90aW1lIjoxNjMzMjkzMjY4LCJpZHAiOiJiaXR3YXJkZW4iLCJwcmVtaXVtIjpmYWxzZSwiZW1haWwiOiJhYWxkaGFoZUB1bWljaC5lZHUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInNzdGFtcCI6IlhVWENRVDJSWVVaRkw3SENDNE1UM1kyM0RJWk9PSEtUIiwibmFtZSI6IkFobWVkIEFiZHVsc2FsYW0gQWxkaGFoZXJpIiwiZGV2aWNlIjoiNWExNjI5MDMtM2Q0Zi00N2Y3LThiYmYtNWRlYjdkZDFmZTczIiwianRpIjoiQjM5NTg3ODJDNzMyNEUyRUZCOTM5QUQzRURCODM3MjkiLCJpYXQiOjE2MzMzMDE1MzQsInNjb3BlIjpbImFwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJBcHBsaWNhdGlvbiJdfQ.SoNdysByTq4-CNOkVuieFt1V6GFYpeIKnPAw93scqr6pj3nbUBgRyDwS9nC0Kd4rF1cdRMdMbQYBPjErbE-W3jNRJmPz-rH45KdNQeR7ieVgZyO3V2lickRtLcr_A__n-YN4TFkbFOvp3ttDsgdMFOUZqD_RrsJ-kA6MtLa48Z6cfQl-7Gemg8rQcXveT2XgqK6xR6hEn5zS6K_sRBY7TEcUGUlxTYTgUD69G4B3JyO6eTseaHXQmzQ97nlPHOSHefyGyZ3l6dKAUG4Czd7YpfBZOKvfc1ZB6-CWwJMBLXwv1nbUtBGncuayYo6lC6QzWX3Ni1KCsyvb7pIgxTsujJ0KXPaCdLi_Wrhdu-p94EIQ1e-AnMDw3VqFLbu9IgoK5b3eMaE_zPHtejSkbFNzo1263nNiw2fZlBEGT7orto-Na9Os_60qADBca2E501NzdEf2C
'''

# d1 = dirtyjson.loads(text2)
# print (d1)
d1 = json.loads(text2)
print (d1)

# print (regex.match(r'{(?:[^{}]|(?R))*}', text2))

