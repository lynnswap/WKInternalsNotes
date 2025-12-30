# ``WKInternalsNotes/_WKVisitedLinkStore/removeVisitedLinkWithURL(_:)``

指定 URL を訪問済みから削除する。

## Objective-C Declaration
```objective-c
- (void)removeVisitedLinkWithURL:(NSURL *)URL WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`URL.absoluteString` から共有ハッシュを計算し、`removeVisitedLinkHash` を呼ぶ。

## References
- [`_WKVisitedLinkStore.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKVisitedLinkStore.h#L36)
- [`_WKVisitedLinkStore.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKVisitedLinkStore.mm#L79)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
