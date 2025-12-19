# ``WKInternalsNotes/WKWebViewContentProvider/web_contentView``

コンテンツ表示用のビューを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIView *web_contentView;
```

## Discussion
`WKUSDPreviewView` では自分自身 (`self`) を返す。

## References
- [`WKWebViewContentProvider.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProvider.h#L51)
- [`WKUSDPreviewView.mm#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUSDPreviewView.mm#L173)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
