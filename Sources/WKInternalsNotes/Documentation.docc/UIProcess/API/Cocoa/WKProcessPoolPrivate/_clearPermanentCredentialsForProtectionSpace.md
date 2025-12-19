# ``WKInternalsNotes/WKProcessPool/_clearPermanentCredentialsForProtectionSpace(_:)``

指定保護空間の永続資格情報を削除する。

## Objective-C Declaration
```objective-c
- (void)_clearPermanentCredentialsForProtectionSpace:(NSURLProtectionSpace *)protectionSpace WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
`NSURLProtectionSpace` を `WebCore::ProtectionSpace` に変換して `clearPermanentCredentialsForProtectionSpace` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L180`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L180)
- [`WKProcessPool.mm#L633`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L633)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
