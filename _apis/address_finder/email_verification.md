---
category: Address Finder
name: Email Verification
code_snippets:
  Valid Email Verification: address_finder/valid_email_verification.py
  Invalid Email Verification: address_finder/invalid_email_verification.py
---

## Official Reference

[Email Verification](https://addressfinder.com.au/api/email/verification/)

## Usage Scenerios

When user submit a Payment from a Payment Form, it checks whether the email is valid

## Code Related

Currently this API is not yet integrated into payment2us, in order to integrate it:

1. Modify Picklist (Multi-Select) `AAkPay__Validate__c` for Merchant Facility and ensure `Email` option is available for `AAkPay__Address_Helper__c` == `Address Finder`
2. Add a new method `addressValidationCon.addressFinderEmail` similar to the current already existed method `addressValidationCon.dataToolsEmail`
3. Search the general code base for `PaymentSetting.AAkPay__Validate__c.contains('Email')`, e.g. checkoutCon.cls, manualPaymentCon.cls, payments2Us.cls, currently the pattern is similar to

```java
    if(PaymentSetting.AAkPay**Validate**c.contains('Email')){
        addressValidation.dataToolsEmail(xxx)
    }
```

It may need to modify to

```java
    if(PaymentSetting.AAkPay__Validate__c.contains('Email')){
        if(PaymentSetting.AAkPay__Address_Helper__c == 'DataTools Kleber'){
                addressValidation.dataToolsEmail(xxx)
            }else{
                addressValidation.addressFinderEmail(xxx)
            }
        }
    }
```
