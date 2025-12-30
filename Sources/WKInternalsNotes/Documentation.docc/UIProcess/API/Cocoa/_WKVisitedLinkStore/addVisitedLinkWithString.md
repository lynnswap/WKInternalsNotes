# ``WKInternalsNotes/_WKVisitedLinkStore/addVisitedLinkWithString(_:)``

文字列から訪問済みリンクを登録する。

## Objective-C Declaration
```objective-c
- (void)addVisitedLinkWithString:(NSString *)string WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
文字列の共有ハッシュを計算し、`addVisitedLinkHash` を呼ぶ。

## References
- [`_WKVisitedLinkStore.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKVisitedLinkStore.h#L33)
- [`_WKVisitedLinkStore.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKVisitedLinkStore.mm#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
