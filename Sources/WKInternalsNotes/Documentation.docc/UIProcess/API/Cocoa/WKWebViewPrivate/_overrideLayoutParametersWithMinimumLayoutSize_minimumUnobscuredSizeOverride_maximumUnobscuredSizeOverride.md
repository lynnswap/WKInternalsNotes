# ``WKInternalsNotes/WKWebView/_overrideLayoutParametersWithMinimumLayoutSize(_:minimumUnobscuredSizeOverride:maximumUnobscuredSizeOverride:)``

`_overrideLayoutParametersWithMinimumLayoutSize` を実行する。

## Objective-C Declaration
```objective-c
- (void)_overrideLayoutParametersWithMinimumLayoutSize:(CGSize)minimumLayoutSize minimumUnobscuredSizeOverride:(CGSize)minimumUnobscuredSizeOverride maximumUnobscuredSizeOverride:(CGSize)maximumUnobscuredSizeOverride WK_API_AVAILABLE(ios(17.4), visionos(1.1));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L759`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L759)
- [`API/ios/WKWebViewIOS.mm#L4878`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4878)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
