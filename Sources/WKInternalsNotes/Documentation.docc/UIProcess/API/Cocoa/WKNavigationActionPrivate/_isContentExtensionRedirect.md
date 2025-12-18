# ``WKInternalsNotes/WKNavigationAction/_isContentExtensionRedirect``

コンテンツ拡張によるリダイレクトかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isContentExtensionRedirect;
```

## Default Value
`_navigationAction->isContentRuleListRedirect()` の結果。

## Discussion
API::NavigationAction の `isContentRuleListRedirect()` をそのまま返す。

## References
- [`WKNavigationActionPrivate.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L61)
- [`WKNavigationAction.mm#L227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L227)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
