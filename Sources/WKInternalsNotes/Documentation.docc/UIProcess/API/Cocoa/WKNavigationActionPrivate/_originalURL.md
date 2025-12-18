# ``WKInternalsNotes/WKNavigationAction/_originalURL``

ナビゲーションの元 URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *_originalURL;
```

## Default Value
`_navigationAction->originalURL().createNSURL()` の結果。

## Discussion
API::NavigationAction の `originalURL()` を `NSURL` に変換して返す。

## References
- [`WKNavigationActionPrivate.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L44)
- [`WKNavigationAction.mm#L182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L182)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
