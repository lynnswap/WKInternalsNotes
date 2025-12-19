# ``WKInternalsNotes/WKWebViewContentProvider/web_countStringMatches(_:options:maxCount:)``

文字列の一致数を報告する。

## Objective-C Declaration
```objective-c
- (void)web_countStringMatches:(NSString *)string options:(_WKFindOptions)options maxCount:(NSUInteger)maxCount;
```

## Discussion
`WKUSDPreviewView` では `findClient().didCountStringMatches` を呼び、0 件として報告する。

## References
- [`WKWebViewContentProvider.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProvider.h#L48)
- [`WKUSDPreviewView.mm#L206`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUSDPreviewView.mm#L206)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
