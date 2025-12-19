# ``WKInternalsNotes/WKSecurityOrigin/isSameSiteAsURL(_:)``

指定 URL と同一サイトかを判定する。

## Objective-C Declaration
```objective-c
-(BOOL)isSameSiteAsURL:(NSURL *)url WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
自身の `WebCore::SecurityOrigin` と、`URL { url }` から生成した `WebCore::SecurityOrigin` を比較して `isSameSiteAs` の結果を返す。

## References
- [`WKSecurityOriginPrivate.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSecurityOriginPrivate.h#L30)
- [`WKSecurityOrigin.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKSecurityOrigin.mm#L76)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
