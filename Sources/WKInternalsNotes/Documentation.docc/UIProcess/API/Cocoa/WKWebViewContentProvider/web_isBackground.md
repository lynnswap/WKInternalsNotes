# ``WKInternalsNotes/WKWebViewContentProvider/web_isBackground``

背景表示かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL web_isBackground;
```

## Discussion
`WKUSDPreviewView` では `isBackground` の値をそのまま返す。

## References
- [`WKWebViewContentProvider.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProvider.h#L54)
- [`WKUSDPreviewView.mm#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUSDPreviewView.mm#L199)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
