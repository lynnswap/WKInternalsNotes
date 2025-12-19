# ``WKInternalsNotes/WKSecurityOrigin/isSameSiteAsOrigin(_:)``

別の `WKSecurityOrigin` と同一サイトかを判定する。

## Objective-C Declaration
```objective-c
-(BOOL)isSameSiteAsOrigin:(WKSecurityOrigin *)origin WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
自身と引数の `WKSecurityOrigin` を `WebCore::SecurityOrigin` に変換し、`isSameSiteAs` の結果を返す。

## References
- [`WKSecurityOriginPrivate.h#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSecurityOriginPrivate.h#L29)
- [`WKSecurityOrigin.mm#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSecurityOrigin.mm#L68)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
