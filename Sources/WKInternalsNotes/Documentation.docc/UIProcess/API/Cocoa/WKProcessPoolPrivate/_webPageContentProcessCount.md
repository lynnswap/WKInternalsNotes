# ``WKInternalsNotes/WKProcessPool/_webPageContentProcessCount()``

Web ページを実行中の WebProcess 数を返す（テスト用）。

## Objective-C Declaration
```objective-c
- (size_t)_webPageContentProcessCount WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`processes().size()` を基準に、`useSeparateServiceWorkerProcess()` の場合は `serviceWorkerProxiesCount()` を差し引く。

## References
- [`WKProcessPoolPrivate.h#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L158)
- [`WKProcessPool.mm#L486`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L486)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
