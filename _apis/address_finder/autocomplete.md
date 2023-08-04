---
category: Address Finder
name: Address Autocomplete
code_snippets:
  AU Address Autocomplete: address_finder/au_address_autocomplete.py
  NZ Address Autocomplete: address_finder/nz_address_autocomplete.py
  CA Address Autocomplete: address_finder/ca_address_autocomplete.py
---

## Official Reference:

[AU Address Autocomplete](https://addressfinder.com.au/api/au/address/autocomplete/)

[NZ Address Autocomplete](https://addressfinder.com.au/api/nz/address/autocomplete/)

[CA Address Autocomplete](https://addressfinder.com.au/api/international/address/autocomplete/ca)

## Usage Scenarios

User filled in PaymentForm

## Code related

- Apex Code  
   `addressValidationCon.AddressFinderSearch - calls -> AddressFinderUtil.dataToolsSearch - calls -> this API`
- Salesforce Lightning Component Page JavaScript Code  
   `checkoutMComponent directly calls this API via ajax`
