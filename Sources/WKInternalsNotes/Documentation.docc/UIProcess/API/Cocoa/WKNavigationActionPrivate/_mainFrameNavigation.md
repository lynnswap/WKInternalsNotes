# ``WKInternalsNotes/WKNavigationAction/_mainFrameNavigation``

メインフレームの WKNavigation を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKNavigation *_mainFrameNavigation WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
`_navigationAction->protectedMainFrameNavigation()` をラップした結果。

## Discussion
`protectedMainFrameNavigation()` が null の場合は `nil` を返す。

## References
- [`WKNavigationActionPrivate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L63)
- [`WKNavigationAction.mm#L237`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L237)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
