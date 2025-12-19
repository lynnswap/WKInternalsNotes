# ``WKInternalsNotes/_WKWebPushDaemonConnectionConfiguration/bundleIdentifierOverrideForTesting``

テスト用の bundle identifier 上書き値を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, nullable) NSString *bundleIdentifierOverrideForTesting;
```

## Default Value
`init` では設定されず `nil`。

## Discussion
`initWithConfiguration:` で `WebPushDaemonConnectionConfiguration` に渡され、テスト時の識別子上書きに使われる。

## References
- [`_WKWebPushDaemonConnection.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L49)
- [`_WKWebPushDaemonConnection.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L67)
- [`_WKWebPushDaemonConnection.mm#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L83)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
