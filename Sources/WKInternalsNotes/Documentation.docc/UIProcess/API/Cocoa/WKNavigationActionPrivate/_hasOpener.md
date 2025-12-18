# ``WKInternalsNotes/WKNavigationAction/_hasOpener``

opener を持つかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _hasOpener WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
`_navigationAction->hasOpener()` の結果。

## Discussion
API::NavigationAction の `hasOpener()` を返す。

## References
- [`WKNavigationActionPrivate.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L68)
- [`WKNavigationAction.mm#L288`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L288)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
