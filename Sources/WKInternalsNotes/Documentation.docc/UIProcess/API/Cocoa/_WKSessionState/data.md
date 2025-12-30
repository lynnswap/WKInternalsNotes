# ``WKInternalsNotes/_WKSessionState/data``

保持している `SessionState` をエンコードした `NSData` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSData *data;
```

## Default Value
`_sessionState` の内容に依存。

## Discussion
`encodeSessionState` の結果を `autorelease` して返す。

## References
- [`_WKSessionState.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSessionState.h#L36)
- [`_WKSessionState.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKSessionState.mm#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
