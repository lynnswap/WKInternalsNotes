# ``WKInternalsNotes/_WKAuthenticatorAssertionResponse/userHandle``

userHandle を保持する（nullable）。

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, readonly) NSData *userHandle;
```

## Default Value
初期化時に渡された値を保持する。

## Discussion
初期化時に `userHandle` を `retain` して保持する。`userHandle` は `nil` の可能性がある。

## References
- [`_WKAuthenticatorAssertionResponse.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponse.h#L37)
- [`_WKAuthenticatorAssertionResponse.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponse.mm#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
