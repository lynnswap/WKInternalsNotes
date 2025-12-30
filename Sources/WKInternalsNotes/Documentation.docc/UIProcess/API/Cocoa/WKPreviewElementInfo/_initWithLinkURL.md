# ``WKInternalsNotes/WKPreviewElementInfo/_initWithLinkURL(_:)``

`linkURL` をコピーして保持する初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithLinkURL:(NSURL *)url;
```

## Discussion
`[super init]` が失敗した場合は `nil` を返し、成功時は `url` をコピーして `_linkURL` に保持する。

## References
- [`WKPreviewElementInfoInternal.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreviewElementInfoInternal.h#L37)
- [`WKPreviewElementInfo.mm#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreviewElementInfo.mm#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
