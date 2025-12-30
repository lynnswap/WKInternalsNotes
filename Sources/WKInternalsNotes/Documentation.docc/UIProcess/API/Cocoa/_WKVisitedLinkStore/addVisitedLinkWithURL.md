# ``WKInternalsNotes/_WKVisitedLinkStore/addVisitedLinkWithURL(_:)``

URL を訪問済みとして登録する。

## Objective-C Declaration
```objective-c
- (void)addVisitedLinkWithURL:(NSURL *)URL;
```

## Discussion
`URL.absoluteString` から共有ハッシュを計算し、`addVisitedLinkHash` を呼ぶ。

## References
- [`_WKVisitedLinkStore.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKVisitedLinkStore.h#L32)
- [`_WKVisitedLinkStore.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKVisitedLinkStore.mm#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
