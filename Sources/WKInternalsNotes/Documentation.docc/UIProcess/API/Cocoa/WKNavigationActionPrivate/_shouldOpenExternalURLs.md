# ``WKInternalsNotes/WKNavigationAction/_shouldOpenExternalURLs``

外部 URL を開くべきかどうかを返す（非推奨）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _shouldOpenExternalURLs WK_API_DEPRECATED("use _shouldOpenExternalSchemes and _shouldOpenAppLinks", macos(10.11, 10.11), ios(9.0, 9.0));
```

## Default Value
`[self _shouldOpenExternalSchemes]` の結果。

## Discussion
`_shouldOpenExternalSchemes` の結果をそのまま返す互換用プロパティ。

## References
- [`WKNavigationActionPrivate.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L52)
- [`WKNavigationAction.mm#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L212)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
