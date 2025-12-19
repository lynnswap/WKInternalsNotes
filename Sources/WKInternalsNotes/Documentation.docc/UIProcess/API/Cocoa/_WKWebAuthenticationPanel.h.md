# ``WKInternalsNotes/_WKWebAuthenticationPanel``

## Topics

### WKTesting

#### Properties
- ``WKInternalsNotes/_WKWebAuthenticationPanel/mockConfiguration``

#### Methods
- ``WKInternalsNotes/_WKWebAuthenticationPanel/convertToCoreCreationOptionsWithOptions(_:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/convertToCoreRequestOptionsWithOptions(_:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataHash(_:options:userVerificationAvailability:authenticatorSupportedCredentialParameters:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentialsWithAccessGroup(_:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentialsWithCredentialIDAndAccessGroup(_:credentialID:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentialsWithRPIDAndAccessGroup(_:rpID:)``

### Type

#### Properties
- ``WKInternalsNotes/_WKWebAuthenticationPanel/delegate``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/relyingPartyID``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/transports``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/type``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/userName``

#### Methods
- ``WKInternalsNotes/_WKWebAuthenticationPanel/cancel()``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/clearAllLocalAuthenticatorCredentials()``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/deleteLocalAuthenticatorCredentialWithGroupAndID(_:credential:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/deleteLocalAuthenticatorCredentialWithID(_:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeGetAssertionCommandWithClientDataHash(_:options:userVerificationAvailability:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeGetAssertionCommandWithClientDataHash(_:options:userVerificationAvailability:authenticatorSupportedExtensions:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeGetAssertionCommandWithClientDataJSON(_:options:userVerificationAvailability:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeGetAssertionCommandWithClientDataJSON(_:options:userVerificationAvailability:authenticatorSupportedExtensions:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataHash(_:options:userVerificationAvailability:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataHash(_:options:userVerificationAvailability:authenticatorSupportedExtensions:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataJSON(_:options:userVerificationAvailability:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/encodeMakeCredentialCommandWithClientDataJSON(_:options:userVerificationAvailability:authenticatorSupportedExtensions:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/exportLocalAuthenticatorCredentialWithGroupAndID(_:credential:error:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/exportLocalAuthenticatorCredentialWithID(_:error:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentials()``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentialsWithCredentialID(_:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentialsWithRPID(_:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getAssertionWithChallenge(_:origin:options:completionHandler:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getAssertionWithClientDataHash(_:options:completionHandler:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getAssertionWithMediationRequirement(_:clientDataHash:options:completionHandler:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getClientDataJSONForAuthenticationType(_:challenge:origin:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/getClientDataJSONWithTopOrigin(_:challenge:origin:topOrigin:crossOrigin:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/importLocalAuthenticatorCredential(_:error:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/importLocalAuthenticatorWithAccessGroup(_:credential:error:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/init()``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/isUserVerifyingPlatformAuthenticatorAvailable()``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/makeCredentialWithChallenge(_:origin:options:completionHandler:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/makeCredentialWithClientDataHash(_:options:completionHandler:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/makeCredentialWithMediationRequirement(_:clientDataHash:options:completionHandler:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/setDisplayNameForLocalCredentialWithGroupAndID(_:credential:displayName:)``
- ``WKInternalsNotes/_WKWebAuthenticationPanel/setNameForLocalCredentialWithGroupAndID(_:credential:name:)``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`_WKWebAuthenticationPanel.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h) |
