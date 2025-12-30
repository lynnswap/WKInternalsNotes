# ``WKInternalsNotes/_WKVisitedLinkStore/containsVisitedLinkWithURL(_:)``

指定 URL が訪問済みかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)containsVisitedLinkWithURL:(NSURL *)URL WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`URL.absoluteString` から共有ハッシュを計算し、`containsVisitedLinkHash` で判定する。

## References
- [`_WKVisitedLinkStore.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKVisitedLinkStore.h#L35)
- [`_WKVisitedLinkStore.mm#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKVisitedLinkStore.mm#L72)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
