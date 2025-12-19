# ``WKInternalsNotes/WKWebView/_overrideLayoutParametersWithMinimumLayoutSize(_:maximumUnobscuredSizeOverride:)``

`_overrideLayoutParametersWithMinimumLayoutSize` を実行する。

## Objective-C Declaration
```objective-c
- (void)_overrideLayoutParametersWithMinimumLayoutSize:(CGSize)minimumLayoutSize maximumUnobscuredSizeOverride:(CGSize)maximumUnobscuredSizeOverride WK_API_DEPRECATED_WITH_REPLACEMENT("-_overrideLayoutParametersWithMinimumLayoutSize:minimumUnobscuredSizeOverride:maximumUnobscuredSizeOverride:", ios(9.0, 17.4), visionos(1.0, 1.1));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L758`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L758)
- [`WKWebViewIOS.mm#L4878`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4878)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
