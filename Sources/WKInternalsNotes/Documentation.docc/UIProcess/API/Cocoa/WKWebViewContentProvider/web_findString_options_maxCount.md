# ``WKInternalsNotes/WKWebViewContentProvider/web_findString(_:options:maxCount:)``

文字列検索結果を通知する。

## Objective-C Declaration
```objective-c
- (void)web_findString:(NSString *)string options:(_WKFindOptions)options maxCount:(NSUInteger)maxCount;
```

## Discussion
`WKUSDPreviewView` では `findClient().didFailToFindString` を呼び、検索失敗として扱う。

## References
- [`WKWebViewContentProvider.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProvider.h#L49)
- [`WKUSDPreviewView.mm#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUSDPreviewView.mm#L212)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
