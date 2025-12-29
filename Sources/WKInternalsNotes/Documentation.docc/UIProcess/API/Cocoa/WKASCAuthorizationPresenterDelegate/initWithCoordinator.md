# ``WKInternalsNotes/WKASCAuthorizationPresenterDelegate/initWithCoordinator(_:)``

`AuthenticatorPresenterCoordinator` を保持する初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)initWithCoordinator:(WebKit::AuthenticatorPresenterCoordinator&)coordinator;
```

## Discussion
`[super init]` に成功した場合、弱参照として `_coordinator` を保持する。

## References
- [`WKASCAuthorizationPresenterDelegate.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WKASCAuthorizationPresenterDelegate.h#L40)
- [`WKASCAuthorizationPresenterDelegate.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WKASCAuthorizationPresenterDelegate.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
