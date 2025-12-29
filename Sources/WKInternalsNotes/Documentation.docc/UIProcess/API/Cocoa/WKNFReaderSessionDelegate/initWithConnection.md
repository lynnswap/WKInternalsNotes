# ``WKInternalsNotes/WKNFReaderSessionDelegate/initWithConnection(_:)``

`NfcConnection` を保持する初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)initWithConnection:(WebKit::NfcConnection&)connection;
```

## Discussion
`[super init]` に成功した場合、弱参照として `_connection` を保持する。

## References
- [`WKNFReaderSessionDelegate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WKNFReaderSessionDelegate.h#L36)
- [`WKNFReaderSessionDelegate.mm#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WKNFReaderSessionDelegate.mm#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
